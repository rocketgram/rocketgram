# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import inspect
import logging
import asyncio
from contextlib import suppress
from typing import ClassVar, Callable, Awaitable

from .context import Context
from .errors import RocketgramRequest429Error, RocketgramStopRequest
from .errors import RocketgramRequestError, RocketgramRequest400Error, RocketgramRequest401Error
from .requests import *
from .update import Update, Response

if TYPE_CHECKING:
    from .executors import Executor
    from .routers import BaseRouter
    from .connectors import BaseConnector
    from .middlewares import Middleware

logger = logging.getLogger('rocketgram.bot')
logger_raw_in = logging.getLogger('rocketgram.raw.in')
logger_raw_out = logging.getLogger('rocketgram.raw.out')


def _make_method(request: type(Request)) -> Callable:
    def method(self, *args, **kwargs) -> Awaitable:
        return self.send(request(*args, **kwargs))

    for prop in ('__name__', '__qualname__', '__doc__', '__annotations__'):
        if hasattr(method, prop) and hasattr(request, prop):
            setattr(method, prop, getattr(request, prop))

    return method


class Bot:
    __slots__ = ('__token', '__name', '__user_id', '__middlewares', '__router', '__connector', '__globals',
                 '__context_data_class')

    def __init__(self, token: str, *, connector: 'BaseConnector' = None, router: 'BaseRouter' = None,
                 globals_class: ClassVar = dict, context_data_class: ClassVar = dict):

        self.__token = token

        self.__name = None
        self.__user_id = int(self.__token.split(':')[0])
        self.__middlewares: List['Middleware'] = list()

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

    def set_name(self, name):
        if self.__name is not None:
            raise TypeError('Bot''s name can be set one time.')

        self.__name = name

    name = property(fget=lambda self: self.__name, fset=set_name, doc="Bot's username. Can be set one time.")

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

    @property
    def globals(self):
        """Bot's globals data storage."""
        return self.__globals

    def middleware(self, middleware: 'Middleware'):
        """Registers middleware."""

        self.__middlewares.append(middleware)

    async def init(self):
        """Initializes connector and dispatcher.
        Performs bot initialization authorize bot on telegram and sets bot's name.

        Must be called before any operation with bot."""

        logger.debug('Performing init...')

        await self.connector.init()

        for md in self.__middlewares:
            m = md.init(self)
            if inspect.isawaitable(m):
                await m

        await self.router.init(self)

        return True

    async def shutdown(self):
        """Release bot's resources.

        Must be called after bot work was done."""

        logger.debug('Performing shutdown...')

        await self.router.shutdown(self)

        for md in reversed(self.__middlewares):
            m = md.init(self)
            if inspect.isawaitable(m):
                await m

        await self.connector.shutdown()

    async def process(self, executor: 'Executor', update: Update) -> Optional[Request]:
        logger_raw_in.debug('Raw in: %s', update.raw)

        context_data = self.__context_data_class()
        ctx = Context(self, update, context_data)

        try:
            for md in self.__middlewares:
                ctx = md.process(ctx)
                if inspect.isawaitable(ctx):
                    ctx = await ctx

            await self.router.process(ctx)

            webhook_request = None

            for req in ctx.get_webhook_requests():
                # set request to return if it can be processed
                if webhook_request is None and executor.can_process_webhook_request(req):
                    for md in self.__middlewares:
                        req = md.before_request(self, req)
                        if inspect.isawaitable(req):
                            req = await req
                    webhook_request = req
                    continue

                # fallback and send by hands
                with suppress(Exception):
                    await self.send(req)

            return webhook_request

        except RocketgramStopRequest as e:
            logger.debug('Request `%s` was interrupted: `%s`', update.update_id, e)
        except Exception as error:

            for md in self.__middlewares:
                with suppress(Exception):
                    m = md.process_error(ctx, error)
                    if inspect.isawaitable(m):
                        await m

            logger.exception('Got exception during processing request:')

    async def send(self, request: Request) -> Response:
        try:
            for md in self.__middlewares:
                request = md.before_request(self, request)
                if inspect.isawaitable(request):
                    request = await request

            response = await self.__connector.send(self.token, request)

            for md in reversed(self.__middlewares):
                response = md.after_request(self, request, response)
                if inspect.isawaitable(request):
                    response = await response

            if response.ok:
                return response
            if response.error_code == 400:
                raise RocketgramRequest400Error(request, response)
            elif response.error_code == 401:
                raise RocketgramRequest401Error(request, response)
            elif response.error_code == 429:
                raise RocketgramRequest429Error(request, response)
            raise RocketgramRequestError(request, response)
        except asyncio.CancelledError:
            raise
        except Exception as error:
            for md in reversed(self.__middlewares):
                m = md.request_error(self, request, error)
                if inspect.isawaitable(m):
                    await m
            raise

    get_updates = _make_method(GetUpdates)
    set_webhook = _make_method(SetWebhook)
    delete_webhook = _make_method(DeleteWebhook)
    get_webhook_info = _make_method(GetWebhookInfo)
    get_me = _make_method(GetMe)
    send_message = _make_method(SendMessage)
    forward_message = _make_method(ForwardMessage)
    send_photo = _make_method(SendPhoto)
    send_audio = _make_method(SendAudio)
    send_document = _make_method(SendDocument)
    send_video = _make_method(SendVideo)
    send_animation = _make_method(SendAnimation)
    send_voice = _make_method(SendVoice)
    send_video_note = _make_method(SendVideoNote)
    send_media_group = _make_method(SendMediaGroup)
    send_location = _make_method(SendLocation)
    edit_message_live_location = _make_method(EditMessageLiveLocation)
    stop_message_live_location = _make_method(StopMessageLiveLocation)
    send_venue = _make_method(SendVenue)
    send_contact = _make_method(SendContact)
    send_chat_action = _make_method(SendChatAction)
    get_user_profile_photos = _make_method(GetUserProfilePhotos)
    get_file = _make_method(GetFile)
    kick_chat_member = _make_method(KickChatMember)
    unban_chat_member = _make_method(UnbanChatMember)
    restrict_chat_member = _make_method(RestrictChatMember)
    promote_chat_member = _make_method(PromoteChatMember)
    export_chat_invite_link = _make_method(ExportChatInviteLink)
    set_chat_photo = _make_method(SetChatPhoto)
    delete_chat_photo = _make_method(DeleteChatPhoto)
    set_chat_title = _make_method(SetChatTitle)
    set_chat_description = _make_method(SetChatDescription)
    pin_chat_message = _make_method(PinChatMessage)
    unpin_chat_message = _make_method(UnpinChatMessage)
    leave_chat = _make_method(LeaveChat)
    get_chat = _make_method(GetChat)
    get_chat_administrators = _make_method(GetChatAdministrators)
    get_chat_members_count = _make_method(GetChatMembersCount)
    get_chat_member = _make_method(GetChatMember)
    set_chat_sticker_set = _make_method(SetChatStickerSet)
    delete_shat_sticker_set = _make_method(DeleteChatStickerSet)
    answer_callback_query = _make_method(AnswerCallbackQuery)
    edit_message_text = _make_method(EditMessageText)
    edit_message_caption = _make_method(EditMessageCaption)
    edit_message_media = _make_method(EditMessageMedia)
    edit_message_reply_markup = _make_method(EditMessageReplyMarkup)
    delete_message = _make_method(DeleteMessage)
    send_sticker = _make_method(SendSticker)
    get_sticker_set = _make_method(GetStickerSet)
    upload_sticker_file = _make_method(UploadStickerFile)
    create_new_sticker_set = _make_method(CreateNewStickerSet)
    add_sticker_to_set = _make_method(AddStickerToSet)
    set_sticker_position_in_set = _make_method(SetStickerPositionInSet)
    delete_sticker_from_set = _make_method(DeleteStickerFromSet)
    answer_inline_query = _make_method(AnswerInlineQuery)
    send_invoice = _make_method(SendInvoice)
    answer_shipping_query = _make_method(AnswerShippingQuery)
    answer_pre_checkout_query = _make_method(AnswerPreCheckoutQuery)
    set_passport_data_errors = _make_method(SetPassportDataErrors)
    send_game = _make_method(SendGame)
    set_game_score = _make_method(SetGameScore)
    get_game_high_scores = _make_method(GetGameHighScores)
