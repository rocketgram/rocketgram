# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).

from dataclasses import dataclass, asdict, field
from datetime import datetime
from enum import auto
from typing import TYPE_CHECKING, Union, Dict, Optional, List

from .types import InputFile, Enum, EnumAutoName

if TYPE_CHECKING:
    from .update import UpdateType, ShippingOption


class ParseModeType(EnumAutoName):
    """\
    Formatting options type:
    https://core.telegram.org/bots/api#formatting-options
    """

    html = auto()
    markdown = auto()


class ChatActionType(EnumAutoName):
    """\
    Formatting options type:
    https://core.telegram.org/bots/api#formatting-options
    """

    typing = auto()
    upload_photo = auto()
    record_video = auto()
    upload_video = auto()
    record_audio = auto()
    upload_audio = auto()
    upload_document = auto()
    find_location = auto()
    record_video_note = auto()
    upload_video_note = auto()


@dataclass(frozen=True)
class MaskPosition:
    """\
    Represents MaskPosition object:
    https://core.telegram.org/bots/api#maskposition
    """
    point: str
    x_shift: float
    y_shift: float
    scale: float


@dataclass(frozen=True)
class KeyboardButton:
    """\
    Represents KeyboardButton keyboard object:
    https://core.telegram.org/bots/api#keyboardbutton
    """

    text: str
    request_contact: Optional[bool] = None
    request_location: Optional[bool] = None


@dataclass(frozen=True)
class InlineKeyboardButton:
    """\
    Represents InlineKeyboardButton keyboard object:
    https://core.telegram.org/bots/api#inlinekeyboardbutton
    """

    text: str
    url: Optional[str] = None
    callback_data: Optional[str] = None
    switch_inline_query: Optional[str] = None
    switch_inline_query_current_chat: Optional[str] = None
    callback_game: Optional[dict] = None  # TODO: CallbackGame
    pay: Optional[bool] = None


@dataclass(frozen=True)
class ReplyKeyboardMarkup:
    """\
    Represents ReplyKeyboardMarkup keyboard object:
    https://core.telegram.org/bots/api#replykeyboardmarkup
    """

    keyboard: List[List[KeyboardButton]]
    resize_keyboard: Optional[bool] = None
    one_time_keyboard: Optional[bool] = None
    selective: Optional[bool] = None


@dataclass(frozen=True)
class InlineKeyboardMarkup:
    """\
    Represents InlineKeyboardMarkup keyboard object:
    https://core.telegram.org/bots/api#inlinekeyboardmarkup
    """

    inline_keyboard: List[List[InlineKeyboardButton]]


@dataclass(frozen=True)
class ReplyKeyboardRemove:
    """\
    Represents ReplyKeyboardRemove keyboard object:
    https://core.telegram.org/bots/api#replykeyboardremove
    """

    selective: bool = False
    remove_keyboard: bool = True


@dataclass(frozen=True)
class ForceReply:
    """\
    Represents ForceReply keyboard object:
    https://core.telegram.org/bots/api#forcereply
    """

    selective: bool = False
    force_reply: bool = True


@dataclass(frozen=True)
class Request:
    """\
    Base class for all request objects.
    """
    method = None

    def __prepare(self, d: Union[Dict, list]) -> Union[Dict, list]:
        assert isinstance(d, (list, dict))

        for k, v in d.items() if isinstance(d, dict) else enumerate(d):
            if isinstance(v, Enum):
                d[k] = v.value
                continue
            if isinstance(v, datetime):
                d[k] = int(v.timestamp())
                continue
            if isinstance(v, InputFile):
                d[k] = 'attach://%s' % v.file_name
                continue
            if isinstance(v, (list, dict)):
                d[k] = self.__prepare(v)

        if isinstance(d, dict):
            return {k: v for k, v in d.items() if v is not None}
        return [v for v in d if v is not None]

    def render(self, with_method=False) -> dict:
        d = asdict(self)

        assert 'method' not in d

        if with_method:
            d['method'] = self.method

        return self.__prepare(d)

    def files(self) -> List[InputFile]:
        return list()


@dataclass(frozen=True)
class GetUpdates(Request):
    """\
    Represents GetUpdates request object:
    https://core.telegram.org/bots/api#getupdates
    """

    method = "getUpdates"

    offset: Optional[int] = None
    limit: Optional[int] = None
    timeout: Optional[int] = None
    allowed_updates: Optional[List['UpdateType']] = None


@dataclass(frozen=True)
class SetWebhook(Request):
    """\
    Represents SetWebhook request object:
    https://core.telegram.org/bots/api#setwebhook
    """

    method = "setWebhook"

    url: str
    certificate: Optional[Union[InputFile, str]] = None
    max_connections: Optional[int] = None
    allowed_updates: Optional[List['UpdateType']] = None

    def files(self) -> List[InputFile]:
        if isinstance(self.certificate, InputFile):
            return [self.certificate]
        return list()


