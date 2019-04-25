# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import io
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional, List, Union

API_URL = "https://api.telegram.org/bot%s/"
API_FILE_URL = "https://api.telegram.org/file/bot%s/"


class EnumAutoName(Enum):
    """Class for enums."""

    def _generate_next_value_(self, start, count, last_values):
        return self


class InputFile:
    """\
    Represents InputFile request object:
    https://core.telegram.org/bots/api#inputfile
    """

    __slots__ = ('__file_name', '__content_type', '__data')

    def __init__(self, file_name: str, content_type: str, data: io.IOBase):
        self.__file_name = file_name
        self.__content_type = content_type
        self.__data = data

    @property
    def file_name(self) -> str:
        return self.__file_name

    @property
    def content_type(self) -> str:
        return self.__content_type

    @property
    def data(self) -> io.IOBase:
        return self.__data

    def __copy__(self):
        return self

    def __deepcopy__(self, memo):
        return self

    def __repr__(self):
        return "%s(%s, %s, %s)" % (self.__class__.__name__,
                                   repr(self.__file_name),
                                   repr(self.__content_type),
                                   repr(self.__data))


class UpdateType(EnumAutoName):
    message = auto()
    edited_message = auto()
    channel_post = auto()
    edited_channel_post = auto()
    inline_query = auto()
    chosen_inline_result = auto()
    callback_query = auto()
    shipping_query = auto()
    pre_checkout_query = auto()
    poll = auto()


class MessageType(EnumAutoName):
    text = auto()
    audio = auto()
    document = auto()
    animation = auto()
    game = auto()
    photo = auto()
    sticker = auto()
    video = auto()
    voice = auto()
    video_note = auto()
    contact = auto()
    location = auto()
    venue = auto()
    poll = auto()
    new_chat_members = auto()
    left_chat_member = auto()
    new_chat_title = auto()
    new_chat_photo = auto()
    delete_chat_photo = auto()
    group_chat_created = auto()
    supergroup_chat_created = auto()
    channel_chat_created = auto()
    migrate_to_chat_id = auto()
    migrate_from_chat_id = auto()
    pinned_message = auto()
    invoice = auto()
    successful_payment = auto()
    connected_website = auto()
    passport_data = auto()


class ChatType(EnumAutoName):
    private = auto()
    group = auto()
    supergroup = auto()
    channel = auto()


class EntityType(EnumAutoName):
    mention = auto()
    hashtag = auto()
    cashtag = auto()
    bot_command = auto()
    url = auto()
    email = auto()
    phone_number = auto()
    bold = auto()
    italic = auto()
    code = auto()
    pre = auto()
    text_link = auto()
    text_mention = auto()


class ChatMemberStatusType(EnumAutoName):
    creator = auto()
    administrator = auto()
    member = auto()
    restricted = auto()
    left = auto()
    kicked = auto()


class MaskPositionPointType(EnumAutoName):
    forehead = auto()
    eyes = auto()
    mouth = auto()
    chin = auto()


class EncryptedPassportElementType(EnumAutoName):
    personal_details = auto()
    passport = auto()
    driver_license = auto()
    identity_card = auto()
    internal_passport = auto()
    address = auto()
    utility_bill = auto()
    bank_statement = auto()
    rental_agreement = auto()
    passport_registration = auto()
    temporary_registration = auto()
    phone_number = auto()
    email = auto()


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
    callback_game: Optional[str] = None
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

    inline_keyboard: List[List['InlineKeyboardButton']]


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
class ForceReply:
    """\
    Represents ForceReply keyboard object:
    https://core.telegram.org/bots/api#forcereply
    """

    selective: bool = False
    force_reply: bool = True


@dataclass(frozen=True)
class InputMedia:
    """\
    Represents InputMedia object:
    https://core.telegram.org/bots/api#inputmedia
    """


@dataclass(frozen=True)
class InputMediaPhoto(InputMedia):
    """\
    Represents InputMediaPhoto object:
    https://core.telegram.org/bots/api#inputmediaphoto
    """

    type: str = field(init=False, default='photo')

    media: Union['InputFile', str]
    caption: Optional[str]
    parse_mode: Optional['ParseModeType']


@dataclass(frozen=True)
class InputMediaVideo(InputMedia):
    """\
    Represents InputMediaVideo object:
    https://core.telegram.org/bots/api#inputmediavideo
    """

    type: str = field(init=False, default='video')

    media: Union['InputFile', str]
    thumb: Optional[Union['InputFile', str]]
    caption: Optional[str]
    parse_mode: Optional['ParseModeType']
    width: Optional[int]
    height: Optional[int]
    duration: Optional[int]
    supports_streaming: Optional[bool]


@dataclass(frozen=True)
class InputMediaAnimation(InputMedia):
    """\
    Represents InputMediaAnimation object:
    https://core.telegram.org/bots/api#inputmediaanimation
    """

    type: str = field(init=False, default='animation')

    media: Union['InputFile', str]
    thumb: Optional[Union['InputFile', str]]
    caption: Optional[str]
    parse_mode: Optional['ParseModeType']
    width: Optional[int]
    height: Optional[int]
    duration: Optional[int]


@dataclass(frozen=True)
class InputMediaAudio(InputMedia):
    """\
    Represents InputMediaAudio object:
    https://core.telegram.org/bots/api#inputmediaaudio
    """

    type: str = field(init=False, default='audio')

    media: Union['InputFile', str]
    thumb: Optional[Union['InputFile', str]]
    caption: Optional[str]
    parse_mode: Optional['ParseModeType']
    duration: Optional[int]
    performer: Optional[str]
    title: Optional[str]


