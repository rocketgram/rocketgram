# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


from .types import Default


class Request:
    @property
    def method(self):
        return self._method

    @property
    def data(self):
        return self._data

    def get(self, include_method=False):
        if include_method:
            d = dict(method=self.method)
            d.update(self.data)
            return d
        return self.data


class GetUpdates(Request):
    """https://core.telegram.org/bots/api#getupdates"""

    def __init__(self, offset=None, limit=None, timeout=None, allowed_updates=None):
        self._method = "getUpdates"
        self._data = dict(offset=offset, limit=limit, timeout=timeout, allowed_updates=allowed_updates)


class SetWebhook(Request):
    """https://core.telegram.org/bots/api#setwebhook"""

    def __init__(self, url, max_connections=None, allowed_updates=None):
        self._method = "setWebhook"
        self._data = dict(url=url, max_connections=max_connections, allowed_updates=allowed_updates)


class DeleteWebhook(Request):
    """https://core.telegram.org/bots/api#deletewebhook"""

    def __init__(self):
        self._method = "deleteWebhook"
        self._data = dict()


class GetWebhookInfo(Request):
    """https://core.telegram.org/bots/api#getwebhookinfo"""

    def __init__(self):
        self._method = "getWebhookInfo"
        self._data = dict()


class GetMe(Request):
    """https://core.telegram.org/bots/api#getme"""

    def __init__(self):
        self._method = "getMe"
        self._data = dict()


class SendMessage(Request):
    """https://core.telegram.org/bots/api#sendmessage"""

    def __init__(self, chat_id, text, parse_mode=Default, disable_web_page_preview=Default,
                 disable_notification=Default, reply_to_message_id=None, reply_markup=None):
        self._method = "sendMessage"
        self._data = dict(chat_id=chat_id, text=text, parse_mode=parse_mode,
                          disable_web_page_preview=disable_web_page_preview, disable_notification=disable_notification,
                          reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)


class ForwardMessage(Request):
    """https://core.telegram.org/bots/api#forwardmessage"""

    def __init__(self, chat_id, from_chat_id, message_id, disable_notification=Default):
        self._method = "forwardMessage"
        self._data = dict(chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id,
                          disable_notification=disable_notification)


class SendPhoto(Request):
    """https://core.telegram.org/bots/api#sendphoto"""

    def __init__(self, chat_id, photo, caption=None, disable_notification=Default, reply_to_message_id=None,
                 reply_markup=None):
        self._method = "sendPhoto"
        self._data = dict(chat_id=chat_id, photo=photo, caption=caption, disable_notification=disable_notification,
                          reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)


class SendAudio(Request):
    """https://core.telegram.org/bots/api#sendaudio"""

    def __init__(self, chat_id, audio, caption=None, duration=None, performer=None, title=None,
                 disable_notification=Default, reply_to_message_id=None, reply_markup=None):
        self._method = "sendAudio"
        self._data = dict(chat_id=chat_id, audio=audio, caption=caption, duration=duration, performer=performer,
                          title=title, disable_notification=disable_notification,
                          reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)


class SendDocument(Request):
    """https://core.telegram.org/bots/api#senddocument"""

    def __init__(self, chat_id, document, caption=None, disable_notification=Default, reply_to_message_id=None,
                 reply_markup=None):
        self._method = "sendDocument"
        self._data = dict(chat_id=chat_id, document=document, caption=caption,
                          disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
                          reply_markup=reply_markup)


class SendSticker(Request):
    """https://core.telegram.org/bots/api#sendsticker"""

    def __init__(self, chat_id, sticker, disable_notification=Default, reply_to_message_id=None, reply_markup=None):
        self._method = "sendSticker"
        self._data = dict(chat_id=chat_id, sticker=sticker, disable_notification=disable_notification,
                          reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)


class SendVideo(Request):
    """https://core.telegram.org/bots/api#sendvideo"""

    def __init__(self, chat_id, video, duration=None, width=None, height=None, caption=None,
                 disable_notification=Default, reply_to_message_id=None, reply_markup=None):
        self._method = "sendVideo"
        self._data = dict(chat_id=chat_id, video=video, duration=duration, width=width, height=height, caption=caption,
                          disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
                          reply_markup=reply_markup)


class SendVoice(Request):
    """https://core.telegram.org/bots/api#sendvoice"""

    def __init__(self, chat_id, voice, caption=None, duration=None, disable_notification=Default,
                 reply_to_message_id=None, reply_markup=None):
        self._method = "sendVoice"
        self._data = dict(chat_id=chat_id, voice=voice, caption=caption, duration=duration,
                          disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
                          reply_markup=reply_markup)