@dataclass(frozen=True)
class DeleteWebhook(Request):
    """\
    Represents DeleteWebhook request object:
    https://core.telegram.org/bots/api#deletewebhook
    """

    method = "deleteWebhook"


@dataclass(frozen=True)
class GetWebhookInfo(Request):
    """\
    Represents GetWebhookInfo request object:
    https://core.telegram.org/bots/api#getwebhookinfo
    """

    method = "getWebhookInfo"


@dataclass(frozen=True)
class GetMe(Request):
    """\
    Represents GetMe request object:
    https://core.telegram.org/bots/api#getme
    """

    method = "getMe"


@dataclass(frozen=True)
class SendMessage(Request):
    """\
    Represents SendMessage request object:
    https://core.telegram.org/bots/api#sendmessage
    """

    method = "sendMessage"

    chat_id: Union[int, str]
    text: str
    parse_mode: Optional[ParseModeType] = None
    disable_web_page_preview: Optional[bool] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[
        Union['InlineKeyboardMarkup', 'ReplyKeyboardMarkup', 'ReplyKeyboardRemove', 'ForceReply']] = None


@dataclass(frozen=True)
class ForwardMessage(Request):
    """\
    Represents ForwardMessage request object:
    https://core.telegram.org/bots/api#forwardmessage
    """

    method = "forwardMessage"

    chat_id: Union[int, str]
    from_chat_id: Union[int, str]
    message_id: int
    disable_notification: Optional[bool] = None


@dataclass(frozen=True)
class SendPhoto(Request):
    """\
    Represents SendPhoto request object:
    https://core.telegram.org/bots/api#sendphoto
    """

    method = "sendPhoto"

    chat_id: Union[int, str]
    photo: Union[InputFile, str]
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[
        Union['InlineKeyboardMarkup', 'ReplyKeyboardMarkup', 'ReplyKeyboardRemove', 'ForceReply']] = None

    def files(self) -> List[InputFile]:
        if isinstance(self.photo, InputFile):
            return [self.photo]
        return list()


@dataclass(frozen=True)
class SendAudio(Request):
    """\
    Represents SendAudio request object:
    https://core.telegram.org/bots/api#sendaudio
    """

    method = "sendAudio"

    chat_id: Union[int, str]
    audio: Union[InputFile, str]
    duration: Optional[int] = None
    performer: Optional[str] = None
    title: Optional[str] = None
    thumb: Optional[Union[InputFile, str]] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[
        Union['InlineKeyboardMarkup', 'ReplyKeyboardMarkup', 'ReplyKeyboardRemove', 'ForceReply']] = None

    def files(self) -> List[InputFile]:
        l = list()
        if isinstance(self.audio, InputFile):
            l.append(self.audio)
        if isinstance(self.thumb, InputFile):
            l.append(self.thumb)
        return l


@dataclass(frozen=True)
class SendDocument(Request):
    """\
    Represents SendDocument request object:
    https://core.telegram.org/bots/api#senddocument
    """

    method = "sendDocument"

    chat_id: Union[int, str]
    document: Union[InputFile, str]
    thumb: Optional[Union[InputFile, str]] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[
        Union['InlineKeyboardMarkup', 'ReplyKeyboardMarkup', 'ReplyKeyboardRemove', 'ForceReply']] = None

    def files(self) -> List[InputFile]:
        l = list()
        if isinstance(self.document, InputFile):
            l.append(self.document)
        if isinstance(self.thumb, InputFile):
            l.append(self.thumb)
        return l


@dataclass(frozen=True)
class SendVideo(Request):
    """\
    Represents SendVideo request object:
    https://core.telegram.org/bots/api#sendvideo
    """

    method = "sendVideo"

    chat_id: Union[int, str]
    video: Union[InputFile, str]
    duration: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    supports_streaming: Optional[bool] = None
    thumb: Optional[Union[InputFile, str]] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[
        Union['InlineKeyboardMarkup', 'ReplyKeyboardMarkup', 'ReplyKeyboardRemove', 'ForceReply']] = None

    def files(self) -> List[InputFile]:
        l = list()
        if isinstance(self.video, InputFile):
            l.append(self.video)
        if isinstance(self.thumb, InputFile):
            l.append(self.thumb)
        return l


@dataclass(frozen=True)
class SendAnimation(Request):
    """\
    Represents SendAnimation request object:
    https://core.telegram.org/bots/api#sendanimation
    """

    method = "sendAnimation"

    chat_id: Union[int, str]
    animation: Union[InputFile, str]
    duration: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    thumb: Optional[Union[InputFile, str]] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[
        Union['InlineKeyboardMarkup', 'ReplyKeyboardMarkup', 'ReplyKeyboardRemove', 'ForceReply']] = None

    def files(self) -> List[InputFile]:
        l = list()
        if isinstance(self.animation, InputFile):
            l.append(self.animation)
        if isinstance(self.thumb, InputFile):
            l.append(self.thumb)
        return l