@dataclass(frozen=True)
class InputMediaDocument(InputMedia):
    """\
    Represents InputMediaDocument object:
    https://core.telegram.org/bots/api#inputmediadocument
    """

    type: str = field(init=False, default='document')

    media: Union['InputFile', str]
    thumb: Optional[Union['InputFile', str]]
    caption: Optional[str]
    parse_mode: Optional['ParseModeType']


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
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    parse_mode: Optional['ParseModeType'] = None
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    parse_mode: Optional['ParseModeType'] = None
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    parse_mode: Optional['ParseModeType'] = None
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    parse_mode: Optional['ParseModeType'] = None
    video_width: Optional[int] = None
    video_height: Optional[int] = None
    video_duration: Optional[int] = None
    description: Optional[str] = None
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    parse_mode: Optional['ParseModeType'] = None
    performer: Optional[str] = None
    audio_duration: Optional[int] = None
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    parse_mode: Optional['ParseModeType'] = None
    voice_duration: Optional[int] = None
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    parse_mode: Optional['ParseModeType'] = None
    description: Optional[str] = None
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    reply_markup: Optional['InlineKeyboardMarkup'] = None


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
    parse_mode: Optional['ParseModeType'] = None
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    parse_mode: Optional['ParseModeType'] = None
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    parse_mode: Optional['ParseModeType'] = None
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    parse_mode: Optional['ParseModeType'] = None
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    parse_mode: Optional['ParseModeType'] = None
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    parse_mode: Optional['ParseModeType'] = None
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    parse_mode: Optional['ParseModeType'] = None
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    parse_mode: Optional['ParseModeType'] = None
    reply_markup: Optional['InlineKeyboardMarkup'] = None
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
    parse_mode: Optional['ParseModeType'] = None
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


@dataclass(frozen=True)
class LabeledPrice:
    """\
    Represents LabeledPrice object:
    https://core.telegram.org/bots/api#labeledprice
    """

    label: str
    amount: int


@dataclass(frozen=True)
class ShippingOption:
    """\
    Represents ShippingOption object:
    https://core.telegram.org/bots/api#shippingoption

    """

    id: str
    title: str
    prices: List['LabeledPrice']


@dataclass(frozen=True)
class PassportElementError:
    """\
    Represents PassportElementError object:
    https://core.telegram.org/bots/api#passportelementerror
    """


@dataclass(frozen=True)
class PassportElementErrorDataField(PassportElementError):
    """\
    Represents PassportElementErrorDataField object:
    https://core.telegram.org/bots/api#passportelementerrordatafield
    """

    source: str = field(init=False, default='data')

    type: 'EncryptedPassportElementType'
    field_name: str
    data_hash: str
    message: str


@dataclass(frozen=True)
class PassportElementErrorFrontSide(PassportElementError):
    """\
    Represents PassportElementErrorFrontSide object:
    https://core.telegram.org/bots/api#passportelementerrorfrontside
    """

    source: str = field(init=False, default='front_side')

    type: 'EncryptedPassportElementType'
    file_hash: str
    message: str


@dataclass(frozen=True)
class PassportElementErrorReverseSide(PassportElementError):
    """\
    Represents PassportElementErrorReverseSide object:
    https://core.telegram.org/bots/api#passportelementerrorreverseside
    """

    source: str = field(init=False, default='reverse_side')

    type: 'EncryptedPassportElementType'
    file_hash: str
    message: str


@dataclass(frozen=True)
class PassportElementErrorSelfie(PassportElementError):
    """\
    Represents PassportElementErrorSelfie object:
    https://core.telegram.org/bots/api#passportelementerrorselfie
    """

    source: str = field(init=False, default='selfie')

    type: 'EncryptedPassportElementType'
    file_hash: str
    message: str


@dataclass(frozen=True)
class PassportElementErrorFile(PassportElementError):
    """\
    Represents PassportElementErrorFile object:
    https://core.telegram.org/bots/api#passportelementerrorfile
    """
    source: str = field(init=False, default='file')

    type: 'EncryptedPassportElementType'
    file_hash: str
    message: str


@dataclass(frozen=True)
class PassportElementErrorFiles(PassportElementError):
    """\
    Represents PassportElementErrorFiles object:
    https://core.telegram.org/bots/api#passportelementerrorfiles
    """
    source: str = field(init=False, default='files')

    type: 'EncryptedPassportElementType'
    file_hashes: List[str]
    message: str


@dataclass(frozen=True)
class PassportElementErrorTranslationFile(PassportElementError):
    """\
    Represents PassportElementErrorTranslationFile object:
    https://core.telegram.org/bots/api#passportelementerrortranslationfile
    """
    source: str = field(init=False, default='translation_file')

    type: 'EncryptedPassportElementType'
    file_hash: str
    message: str


@dataclass(frozen=True)
class PassportElementErrorTranslationFiles(PassportElementError):
    """\
    Represents PassportElementErrorTranslationFiles object:
    https://core.telegram.org/bots/api#passportelementerrortranslationfiles
    """
    source: str = field(init=False, default='translation_files')

    type: 'EncryptedPassportElementType'
    file_hashes: List[str]
    message: str


@dataclass(frozen=True)
class PassportElementErrorUnspecified(PassportElementError):
    """\
    Represents PassportElementErrorUnspecified object:
    https://core.telegram.org/bots/api#passportelementerrorunspecified
    """
    source: str = field(init=False, default='unspecified')

    type: 'EncryptedPassportElementType'
    element_hash: str
    message: str