class SendVideoNote(Request):
    """https://core.telegram.org/bots/api#sendvideonote"""

    def __init__(self, chat_id, video_note, duration=None, length=None, disable_notification=Default,
                 reply_to_message_id=None, reply_markup=None):
        self._method = "sendVideoNote"
        self._data = dict(chat_id=chat_id, video_note=video_note, duration=duration, length=length,
                          disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
                          reply_markup=reply_markup)


class SendLocation(Request):
    """https://core.telegram.org/bots/api#sendlocation"""

    def __init__(self, chat_id, latitude, longitude, disable_notification=Default, reply_to_message_id=None,
                 reply_markup=None):
        self._method = "sendLocation"
        self._data = dict(chat_id=chat_id, latitude=latitude, longitude=longitude,
                          disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
                          reply_markup=reply_markup)


class SendVenue(Request):
    """https://core.telegram.org/bots/api#sendvenue"""

    def __init__(self, chat_id, latitude, longitude, title, address, foursquare_id=None, disable_notification=Default,
                 reply_to_message_id=None, reply_markup=None):
        self._method = "sendVenue"
        self._data = dict(chat_id=chat_id, latitude=latitude, longitude=longitude, title=title, address=address,
                          foursquare_id=foursquare_id, disable_notification=disable_notification,
                          reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)


class SendContact(Request):
    """https://core.telegram.org/bots/api#sendcontact"""

    def __init__(self, chat_id, phone_number, first_name, last_name=None, disable_notification=Default,
                 reply_to_message_id=None, reply_markup=None):
        self._method = "sendContact"
        self._data = dict(chat_id=chat_id, phone_number=phone_number, first_name=first_name, last_name=last_name,
                          disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
                          reply_markup=reply_markup)


class SendChatAction(Request):
    """https://core.telegram.org/bots/api#sendchataction"""

    def __init__(self, chat_id, action):
        self._method = "sendChatAction"
        self._data = dict(chat_id=chat_id, action=action)


class GetUserProfilePhotos(Request):
    """https://core.telegram.org/bots/api#getuserprofilephotos"""

    def __init__(self, chat_id, offset=None, limit=None):
        self._method = "getUserProfilePhotos"
        self._data = dict(chat_id=chat_id, offset=offset, limit=limit)


class GetFile(Request):
    """https://core.telegram.org/bots/api#getfile"""

    def __init__(self, file_id):
        self._method = "getFile"
        self._data = dict(file_id=file_id)


class KickChatMember(Request):
    """https://core.telegram.org/bots/api#kickchatmember"""

    def __init__(self, chat_id, user_id):
        self._method = "kickChatMember"
        self._data = dict(chat_id=chat_id, user_id=user_id)


class UnbanChatMember(Request):
    """https://core.telegram.org/bots/api#unbanchatmember"""

    def __init__(self, chat_id, user_id):
        self._method = "unbanChatMember"
        self._data = dict(chat_id=chat_id, user_id=user_id)


class LeaveChat(Request):
    """https://core.telegram.org/bots/api#leavechat"""

    def __init__(self, chat_id):
        self._method = "leaveChat"
        self._data = dict(chat_id=chat_id)


class GetChat(Request):
    """https://core.telegram.org/bots/api#getchat"""

    def __init__(self, chat_id):
        self._method = "getChat"
        self._data = dict(chat_id=chat_id)


class GetChatAdministrators(Request):
    """https://core.telegram.org/bots/api#getchatadministrators"""

    def __init__(self, chat_id):
        self._method = "getChatAdministrators"
        self._data = dict(chat_id=chat_id)


class GetChatMembersCount(Request):
    """https://core.telegram.org/bots/api#getchatmemberscount"""

    def __init__(self, chat_id):
        self._method = "getChatMembersCount"
        self._data = dict(chat_id=chat_id)


class GetChatMember(Request):
    """https://core.telegram.org/bots/api#getchatmember"""

    def __init__(self, chat_id, user_id):
        self._method = "getChatMember"
        self._data = dict(chat_id=chat_id, user_id=user_id)


class AnswerCallbackQuery(Request):
    """https://core.telegram.org/bots/api#answercallbackquery"""

    def __init__(self, callback_query_id, text=None, show_alert=None, url=None, cache_time=None):
        self._method = "answerCallbackQuery"
        self._data = dict(callback_query_id=callback_query_id, text=text, show_alert=show_alert, url=url,
                          cache_time=cache_time)