@dataclass(frozen=True)
class SendVoice(Request):
    """\
    Represents SendVoice request object:
    https://core.telegram.org/bots/api#sendvoice
    """

    method = "sendVoice"

    chat_id: Union[int, str]
    voice: Union[InputFile, str]
    duration: Optional[int] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[
        Union['InlineKeyboardMarkup', 'ReplyKeyboardMarkup', 'ReplyKeyboardRemove', 'ForceReply']] = None

    def files(self) -> List[InputFile]:
        if isinstance(self.voice, InputFile):
            return [self.voice]
        return list()


@dataclass(frozen=True)
class SendVideoNote(Request):
    """\
    Represents SendVideoNote request object:
    https://core.telegram.org/bots/api#sendvideonote
    """

    method = "sendVideoNote"

    chat_id: Union[int, str]
    video_note: Union[InputFile, str]
    duration: Optional[int] = None
    length: Optional[int] = None
    thumb: Union[InputFile, str] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[
        Union['InlineKeyboardMarkup', 'ReplyKeyboardMarkup', 'ReplyKeyboardRemove', 'ForceReply']] = None

    def files(self) -> List[InputFile]:
        l = list()
        if isinstance(self.video_note, InputFile):
            l.append(self.video_note)
        if isinstance(self.thumb, InputFile):
            l.append(self.thumb)
        return l


@dataclass(frozen=True)
class SendMediaGroup(Request):
    """\
    Represents SendMediaGroup request object:
    https://core.telegram.org/bots/api#sendmediagroup
    """

    method = "sendMediaGroup"

    chat_id: Union[int, str]
    media: List[str]  # TODO: need types for MediaGropus
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None


@dataclass(frozen=True)
class SendLocation(Request):
    """\
    Represents SendLocation request object:
    https://core.telegram.org/bots/api#sendlocation
    """

    method = "sendLocation"

    chat_id: Union[int, str]
    latitude: float
    longitude: float
    live_period: Optional[int] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[
        Union['InlineKeyboardMarkup', 'ReplyKeyboardMarkup', 'ReplyKeyboardRemove', 'ForceReply']] = None


@dataclass(frozen=True)
class EditMessageLiveLocation(Request):
    """\
    Represents EditMessageLiveLocation request object:
    https://core.telegram.org/bots/api#editmessagelivelocation
    """

    method = "editMessageLiveLocation"

    latitude: float
    longitude: float
    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
    reply_markup: Optional[Union['InlineKeyboardMarkup']] = None


@dataclass(frozen=True)
class StopMessageLiveLocation(Request):
    """\
    Represents StopMessageLiveLocation request object:
    https://core.telegram.org/bots/api#stopmessagelivelocation
    """

    method = "stopMessageLiveLocation"

    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
    reply_markup: Optional[Union['InlineKeyboardMarkup']] = None


@dataclass(frozen=True)
class SendVenue(Request):
    """\
    Represents SendVenue request object:
    https://core.telegram.org/bots/api#sendvenue
    """

    method = "sendVenue"

    chat_id: Union[int, str]
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[
        Union['InlineKeyboardMarkup', 'ReplyKeyboardMarkup', 'ReplyKeyboardRemove', 'ForceReply']] = None


@dataclass(frozen=True)
class SendContact(Request):
    """\
    Represents SendContact request object:
    https://core.telegram.org/bots/api#sendcontact
    """

    method = "sendContact"

    chat_id: Union[int, str]
    phone_number: str
    first_name: str
    last_name: Optional[str] = None
    vcard: Optional[str] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[
        Union['InlineKeyboardMarkup', 'ReplyKeyboardMarkup', 'ReplyKeyboardRemove', 'ForceReply']] = None


@dataclass(frozen=True)
class SendPoll(Request):
    """\
    Represents SendPoll request object:
    https://core.telegram.org/bots/api#sendpoll
    """

    method = "sendPoll"

    chat_id: Union[int, str]
    question: str
    options: List[str]
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[
        Union['InlineKeyboardMarkup', 'ReplyKeyboardMarkup', 'ReplyKeyboardRemove', 'ForceReply']] = None


@dataclass(frozen=True)
class SendChatAction(Request):
    """\
    Represents SendChatAction request object:
    https://core.telegram.org/bots/api#sendchataction
    """

    method = "sendChatAction"

    chat_id: Union[int, str]
    action: ChatActionType


@dataclass(frozen=True)
class GetUserProfilePhotos(Request):
    """\
    Represents GetUserProfilePhotos request object:
    https://core.telegram.org/bots/api#getuserprofilephotos
    """

    method = "getUserProfilePhotos"

    user_id: int
    offset: Optional[int] = None
    limit: Optional[int] = None


