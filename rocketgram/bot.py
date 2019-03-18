# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import json
import logging
import typing
from contextlib import suppress

from . import types, update, errors, requests
from .context import Context
from .errors import TelegramSendError
from .keyboards.keyboard import Keyboard

if typing.TYPE_CHECKING:
    from .routers import BaseRouter
    from .connectors import BaseConnector

API_URL = "https://api.telegram.org/bot%s/"
API_FILE_URL = "https://api.telegram.org/file/bot%s/"

logger = logging.getLogger('rocketgram.bot')
logger_raw_in = logging.getLogger('rocketgram.raw.in')
logger_raw_out = logging.getLogger('rocketgram.raw.out')


class Bot:
    def __init__(self, token: str, *, connector: 'BaseConnector' = None, router: 'BaseRouter' = None,
                 globals_class: typing.ClassVar = dict, context_data_class: typing.ClassVar = dict,
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

    async def init(self, getme=True):
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

    async def process(self, upd, is_webhook: bool = False) -> typing.Union[None, requests.Request]:
        try:
            if not isinstance(upd, update.Update):
                upd = update.Update(json.loads(upd))

            logger_raw_in.debug('Raw in: %s', upd.raw)

            context_data = self.__context_data_class()
            ctx = Context(self, upd, context_data)

            await self.router.process(ctx)

            webhook_request = None
            send_file = False

            whreqs = ctx.get_webhook_requests()

            # preparing webhook-request
            if len(whreqs) and is_webhook:
                req = whreqs.pop(0)
                send_file, webhook_request = self.prepare_request(req, include_method=True)

            # fallback if requests more than one
            for r in whreqs:
                with suppress(Exception):
                    await self.send(r)
            if webhook_request:
                return send_file, webhook_request

        except errors.TelegramStopRequest:
            logger.debug('TelegramStopRequest for update %s' % upd.update_id)
        except Exception:
            logger.exception('Got exception during processing request')

    async def send(self, req: requests.Request) -> update.Response:
        sending_file, data = self.prepare_request(req)

        url = self.__full_api_url + req.method

        if sending_file:
            response = await self.__connector.send_file(url, data)
        else:
            response = await self.__connector.send(url, data)

        if response.status == 200:
            return update.Response(response.data, req.method)
        else:
            r = update.Response(response.data, req.method) if response.data else None
            if r:
                logger.debug("Error from telegram: %s '%s'", response.status, r.description)
                raise TelegramSendError(req.method, req, response.status, r)
            else:
                logger.debug("Error from telegram: %s", response.status)
                raise TelegramSendError(req.method, req, response.status, None)

    def prepare_request(self, req: requests.Request, include_method=False):
        request_data = req.get(include_method=include_method)

        if request_data.get('parse_mode') is types.Default:
            request_data['parse_mode'] = self.parse_mode
        if request_data.get('disable_notification') is types.Default:
            request_data['disable_notification'] = self.disable_notification
        if request_data.get('disable_web_page_preview') is types.Default:
            request_data['disable_web_page_preview'] = self.disable_web_page_preview

        if isinstance(request_data.get('reply_markup'), Keyboard):
            request_data['reply_markup'] = request_data['reply_markup'].render()

        sending_file = False
        data = dict()
        for k, v in request_data.items():
            if v is not None:
                data[k] = v
            if isinstance(v, types.InputFile):
                sending_file = True

        return sending_file, data

    def get_updates(self, offset=None, limit=None, timeout=None, allowed_updates=None):
        """https://core.telegram.org/bots/api#getupdates"""

        return self.send(
            requests.GetUpdates(offset=offset, limit=limit, timeout=timeout, allowed_updates=allowed_updates))

    def set_webhook(self, url, max_connections=None, allowed_updates=None):
        """https://core.telegram.org/bots/api#setwebhook"""
        return self.send(requests.SetWebhook(url=url, max_connections=max_connections, allowed_updates=allowed_updates))

    def delete_webhook(self):
        """https://core.telegram.org/bots/api#deletewebhook"""
        return self.send(requests.DeleteWebhook())

    def get_webhook_info(self):
        """https://core.telegram.org/bots/api#getwebhookinfo"""
        return self.send(requests.GetWebhookInfo())

    def get_me(self):
        """https://core.telegram.org/bots/api#getme"""
        return self.send(requests.GetMe())

    def send_message(self, chat_id, text, parse_mode=types.Default, disable_web_page_preview=types.Default,
                     disable_notification=types.Default, reply_to_message_id=None, reply_markup=None):
        """https://core.telegram.org/bots/api#sendmessage"""
        return self.send(requests.SendMessage(chat_id=chat_id, text=text, parse_mode=parse_mode,
                                              disable_web_page_preview=disable_web_page_preview,
                                              disable_notification=disable_notification,
                                              reply_to_message_id=reply_to_message_id, reply_markup=reply_markup))

    def forward_message(self, chat_id, from_chat_id, message_id, disable_notification=types.Default):
        """https://core.telegram.org/bots/api#forwardmessage"""
        return self.send(requests.ForwardMessage(chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id,
                                                 disable_notification=disable_notification))

    def send_photo(self, chat_id, photo, caption=None, disable_notification=types.Default, reply_to_message_id=None,
                   reply_markup=None):
        """https://core.telegram.org/bots/api#sendphoto"""
        return self.send(
            requests.SendPhoto(chat_id=chat_id, photo=photo, caption=caption, disable_notification=disable_notification,
                               reply_to_message_id=reply_to_message_id, reply_markup=reply_markup))

    def send_audio(self, chat_id, audio, caption=None, duration=None, performer=None, title=None,
                   disable_notification=types.Default, reply_to_message_id=None, reply_markup=None):
        """https://core.telegram.org/bots/api#sendaudio"""
        return self.send(
            requests.SendAudio(chat_id=chat_id, audio=audio, caption=caption, duration=duration, performer=performer,
                               title=title, disable_notification=disable_notification,
                               reply_to_message_id=reply_to_message_id, reply_markup=reply_markup))

    def send_document(self, chat_id, document, caption=None, disable_notification=types.Default,
                      reply_to_message_id=None, reply_markup=None):
        """https://core.telegram.org/bots/api#senddocument"""
        return self.send(requests.SendDocument(chat_id=chat_id, document=document, caption=caption,
                                               disable_notification=disable_notification,
                                               reply_to_message_id=reply_to_message_id, reply_markup=reply_markup))

    def send_animation(self, chat_id, animation, duration=None, width=None, height=None, caption=None,
                       thumb=None, disable_notification=types.Default, reply_to_message_id=None, reply_markup=None):
        """https://core.telegram.org/bots/api#sendvideo"""
        return self.send(
            requests.SendAnimation(chat_id=chat_id, animation=animation, duration=duration, width=width, height=height,
                                   thumb=thumb, caption=caption, disable_notification=disable_notification,
                                   reply_to_message_id=reply_to_message_id, reply_markup=reply_markup))

    def send_sticker(self, chat_id, sticker, disable_notification=types.Default, reply_to_message_id=None,
                     reply_markup=None):
        """https://core.telegram.org/bots/api#sendsticker"""
        return self.send(
            requests.SendSticker(chat_id=chat_id, sticker=sticker, disable_notification=disable_notification,
                                 reply_to_message_id=reply_to_message_id, reply_markup=reply_markup))

    def send_video(self, chat_id, video, duration=None, width=None, height=None, caption=None,
                   disable_notification=types.Default, reply_to_message_id=None, reply_markup=None):
        """https://core.telegram.org/bots/api#sendvideo"""
        return self.send(requests.SendVideo(chat_id=chat_id, video=video, duration=duration, width=width, height=height,
                                            caption=caption, disable_notification=disable_notification,
                                            reply_to_message_id=reply_to_message_id, reply_markup=reply_markup))

    def send_voice(self, chat_id, voice, caption=None, duration=None, disable_notification=types.Default,
                   reply_to_message_id=None, reply_markup=None):
        """https://core.telegram.org/bots/api#sendvoice"""
        return self.send(requests.SendVoice(chat_id=chat_id, voice=voice, caption=caption, duration=duration,
                                            disable_notification=disable_notification,
                                            reply_to_message_id=reply_to_message_id, reply_markup=reply_markup))

    def send_video_note(self, chat_id, video_note, duration=None, length=None, disable_notification=types.Default,
                        reply_to_message_id=None, reply_markup=None):
        """https://core.telegram.org/bots/api#sendvideonote"""
        return self.send(
            requests.SendVideoNote(chat_id=chat_id, video_note=video_note, duration=duration, length=length,
                                   disable_notification=disable_notification,
                                   reply_to_message_id=reply_to_message_id, reply_markup=reply_markup))

    def send_location(self, chat_id, latitude, longitude, disable_notification=types.Default, reply_to_message_id=None,
                      reply_markup=None):
        """https://core.telegram.org/bots/api#sendlocation"""
        return self.send(requests.SendLocation(chat_id=chat_id, latitude=latitude, longitude=longitude,
                                               disable_notification=disable_notification,
                                               reply_to_message_id=reply_to_message_id, reply_markup=reply_markup))

    def send_venue(self, chat_id, latitude, longitude, title, address, foursquare_id=None,
                   disable_notification=types.Default, reply_to_message_id=None, reply_markup=None):
        """https://core.telegram.org/bots/api#sendvenue"""
        return self.send(
            requests.SendVenue(chat_id=chat_id, latitude=latitude, longitude=longitude, title=title, address=address,
                               foursquare_id=foursquare_id, disable_notification=disable_notification,
                               reply_to_message_id=reply_to_message_id, reply_markup=reply_markup))

    def send_contact(self, chat_id, phone_number, first_name, last_name=None, disable_notification=types.Default,
                     reply_to_message_id=None, reply_markup=None):
        """https://core.telegram.org/bots/api#sendcontact"""
        return self.send(
            requests.SendContact(chat_id=chat_id, phone_number=phone_number, first_name=first_name, last_name=last_name,
                                 disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
                                 reply_markup=reply_markup))

    def send_chat_action(self, chat_id, action):
        """https://core.telegram.org/bots/api#sendchataction"""
        return self.send(requests.SendChatAction(chat_id=chat_id, action=action))

    def get_user_profile_photos(self, chat_id, offset=None, limit=None):
        """https://core.telegram.org/bots/api#getuserprofilephotos"""
        return self.send(requests.GetUserProfilePhotos(chat_id=chat_id, offset=offset, limit=limit))

    def get_file(self, file_id):
        """https://core.telegram.org/bots/api#getfile"""
        return self.send(requests.GetFile(file_id=file_id))

    def kick_chat_member(self, chat_id, user_id):
        """https://core.telegram.org/bots/api#kickchatmember"""
        return self.send(requests.KickChatMember(chat_id=chat_id, user_id=user_id))

    def unban_chat_member(self, chat_id, user_id):
        """https://core.telegram.org/bots/api#unbanchatmember"""
        return self.send(requests.UnbanChatMember(chat_id=chat_id, user_id=user_id))

    def leave_chat(self, chat_id):
        """https://core.telegram.org/bots/api#leavechat"""
        return self.send(requests.LeaveChat(chat_id=chat_id))

    def get_chat(self, chat_id):
        """https://core.telegram.org/bots/api#getchat"""
        return self.send(requests.GetChat(chat_id=chat_id))

    def get_chat_administrators(self, chat_id):
        """https://core.telegram.org/bots/api#getchatadministrators"""
        return self.send(requests.GetChatAdministrators(chat_id=chat_id))

    def get_chat_members_count(self, chat_id):
        """https://core.telegram.org/bots/api#getchatmemberscount"""
        return self.send(requests.GetChatMembersCount(chat_id=chat_id))

    def get_chat_member(self, chat_id, user_id):
        """https://core.telegram.org/bots/api#getchatmember"""
        return self.send(requests.GetChatMember(chat_id=chat_id, user_id=user_id))

    def answer_callback_query(self, callback_query_id, text=None, show_alert=None, url=None, cache_time=None):
        """https://core.telegram.org/bots/api#answercallbackquery"""
        return self.send(
            requests.AnswerCallbackQuery(callback_query_id=callback_query_id, text=text, show_alert=show_alert, url=url,
                                         cache_time=cache_time))

    def edit_message_text(self, chat_id=None, message_id=None, inline_message_id=None, text=None,
                          parse_mode=types.Default, disable_web_page_preview=types.Default, reply_markup=None):
        """https://core.telegram.org/bots/api#editmessagetext"""
        return self.send(
            requests.EditMessageText(chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id,
                                     text=text, parse_mode=parse_mode,
                                     disable_web_page_preview=disable_web_page_preview,
                                     reply_markup=reply_markup))

    def edit_message_caption(self, chat_id=None, message_id=None, inline_message_id=None, caption=None,
                             reply_markup=None):
        """https://core.telegram.org/bots/api#editmessagecaption"""
        return self.send(
            requests.EditMessageCaption(chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id,
                                        caption=caption, reply_markup=reply_markup))

    def edit_message_reply_markup(self, chat_id=None, message_id=None, inline_message_id=None, reply_markup=None):
        """https://core.telegram.org/bots/api#editmessagereplymarkup"""
        return self.send(
            requests.EditMessageReplyMarkup(chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id,
                                            reply_markup=reply_markup))

    def delete_message(self, chat_id=None, message_id=None):
        """https://core.telegram.org/bots/api#deletemessage"""
        return self.send(requests.DeleteMessage(chat_id=chat_id, message_id=message_id))

    def answer_inline_query(self, inline_query_id, results, cache_time=None, is_personal=None, next_offset=None,
                            switch_pm_text=None, switch_pm_parameter=None):
        """https://core.telegram.org/bots/api#answerinlinequery"""
        return self.send(
            requests.AnswerInlineQuery(inline_query_id=inline_query_id, results=results, cache_time=cache_time,
                                       is_personal=is_personal, next_offset=next_offset, switch_pm_text=switch_pm_text,
                                       switch_pm_parameter=switch_pm_parameter))

    def send_invoice(self, chat_id, title, description, payload, provider_token, start_parameter, currency, prices,
                     photo_url=None, photo_size=None, photo_width=None, photo_height=None, need_name=None,
                     need_phone_number=None, need_email=None, need_shipping_address=None, is_flexible=None,
                     disable_notification=types.Default, reply_to_message_id=None, reply_markup=None):
        """https://core.telegram.org/bots/api#sendinvoice"""
        return self.send(requests.SendInvoice(chat_id=chat_id, title=title, description=description, payload=payload,
                                              provider_token=provider_token, start_parameter=start_parameter,
                                              currency=currency, prices=prices, photo_url=photo_url,
                                              photo_size=photo_size, photo_width=photo_width, photo_height=photo_height,
                                              need_name=need_name, need_phone_number=need_phone_number,
                                              need_email=need_email, need_shipping_address=need_shipping_address,
                                              is_flexible=is_flexible, disable_notification=disable_notification,
                                              reply_to_message_id=reply_to_message_id, reply_markup=reply_markup))

    def answer_shipping_query(self, shipping_query_id, ok, shipping_options=None, error_message=None):
        """https://core.telegram.org/bots/api#answershippingquery"""
        return self.send(
            requests.AnswerShippingQuery(shipping_query_id=shipping_query_id, ok=ok, shipping_options=shipping_options,
                                         error_message=error_message))

    def answer_pre_checkout_query(self, pre_checkout_query_id, ok, error_message=None):
        """https://core.telegram.org/bots/api#answerprecheckoutquery"""
        return self.send(requests.AnswerPreCheckoutQuery(pre_checkout_query_id=pre_checkout_query_id, ok=ok,
                                                         error_message=error_message))

    def send_game(self, chat_id, game_short_name, disable_notification=types.Default, reply_to_message_id=None,
                  reply_markup=None):
        """https://core.telegram.org/bots/api#sendgame"""
        return self.send(requests.SendGame(chat_id=chat_id, game_short_name=game_short_name,
                                           disable_notification=disable_notification,
                                           reply_to_message_id=reply_to_message_id, reply_markup=reply_markup))

    def set_game_score(self, user_id, score, force=None, disable_edit_message=None, chat_id=None, message_id=None,
                       inline_message_id=None):
        """https://core.telegram.org/bots/api#setgamescore"""
        return self.send(
            requests.SetGameScore(user_id=user_id, score=score, force=force, disable_edit_message=disable_edit_message,
                                  chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id))

    def get_game_high_scores(self, user_id, chat_id=None, message_id=None, inline_message_id=None):
        """https://core.telegram.org/bots/api#getgamehighscores"""
        return self.send(requests.GetGameHighScores(user_id=user_id, chat_id=chat_id, message_id=message_id,
                                                    inline_message_id=inline_message_id))