class EditMessageText(Request):
    """https://core.telegram.org/bots/api#editmessagetext"""

    def __init__(self, chat_id=None, message_id=None, inline_message_id=None, text=None, parse_mode=Default,
                 disable_web_page_preview=Default, reply_markup=None):
        self._method = "editMessageText"
        self._data = dict(chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id, text=text,
                          parse_mode=parse_mode, disable_web_page_preview=disable_web_page_preview,
                          reply_markup=reply_markup)


class EditMessageCaption(Request):
    """https://core.telegram.org/bots/api#editmessagecaption"""

    def __init__(self, chat_id=None, message_id=None, inline_message_id=None, caption=None, reply_markup=None):
        self._method = "editMessageCaption"
        self._data = dict(chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id, caption=caption,
                          reply_markup=reply_markup)


class EditMessageReplyMarkup(Request):
    """https://core.telegram.org/bots/api#editmessagereplymarkup"""

    def __init__(self, chat_id=None, message_id=None, inline_message_id=None, reply_markup=None):
        self._method = "editMessageReplyMarkup"
        self._data = dict(chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id,
                          reply_markup=reply_markup)


class DeleteMessage(Request):
    """https://core.telegram.org/bots/api#deletemessage"""

    def __init__(self, chat_id=None, message_id=None):
        self._method = "deleteMessage"
        self._data = dict(chat_id=chat_id, message_id=message_id)


class AnswerInlineQuery(Request):
    """https://core.telegram.org/bots/api#answerinlinequery"""

    def __init__(self, inline_query_id, results, cache_time=None, is_personal=None, next_offset=None,
                 switch_pm_text=None, switch_pm_parameter=None):
        self._method = "answerInlineQuery"
        self._data = dict(inline_query_id=inline_query_id, results=results, cache_time=cache_time,
                          is_personal=is_personal, next_offset=next_offset, switch_pm_text=switch_pm_text,
                          switch_pm_parameter=switch_pm_parameter)


class SendInvoice(Request):
    """https://core.telegram.org/bots/api#sendinvoice"""

    def __init__(self, chat_id, title, description, payload, provider_token, start_parameter, currency, prices,
                 photo_url=None, photo_size=None, photo_width=None, photo_height=None, need_name=None,
                 need_phone_number=None, need_email=None, need_shipping_address=None, is_flexible=None,
                 disable_notification=Default, reply_to_message_id=None, reply_markup=None):
        self._method = "sendInvoice"
        self._data = dict(chat_id=chat_id, title=title, description=description, payload=payload,
                          provider_token=provider_token, start_parameter=start_parameter, currency=currency,
                          prices=prices, photo_url=photo_url, photo_size=photo_size, photo_width=photo_width,
                          photo_height=photo_height, need_name=need_name, need_phone_number=need_phone_number,
                          need_email=need_email, need_shipping_address=need_shipping_address, is_flexible=is_flexible,
                          disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
                          reply_markup=reply_markup)


class AnswerShippingQuery(Request):
    """https://core.telegram.org/bots/api#answershippingquery"""

    def __init__(self, shipping_query_id, ok, shipping_options=None, error_message=None):
        self._method = "answerShippingQuery"
        self._data = dict(shipping_query_id=shipping_query_id, ok=ok, shipping_options=shipping_options,
                          error_message=error_message)


class AnswerPreCheckoutQuery(Request):
    """https://core.telegram.org/bots/api#answerprecheckoutquery"""

    def __init__(self, pre_checkout_query_id, ok, error_message=None):
        self._method = "answerPreCheckoutQuery"
        self._data = dict(pre_checkout_query_id=pre_checkout_query_id, ok=ok, error_message=error_message)


class SendGame(Request):
    """https://core.telegram.org/bots/api#sendgame"""

    def __init__(self, chat_id, game_short_name, disable_notification=Default, reply_to_message_id=None,
                 reply_markup=None):
        self._method = "sendGame"
        self._data = dict(chat_id=chat_id, game_short_name=game_short_name, disable_notification=disable_notification,
                          reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)


class SetGameScore(Request):
    """https://core.telegram.org/bots/api#setgamescore"""

    def __init__(self, user_id, score, force=None, disable_edit_message=None, chat_id=None, message_id=None,
                 inline_message_id=None):
        self._method = "setGameScore"
        self._data = dict(user_id=user_id, score=score, force=force, disable_edit_message=disable_edit_message,
                          chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id)


class GetGameHighScores(Request):
    """https://core.telegram.org/bots/api#getgamehighscores"""

    def __init__(self, user_id, chat_id=None, message_id=None, inline_message_id=None):
        self._method = "getGameHighScores"
        self._data = dict(user_id=user_id, chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id)