@dataclass(frozen=True)
class GetFile(Request):
    """\
    Represents GetFile request object:
    https://core.telegram.org/bots/api#getfile
    """

    method = "getFile"

    file_id: str


@dataclass(frozen=True)
class KickChatMember(Request):
    """\
    Represents KickChatMember request object:
    https://core.telegram.org/bots/api#kickchatmember
    """

    method = "kickChatMember"

    chat_id: Union[int, str]
    user_id: int
    until_date: Optional[datetime] = None


@dataclass(frozen=True)
class UnbanChatMember(Request):
    """\
    Represents UnbanChatMember request object:
    https://core.telegram.org/bots/api#unbanchatmember
    """

    method = "unbanChatMember"

    chat_id: Union[int, str]
    user_id: int
    until_date: Optional[datetime] = None


@dataclass(frozen=True)
class RestrictChatMember(Request):
    """\
    Represents RestrictChatMember request object:
    https://core.telegram.org/bots/api#restrictchatmember
    """

    method = "restrictChatMember"

    chat_id: Union[int, str]
    user_id: int
    until_date: Optional[datetime] = None
    can_send_messages: Optional[bool] = None
    can_send_media_messages: Optional[bool] = None
    can_send_other_messages: Optional[bool] = None
    can_add_web_page_previews: Optional[bool] = None


@dataclass(frozen=True)
class PromoteChatMember(Request):
    """\
    Represents PromoteChatMember request object:
    https://core.telegram.org/bots/api#promotechatmember
    """

    method = "promoteChatMember"

    chat_id: Union[int, str]
    user_id: int
    can_change_info: Optional[bool] = None
    can_post_messages: Optional[bool] = None
    can_edit_messages: Optional[bool] = None
    can_delete_messages: Optional[bool] = None
    can_invite_users: Optional[bool] = None
    can_restrict_members: Optional[bool] = None
    can_pin_messages: Optional[bool] = None
    can_promote_members: Optional[bool] = None


@dataclass(frozen=True)
class ExportChatInviteLink(Request):
    """\
    Represents ExportChatInviteLink request object:
    https://core.telegram.org/bots/api#exportchatinvitelink
    """

    method = "exportChatInviteLink"

    chat_id: Union[int, str]


@dataclass(frozen=True)
class SetChatPhoto(Request):
    """\
    Represents SetChatPhoto request object:
    https://core.telegram.org/bots/api#setchatphoto
    """

    method = "setChatPhoto"

    chat_id: Union[int, str]
    photo: Union[InputFile, str]

    def files(self) -> List[InputFile]:
        if isinstance(self.photo, InputFile):
            return [self.photo]
        return list()


@dataclass(frozen=True)
class DeleteChatPhoto(Request):
    """\
    Represents DeleteChatPhoto request object:
    https://core.telegram.org/bots/api#deletechatphoto
    """

    method = "deleteChatPhoto"

    chat_id: Union[int, str]


@dataclass(frozen=True)
class SetChatTitle(Request):
    """\
    Represents SetChatTitle request object:
    https://core.telegram.org/bots/api#setchattitle
    """

    method = "setChatTitle"

    chat_id: Union[int, str]
    title: str


@dataclass(frozen=True)
class SetChatDescription(Request):
    """\
    Represents SetChatDescription request object:
    https://core.telegram.org/bots/api#setchatdescription
    """

    method = "setChatDescription"

    chat_id: Union[int, str]
    description: Optional[str]


@dataclass(frozen=True)
class PinChatMessage(Request):
    """\
    Represents PinChatMessage request object:
    https://core.telegram.org/bots/api#pinchatmessage
    """

    method = "pinChatMessage"

    chat_id: Union[int, str]
    message_id: int
    disable_notification: Optional[bool] = None


@dataclass(frozen=True)
class UnpinChatMessage(Request):
    """\
    Represents UnpinChatMessage request object:
    https://core.telegram.org/bots/api#unpinchatmessage
    """

    method = "unpinChatMessage"

    chat_id: Union[int, str]


@dataclass(frozen=True)
class LeaveChat(Request):
    """\
    Represents LeaveChat request object:
    https://core.telegram.org/bots/api#leavechat
    """

    method = "leaveChat"

    chat_id: Union[int, str]


@dataclass(frozen=True)
class GetChat(Request):
    """\
    Represents GetChat request object:
    https://core.telegram.org/bots/api#getchat
    """

    method = "getChat"

    chat_id: Union[int, str]


@dataclass(frozen=True)
class GetChatAdministrators(Request):
    """\
    Represents GetChatAdministrators request object:
    https://core.telegram.org/bots/api#getchatadministrators
    """

    method = "getChatAdministrators"

    chat_id: Union[int, str]


