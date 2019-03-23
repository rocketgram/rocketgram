# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).

import logging
from contextlib import suppress
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar, Optional, Callable, Awaitable

try:
    import ujson as json
except ModuleNotFoundError:
    import json

from . import types, update, errors, requests
from .context import Context
from .errors import TelegramSendError
from .keyboards.keyboard import Keyboard

if TYPE_CHECKING:
    from .routers import BaseRouter
    from .connectors import BaseConnector

API_URL = "https://api.telegram.org/bot%s/"
API_FILE_URL = "https://api.telegram.org/file/bot%s/"

logger = logging.getLogger('rocketgram.bot')
logger_raw_in = logging.getLogger('rocketgram.raw.in')
logger_raw_out = logging.getLogger('rocketgram.raw.out')


@dataclass
class PreparedRequest:
    send_file: bool
    request: dict


def _make_method(request: type(requests.Request)) -> Callable:
    def method(self, *args, **kwargs) -> Awaitable:
        return self.send(request(*args, **kwargs))

    for prop in ('__name__', '__qualname__', '__doc__', '__annotations__'):
        if hasattr(request, prop):
            attr = getattr(request, prop)
            setattr(method, prop, attr)
            continue

    return method


class Bot:
    def __init__(self, token: str, *, connector: 'BaseConnector' = None, router: 'BaseRouter' = None,
                 globals_class: ClassVar = dict, context_data_class: ClassVar = dict,
                 api_url: str = API_URL, api_file_url: str = API_FILE_URL):

        self.__token = token
        self.__full_api_url = api_url % token
        self.__full_api_file_url = api_file_url % token

        self.__name = None
        self.__user_id = int(self.__token.split(':')[0])

        self.__parse_mode = 'html'
        self.__disable_notification = False
        self.__disable_web_page_preview = False

        self.__router = router
        if self.__router is None:
            from .routers.dispatcher import Dispatcher
            self.__router = Dispatcher()

        self.__connector = connector
        if self.__connector is None:
            from .connectors import AioHttpConnector
            self.__connector = AioHttpConnector()

        assert issubclass(globals_class, dict), "`globals_class` must be `dict` or subcalss of `dict`!"
        assert issubclass(context_data_class, dict), "`context_data_class` must be `dict` or subcalss of `dict`!"

        self.__globals = globals_class()
        self.__context_data_class = context_data_class

    @property
    def token(self):
        """Bot's token."""

        return self.__token

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if self.__name is not None:
            raise TypeError('Bot''s name can be set one time.')

        self.__name = name

    name = property(fget=get_name, fset=set_name, doc="Bot's username. Can be set one time.")

    @property
    def user_id(self):
        """Bot's user_id."""

        return self.__user_id

    @property
    def router(self):
        """Bot's dispatcher."""

        return self.__router

    @property
    def connector(self):
        """Bot's connector."""

        return self.__connector

    def get_parse_mode(self):
        return self.__parse_mode

    def set_parse_mode(self, parse_mode: str):
        self.__parse_mode = parse_mode

    parse_mode = property(get_parse_mode, set_parse_mode, doc="Default parse_mode for send messages.")

    def get_disable_web_page_preview(self):
        return self.__disable_web_page_preview

    def set_disable_web_page_preview(self, disable_web_page_preview: bool):
        self.__disable_web_page_preview = disable_web_page_preview

    disable_web_page_preview = property(get_disable_web_page_preview, set_disable_web_page_preview,
                                        doc="Default disable_web_page_preview for send messages.")

    def get_disable_notification(self):
        return self.__disable_notification

    def set_disable_notification(self, disable_notification: bool):
        self.__disable_notification = disable_notification

    disable_notification = property(get_disable_notification, set_disable_notification,
                                    doc="Default disable_notification for send messages.")

    @property
    def globals(self):
        """Bot's globals data storage."""
        return self.__globals

    async def init(self):
        """Initializes connector and dispatcher.
        Performs bot initialization authorize bot on telegram and sets bot's name.

        Must be called before any operation with bot."""

        logger.debug('Performing init...')

        await self.connector.init()
        await self.router.init(self)

        return True

    async def shutdown(self):
        """Release bot's resources.

        Must be called after bot work was done."""

        logger.debug('Performing shutdown...')

        await self.router.shutdown(self)
        await self.connector.shutdown()

    async def process(self, upd, *, webhook: bool = False,
                      webhook_sendfile: bool = False) -> Optional[PreparedRequest]:
        try:
            if not isinstance(upd, update.Update):
                upd = update.Update.parse(json.loads(upd))

            logger_raw_in.debug('Raw in: %s', upd.raw)

            context_data = self.__context_data_class()
            ctx = Context(self, upd, context_data)

            await self.router.process(ctx)

            prepared = None
            send_webhook_request = False

            for req in ctx.get_webhook_requests():
                # prepare request
                if not send_webhook_request and webhook:
                    prepared = self.prepare_request(req, with_method=True)
                    if webhook_sendfile or not prepared.send_file:
                        send_webhook_request = True
                        continue

                # fallback and send by hands
                with suppress(Exception):
                    await self.send(req)

            if send_webhook_request:
                return prepared

        except errors.TelegramStopRequest as e:
            logger.debug('Request was %s interrupted: %s', upd.update_id, e)
        except Exception:
            logger.exception('Got exception during processing request')

    async def send(self, req: requests.Request) -> update.Response:
        prepared = self.prepare_request(req)
        url = self.__full_api_url + req.method

        if prepared.send_file:
            response = await self.__connector.send_file(url, prepared.request)
        else:
            response = await self.__connector.send(url, prepared.request)

        if response.status == 200:
            return update.Response.parse(response.data, req)
        else:
            r = update.Response.parse(response.data, req.method)
            if r:
                logger.debug("Error from telegram: %s '%s'", response.status, r.description)
                raise TelegramSendError(req.method, req, response.status, r)
            else:
                logger.debug("Error from telegram: %s", response.status)
                raise TelegramSendError(req.method, req, response.status, None)

    def prepare_request(self, req: requests.Request, with_method=False) -> PreparedRequest:
        request_data = req.render(with_method=with_method)

        if request_data.get('parse_mode') is types.Default:
            request_data['parse_mode'] = self.parse_mode
        if request_data.get('disable_notification') is types.Default:
            request_data['disable_notification'] = self.disable_notification
        if request_data.get('disable_web_page_preview') is types.Default:
            request_data['disable_web_page_preview'] = self.disable_web_page_preview

        if isinstance(request_data.get('reply_markup'), Keyboard):
            request_data['reply_markup'] = request_data['reply_markup'].render()

        send_file = False
        data = dict()
        for k, v in request_data.items():
            if v is not None:
                data[k] = v
            if isinstance(v, types.InputFile):
                send_file = True

        return PreparedRequest(send_file, data)

    get_updates = _make_method(requests.GetUpdates)
    set_webhook = _make_method(requests.SetWebhook)
    delete_webhook = _make_method(requests.DeleteWebhook)
    get_webhook_info = _make_method(requests.GetWebhookInfo)
    get_me = _make_method(requests.GetMe)
    send_message = _make_method(requests.SendMessage)
    forward_message = _make_method(requests.ForwardMessage)
    send_photo = _make_method(requests.SendPhoto)
    send_audio = _make_method(requests.SendAudio)
    send_document = _make_method(requests.SendDocument)
    send_video = _make_method(requests.SendVideo)
    send_animation = _make_method(requests.SendAnimation)
    send_voice = _make_method(requests.SendVoice)
    send_video_note = _make_method(requests.SendVideoNote)
    send_media_group = _make_method(requests.SendMediaGroup)
    send_location = _make_method(requests.SendLocation)
    edit_message_live_location = _make_method(requests.EditMessageLiveLocation)
    stop_message_live_location = _make_method(requests.StopMessageLiveLocation)
    send_venue = _make_method(requests.SendVenue)
    send_contact = _make_method(requests.SendContact)
    send_chat_action = _make_method(requests.SendChatAction)
    get_user_profile_photos = _make_method(requests.GetUserProfilePhotos)
    get_file = _make_method(requests.GetFile)
    kick_chat_member = _make_method(requests.KickChatMember)
    unban_chat_member = _make_method(requests.UnbanChatMember)
    restrict_chat_member = _make_method(requests.RestrictChatMember)
    promote_chat_member = _make_method(requests.PromoteChatMember)
    export_chat_invite_link = _make_method(requests.ExportChatInviteLink)
    set_chat_photo = _make_method(requests.SetChatPhoto)
    delete_chat_photo = _make_method(requests.DeleteChatPhoto)
    set_chat_title = _make_method(requests.SetChatTitle)
    set_chat_description = _make_method(requests.SetChatDescription)
    pin_chat_message = _make_method(requests.PinChatMessage)
    unpin_chat_message = _make_method(requests.UnpinChatMessage)
    leave_chat = _make_method(requests.LeaveChat)
    get_chat = _make_method(requests.GetChat)
    get_chat_administrators = _make_method(requests.GetChatAdministrators)
    get_chat_members_count = _make_method(requests.GetChatMembersCount)
    get_chat_member = _make_method(requests.GetChatMember)
    set_chat_sticker_set = _make_method(requests.SetChatStickerSet)
    delete_shat_sticker_set = _make_method(requests.DeleteChatStickerSet)
    answer_callback_query = _make_method(requests.AnswerCallbackQuery)
    edit_message_text = _make_method(requests.EditMessageText)
    edit_message_caption = _make_method(requests.EditMessageCaption)
    edit_message_media = _make_method(requests.EditMessageMedia)
    edit_message_reply_markup = _make_method(requests.EditMessageReplyMarkup)
    delete_message = _make_method(requests.DeleteMessage)
    send_sticker = _make_method(requests.SendSticker)
    get_sticker_set = _make_method(requests.GetStickerSet)
    upload_sticker_file = _make_method(requests.UploadStickerFile)
    create_new_sticker_set = _make_method(requests.CreateNewStickerSet)
    add_sticker_to_set = _make_method(requests.AddStickerToSet)
    set_sticker_position_in_set = _make_method(requests.SetStickerPositionInSet)
    delete_sticker_from_set = _make_method(requests.DeleteStickerFromSet)
    answer_inline_query = _make_method(requests.AnswerInlineQuery)
    send_invoice = _make_method(requests.SendInvoice)
    answer_shipping_query = _make_method(requests.AnswerShippingQuery)
    answer_pre_checkout_query = _make_method(requests.AnswerPreCheckoutQuery)
    set_passport_data_errors = _make_method(requests.SetPassportDataErrors)
    send_game = _make_method(requests.SendGame)
    set_game_score = _make_method(requests.SetGameScore)
    get_game_high_scores = _make_method(requests.GetGameHighScores)