@dataclass(frozen=True)
class GetChatMembersCount(Request):
    """\
    Represents GetChatMembersCount request object:
    https://core.telegram.org/bots/api#getchatmemberscount
    """

    method = "getChatMembersCount"

    chat_id: Union[int, str]


@dataclass(frozen=True)
class GetChatMember(Request):
    """\
    Represents GetChatMember request object:
    https://core.telegram.org/bots/api#getchatmember
    """

    method = "getChatMember"

    chat_id: Union[int, str]
    user_id: int


@dataclass(frozen=True)
class SetChatStickerSet(Request):
    """\
    Represents SetChatStickerSet request object:
    https://core.telegram.org/bots/api#setchatstickerset
    """

    method = "setChatStickerSet"

    chat_id: Union[int, str]
    sticker_set_name: str


@dataclass(frozen=True)
class DeleteChatStickerSet(Request):
    """\
    Represents DeleteChatStickerSet request object:
    https://core.telegram.org/bots/api#deletechatstickerset
    """

    method = "deleteChatStickerSet"

    chat_id: Union[int, str]
    sticker_set_name: str


@dataclass(frozen=True)
class AnswerCallbackQuery(Request):
    """\
    Represents AnswerCallbackQuery request object:
    https://core.telegram.org/bots/api#answercallbackquery
    """

    method = "answerCallbackQuery"

    callback_query_id: str
    text: Optional[str] = None
    show_alert: Optional[bool] = None
    url: Optional[str] = None
    cache_time: Optional[int] = None


@dataclass(frozen=True)
class EditMessageText(Request):
    """\
    Represents EditMessageText request object:
    https://core.telegram.org/bots/api#editmessagetext
    """

    method = "editMessageText"

    text: str
    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    disable_web_page_preview: Optional[bool] = None
    reply_markup: Optional[Union['InlineKeyboardMarkup']] = None


@dataclass(frozen=True)
class EditMessageCaption(Request):
    """\
    Represents EditMessageCaption request object:
    https://core.telegram.org/bots/api#editmessagecaption
    """

    method = "editMessageCaption"

    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    disable_web_page_preview: Optional[bool] = None
    reply_markup: Optional[Union['InlineKeyboardMarkup']] = None


@dataclass(frozen=True)
class EditMessageMedia(Request):
    """\
    Represents EditMessageMedia request object:
    https://core.telegram.org/bots/api#editmessagemedia
    """

    method = "editMessageMedia"

    media: str  # TODO: need types for MediaGropus
    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
    disable_web_page_preview: Optional[bool] = None
    reply_markup: Optional[Union['InlineKeyboardMarkup']] = None


@dataclass(frozen=True)
class EditMessageReplyMarkup(Request):
    """\
    Represents EditMessageReplyMarkup request object:
    https://core.telegram.org/bots/api#editmessagereplymarkup
    """

    method = "editMessageReplyMarkup"

    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
    disable_web_page_preview: Optional[bool] = None
    reply_markup: Optional[Union['InlineKeyboardMarkup']] = None


@dataclass(frozen=True)
class StopPoll(Request):
    """\
    Represents StopPoll request object:
    https://core.telegram.org/bots/api#stoppoll
    """

    method = "stopPoll"

    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    reply_markup: Optional[Union['InlineKeyboardMarkup']] = None


@dataclass(frozen=True)
class DeleteMessage(Request):
    """\
    Represents DeleteMessage request object:
    https://core.telegram.org/bots/api#deletemessage
    """

    method = "deleteMessage"

    chat_id: Union[int, str] = None
    message_id: int = None


@dataclass(frozen=True)
class SendSticker(Request):
    """\
    Represents SendSticker request object:
    https://core.telegram.org/bots/api#sendsticker
    """

    method = "sendSticker"

    chat_id: Union[int, str]
    sticker: Union[InputFile, str]
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[
        Union['InlineKeyboardMarkup', 'ReplyKeyboardMarkup', 'ReplyKeyboardRemove', 'ForceReply']] = None

    def files(self) -> List[InputFile]:
        if isinstance(self.sticker, InputFile):
            return [self.sticker]
        return list()


@dataclass(frozen=True)
class GetStickerSet(Request):
    """\
    Represents GetStickerSet request object:
    https://core.telegram.org/bots/api#getstickerset
    """

    method = "getStickerSet"

    name: str


@dataclass(frozen=True)
class UploadStickerFile(Request):
    """\
    Represents UploadStickerFile request object:
    https://core.telegram.org/bots/api#uploadstickerfile
    """

    method = "uploadStickerFile"

    user_id: int
    png_sticker: InputFile

    def files(self) -> List[InputFile]:
        if isinstance(self.png_sticker, InputFile):
            return [self.png_sticker]
        return list()


@dataclass(frozen=True)
class CreateNewStickerSet(Request):
    """\
    Represents CreateNewStickerSet request object:
    https://core.telegram.org/bots/api#createnewstickerset
    """

    method = "createNewStickerSet"

    user_id: int
    name: str
    title: str
    png_sticker: Union[InputFile, str]
    emojis: str
    contains_masks: Optional[bool] = None
    mask_position: Optional[MaskPosition] = None

    def files(self) -> List[InputFile]:
        if isinstance(self.png_sticker, InputFile):
            return [self.png_sticker]
        return list()


@dataclass(frozen=True)
class AddStickerToSet(Request):
    """\
    Represents AddStickerToSet request object:
    https://core.telegram.org/bots/api#addstickertoset
    """

    method = "addStickerToSet"

    user_id: int
    name: str
    png_sticker: Union[InputFile, str]
    emojis: str
    mask_position: Optional[MaskPosition] = None

    def files(self) -> List[InputFile]:
        if isinstance(self.png_sticker, InputFile):
            return [self.png_sticker]
        return list()


@dataclass(frozen=True)
class SetStickerPositionInSet(Request):
    """\
    Represents SetStickerPositionInSet request object:
    https://core.telegram.org/bots/api#setstickerpositioninset
    """

    method = "setStickerPositionInSet"

    sticker: str
    position: int


@dataclass(frozen=True)
class DeleteStickerFromSet(Request):
    """\
    Represents DeleteStickerFromSet request object:
    https://core.telegram.org/bots/api#deletestickerfromset
    """

    method = "deleteStickerFromSet"

    sticker: str


@dataclass(frozen=True)
class AnswerInlineQuery(Request):
    """\
    Represents AnswerInlineQuery request object:
    https://core.telegram.org/bots/api#answerinlinequery
    """

    method = "answerInlineQuery"

    inline_query_id: str
    results: List['InlineQueryResult']
    cache_time: Optional[int] = None
    is_personal: Optional[bool] = None
    next_offset: Optional[str] = None
    switch_pm_text: Optional[str] = None
    switch_pm_parameter: Optional[str] = None


@dataclass(frozen=True)
class InlineQueryResult:
    """\
    Represents InlineQueryResult object:
    https://core.telegram.org/bots/api#inlinequeryresult
    """


@dataclass(frozen=True)
class InlineQueryResultArticle(InlineQueryResult):
    """\
    Represents InlineQueryResultArticle object:
    https://core.telegram.org/bots/api#inlinequeryresultarticle
    """

    type: str = field(init=False, default='article')

    id: str
    title: str
    input_message_content: 'InputMessageContent'
    reply_markup: Optional[InlineKeyboardMarkup] = None
    url: Optional[str] = None
    hide_url: Optional[bool] = None
    description: Optional[str] = None
    thumb_url: Optional[str] = None
    thumb_width: Optional[int] = None
    thumb_height: Optional[int] = None


@dataclass(frozen=True)
class InlineQueryResultPhoto(InlineQueryResult):
    """\
    Represents InlineQueryResultPhoto object:
    https://core.telegram.org/bots/api#inlinequeryresultphoto
    """

    type: str = field(init=False, default='photo')

    id: str
    photo_url: str
    thumb_url: str
    photo_width: Optional[int] = None
    photo_height: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None


@dataclass(frozen=True)
class InlineQueryResultGif(InlineQueryResult):
    """\
    Represents InlineQueryResultGif object:
    https://core.telegram.org/bots/api#inlinequeryresultgif
    """

    type: str = field(init=False, default='gif')

    id: str
    gif_url: str
    thumb_url: str
    gif_width: Optional[int] = None
    gif_height: Optional[int] = None
    gif_duration: Optional[int] = None
    title: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None


@dataclass(frozen=True)
class InlineQueryResultMpeg4Gif(InlineQueryResult):
    """\
    Represents InlineQueryResultMpeg4Gif object:
    https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif
    """

    type: str = field(init=False, default='mpeg4_gif')

    id: str
    mpeg4_url: str
    thumb_url: str
    mpeg4_width: Optional[int] = None
    mpeg4_height: Optional[int] = None
    mpeg4_duration: Optional[int] = None
    title: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None


@dataclass(frozen=True)
class InlineQueryResultVideo(InlineQueryResult):
    """\
    Represents InlineQueryResultMpeg4Gif object:
    https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif
    """

    type: str = field(init=False, default='mpeg4_gif')

    id: str
    video_url: str
    mime_type: str
    thumb_url: str
    title: str
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    video_width: Optional[int] = None
    video_height: Optional[int] = None
    video_duration: Optional[int] = None
    description: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None


@dataclass(frozen=True)
class InlineQueryResultAudio(InlineQueryResult):
    """\
    Represents InlineQueryResultAudio object:
    https://core.telegram.org/bots/api#inlinequeryresultaudio
    """

    type: str = field(init=False, default='audio')

    id: str
    audio_url: str
    title: str
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    performer: Optional[str] = None
    audio_duration: Optional[int] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None


@dataclass(frozen=True)
class InlineQueryResultVoice(InlineQueryResult):
    """\
    Represents InlineQueryResultVoice object:
    https://core.telegram.org/bots/api#inlinequeryresultvoice
    """

    type: str = field(init=False, default='voice')

    id: str
    voice_url: str
    title: str
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    voice_duration: Optional[int] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None


@dataclass(frozen=True)
class InlineQueryResultDocument(InlineQueryResult):
    """\
    Represents InlineQueryResultDocument object:
    https://core.telegram.org/bots/api#inlinequeryresultdocument
    """

    type: str = field(init=False, default='document')

    id: str
    title: str
    document_url: str
    mime_type: str
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    description: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None
    thumb_url: Optional[str] = None
    thumb_width: Optional[int] = None
    thumb_height: Optional[int] = None


@dataclass(frozen=True)
class InlineQueryResultLocation(InlineQueryResult):
    """\
    Represents InlineQueryResultLocation object:
    https://core.telegram.org/bots/api#inlinequeryresultlocation
    """

    type: str = field(init=False, default='location')

    id: str
    latitude: float
    longitude: float
    title: str
    live_period: Optional[int] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None
    thumb_url: Optional[str] = None
    thumb_width: Optional[int] = None
    thumb_height: Optional[int] = None


@dataclass(frozen=True)
class InlineQueryResultVenue(InlineQueryResult):
    """\
    Represents InlineQueryResultVenue object:
    https://core.telegram.org/bots/api#inlinequeryresultvenue
    """

    type: str = field(init=False, default='venue')

    id: str
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None
    thumb_url: Optional[str] = None
    thumb_width: Optional[int] = None
    thumb_height: Optional[int] = None


@dataclass(frozen=True)
class InlineQueryResultContact(InlineQueryResult):
    """\
    Represents InlineQueryResultContact object:
    https://core.telegram.org/bots/api#inlinequeryresultcontact
    """

    type: str = field(init=False, default='contact')

    id: str
    phone_number: str
    first_name: str
    last_name: Optional[str] = None
    vcard: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None
    thumb_url: Optional[str] = None
    thumb_width: Optional[int] = None
    thumb_height: Optional[int] = None


@dataclass(frozen=True)
class InlineQueryResultGame(InlineQueryResult):
    """\
    Represents InlineQueryResultGame object:
    https://core.telegram.org/bots/api#inlinequeryresultgame
    """

    type: str = field(init=False, default='game')

    id: str
    game_short_name: str
    reply_markup: Optional[InlineKeyboardMarkup] = None


@dataclass(frozen=True)
class InlineQueryResultCachedPhoto(InlineQueryResult):
    """\
    Represents InlineQueryResultCachedPhoto object:
    https://core.telegram.org/bots/api#inlinequeryresultcachedphoto
    """

    type: str = field(init=False, default='photo')

    id: str
    photo_file_id: str
    title: Optional[str] = None
    description: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None


@dataclass(frozen=True)
class InlineQueryResultCachedGif(InlineQueryResult):
    """\
    Represents InlineQueryResultCachedGif object:
    https://core.telegram.org/bots/api#inlinequeryresultcachedgif
    """

    type: str = field(init=False, default='gif')

    id: str
    gif_file_id: str
    title: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None


@dataclass(frozen=True)
class InlineQueryResultCachedMpeg4Gif(InlineQueryResult):
    """\
    Represents InlineQueryResultCachedMpeg4Gif object:
    https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif
    """

    type: str = field(init=False, default='mpeg4_gif')

    id: str
    mpeg4_file_id: str
    title: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None


@dataclass(frozen=True)
class InlineQueryResultCachedSticker(InlineQueryResult):
    """\
    Represents InlineQueryResultCachedSticker object:
    https://core.telegram.org/bots/api#inlinequeryresultcachedsticker
    """

    type: str = field(init=False, default='sticker')

    id: str
    sticker_file_id: str
    parse_mode: Optional[ParseModeType] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None


@dataclass(frozen=True)
class InlineQueryResultCachedDocument(InlineQueryResult):
    """\
    Represents InlineQueryResultCachedDocument object:
    https://core.telegram.org/bots/api#inlinequeryresultcacheddocument
    """

    type: str = field(init=False, default='document')

    id: str
    document_file_id: str
    title: str
    description: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None


@dataclass(frozen=True)
class InlineQueryResultCachedVideo(InlineQueryResult):
    """\
    Represents InlineQueryResultCachedVideo object:
    https://core.telegram.org/bots/api#inlinequeryresultcachedvideo
    """

    type: str = field(init=False, default='video')

    id: str
    video_file_id: str
    title: str
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None


@dataclass(frozen=True)
class InlineQueryResultCachedVoice(InlineQueryResult):
    """\
    Represents InlineQueryResultCachedVoice object:
    https://core.telegram.org/bots/api#inlinequeryresultcachedvoice
    """

    type: str = field(init=False, default='voice')

    id: str
    voice_file_id: str
    title: str
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None


@dataclass(frozen=True)
class InlineQueryResultCachedAudio(InlineQueryResult):
    """\
    Represents InlineQueryResultCachedAudio object:
    https://core.telegram.org/bots/api#inlinequeryresultcachedaudio
    """

    type: str = field(init=False, default='audio')

    id: str
    audio_file_id: str
    caption: Optional[str] = None
    parse_mode: Optional[ParseModeType] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional['InputMessageContent'] = None


@dataclass(frozen=True)
class InputMessageContent:
    """\
    Represents InputMessageContent object:
    https://core.telegram.org/bots/api#inputmessagecontent
    """


@dataclass(frozen=True)
class InputTextMessageContent(InputMessageContent):
    """\
    Represents InputTextMessageContent object:
    https://core.telegram.org/bots/api#inputtextmessagecontent
    """

    message_text: str
    parse_mode: Optional[ParseModeType] = None
    disable_web_page_preview: Optional[bool] = None


@dataclass(frozen=True)
class InputLocationMessageContent(InputMessageContent):
    """\
    Represents InputLocationMessageContent object:
    https://core.telegram.org/bots/api#inputlocationmessagecontent
    """

    latitude: float
    longitude: float
    live_period: Optional[int] = None


@dataclass(frozen=True)
class InputVenueMessageContent(InputMessageContent):
    """\
    Represents InputVenueMessageContent object:
    https://core.telegram.org/bots/api#inputvenuemessagecontent
    """

    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None


@dataclass(frozen=True)
class InputContactMessageContent(InputMessageContent):
    """\
    Represents InputContactMessageContent object:
    https://core.telegram.org/bots/api#inputcontactmessagecontent
    """

    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None


class SendInvoice(Request):
    """\
    Represents SendInvoice request object:
    https://core.telegram.org/bots/api#sendinvoice
    """

    method = "sendInvoice"

    chat_id: int
    title: str
    description: str
    payload: str
    provider_token: str
    start_parameter: str
    currency: str
    prices: List[str]  # TODO: Add LabeledPrice type
    provider_data: Optional[str] = None
    photo_url: Optional[str] = None
    photo_size: Optional[int] = None
    photo_width: Optional[int] = None
    photo_height: Optional[int] = None
    need_name: Optional[bool] = None
    need_phone_number: Optional[bool] = None
    need_email: Optional[bool] = None
    need_shipping_address: Optional[bool] = None
    send_phone_number_to_provider: Optional[bool] = None
    send_email_to_provider: Optional[bool] = None
    is_flexible: Optional[bool] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[bool] = None
    reply_markup: Optional[Union['InlineKeyboardMarkup']] = None


@dataclass(frozen=True)
class AnswerShippingQuery(Request):
    """\
    Represents AnswerShippingQuery request object:
    https://core.telegram.org/bots/api#answershippingquery
    """

    method = "answerShippingQuery"

    shipping_query_id: str
    ok: bool
    shipping_options: Optional[List['ShippingOption']]
    error_message: Optional[str]


@dataclass(frozen=True)
class AnswerPreCheckoutQuery(Request):
    """\
    Represents AnswerPreCheckoutQuery request object:
    https://core.telegram.org/bots/api#answerprecheckoutquery
    """

    method = "answerPreCheckoutQuery"

    pre_checkout_query_id: str
    ok: bool
    error_message: Optional[str]


@dataclass(frozen=True)
class SetPassportDataErrors(Request):
    """\
    Represents SetPassportDataErrors request object:
    https://core.telegram.org/bots/api#answerprecheckoutquery
    """

    method = "setPassportDataErrors"

    user_id: str
    errors: List[Dict]  # TODO: PassportElementError


@dataclass(frozen=True)
class SendGame(Request):
    """\
    Represents SendGame request object:
    https://core.telegram.org/bots/api#sendgame
    """

    method = "sendGame"

    chat_id: int
    game_short_name: str
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[Union['InlineKeyboardMarkup']] = None


@dataclass(frozen=True)
class SetGameScore(Request):
    """\
    Represents SetGameScore request object:
    https://core.telegram.org/bots/api#setgamescore
    """

    method = "setGameScore"

    user_id: int
    score: int
    force: Optional[bool] = None
    disable_edit_message: Optional[bool] = None
    chat_id: Optional[int] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None


@dataclass(frozen=True)
class GetGameHighScores(Request):
    """\
    Represents GetGameHighScores request object:
    https://core.telegram.org/bots/api#getgamehighscores
    """

    method = "getGameHighScores"

    user_id: int
    chat_id: Optional[int] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
