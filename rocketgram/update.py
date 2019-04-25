# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING, Dict, List, Optional, Union

from .requests import GetUpdates, SetWebhook, DeleteWebhook, SendChatAction, KickChatMember, UnbanChatMember, \
    RestrictChatMember, PromoteChatMember, SetChatPhoto, DeleteChatPhoto, SetChatTitle, SetChatDescription, \
    PinChatMessage, UnpinChatMessage, LeaveChat, SetChatStickerSet, DeleteChatStickerSet, DeleteMessage, \
    CreateNewStickerSet, AddStickerToSet, SetStickerPositionInSet, DeleteStickerFromSet, SetPassportDataErrors, \
    SetGameScore, ExportChatInviteLink, GetChatMembersCount, AnswerCallbackQuery, AnswerInlineQuery, \
    AnswerPreCheckoutQuery, AnswerShippingQuery, GetWebhookInfo, GetMe, SendMessage, ForwardMessage, SendPhoto, \
    SendAudio, SendDocument, SendVideo, SendAnimation, SendVoice, SendVideoNote, SendLocation, SendVenue, SendContact, \
    SendPoll, SendSticker, SendInvoice, SendGame, EditMessageLiveLocation, StopMessageLiveLocation, StopPoll, \
    EditMessageText, EditMessageCaption, EditMessageMedia, EditMessageReplyMarkup, SendMediaGroup, \
    GetUserProfilePhotos, GetFile, UploadStickerFile, GetChat, GetChatMember, GetChatAdministrators, GetStickerSet, \
    GetGameHighScores
from .types import UpdateType, MessageType, ChatType, EntityType, ChatMemberStatusType, MaskPositionPointType, \
    EncryptedPassportElementType, MaskPosition

if TYPE_CHECKING:
    from .requests import Request


@dataclass(frozen=True)
class Response:
    """\
    Represents Response object:
    https://core.telegram.org/bots/api#making-requests

    Additional fields:
    method
    raw
    """

    method: 'Request'
    raw: dict
    ok: bool
    error_code: Optional[int]
    description: Optional[str]
    result: Optional[Union[bool, int, str, 'Chat', 'ChatMember', 'File', 'Message', List['GameHighScore'],
                           List['Update'], 'StickerSet', 'User', 'WebhookInfo', 'UserProfilePhotos',
                           List['ChatMember']]]
    parameters: Optional['ResponseParameters']

    @classmethod
    def parse(cls, data: dict, method: 'Request') -> Optional['Response']:
        if data is None:
            return None

        ok = data['ok']
        error_code = data.get('error_code')
        description = data.get('description')
        parameters = ResponseParameters.parse(data.get('parameters'))

        if error_code is not None:
            return cls(method, data, ok, error_code, description, None, parameters)

        result = None

        if isinstance(method, GetUpdates):
            result = [Update.parse(r) for r in data['result']]
        elif isinstance(method, (SetWebhook, DeleteWebhook, SendChatAction, KickChatMember, UnbanChatMember,
                                 RestrictChatMember, PromoteChatMember, SetChatPhoto, DeleteChatPhoto, SetChatTitle,
                                 SetChatDescription, PinChatMessage, UnpinChatMessage, LeaveChat, SetChatStickerSet,
                                 DeleteChatStickerSet, DeleteMessage, CreateNewStickerSet, AddStickerToSet,
                                 SetStickerPositionInSet, DeleteStickerFromSet, SetPassportDataErrors, SetGameScore,
                                 ExportChatInviteLink, GetChatMembersCount, AnswerCallbackQuery, AnswerInlineQuery,
                                 AnswerPreCheckoutQuery, AnswerShippingQuery)):
            result = data['result']
        elif isinstance(method, GetWebhookInfo):
            result = WebhookInfo.parse(data['result'])
        elif isinstance(method, GetMe):
            result = User.parse(data['result'])
        elif isinstance(method, (SendMessage, ForwardMessage, SendPhoto, SendAudio, SendDocument, SendVideo,
                                 SendAnimation, SendVoice, SendVideoNote, SendLocation, SendVenue, SendContact,
                                 SendPoll, SendSticker, SendInvoice, SendGame)):
            result = Message.parse(data['result'])
        elif isinstance(method, (EditMessageLiveLocation, StopMessageLiveLocation, EditMessageText, EditMessageCaption,
                                 EditMessageMedia, EditMessageReplyMarkup)):
            r = data['result']
            if isinstance(r, bool):
                result = r
            else:
                result = Message.parse(r)
        elif isinstance(method, StopPoll):
            result = Poll.parse(data['result'])
        elif isinstance(method, SendMediaGroup):
            result = [Message.parse(r) for r in data['result']]
        elif isinstance(method, GetUserProfilePhotos):
            result = UserProfilePhotos.parse(data['result'])
        elif isinstance(method, (GetFile, UploadStickerFile)):
            result = File.parse(data['result'])
        elif isinstance(method, GetChat):
            result = Chat.parse(data['result'])
        elif isinstance(method, GetChatMember):
            result = ChatMember.parse(data['result'])
        elif isinstance(method, GetChatAdministrators):
            result = [ChatMember.parse(r) for r in data['result']]
        elif isinstance(method, GetStickerSet):
            result = StickerSet.parse(data['result'])
        elif isinstance(method, GetGameHighScores):
            result = [GameHighScore.parse(r) for r in data['result']]

        assert result is not None, "Should have value here! This probably means api was changed."

        return cls(method, data, ok, error_code, description, result, parameters)


@dataclass(frozen=True)
class Update:
    """\
    Represents Update object:
    https://core.telegram.org/bots/api#update

    Additional fields:
    raw
    update_type
    """

    raw: Dict
    update_id: int
    update_type: UpdateType
    message: Optional['Message']
    edited_message: Optional['Message']
    channel_post: Optional['Message']
    edited_channel_post: Optional['Message']
    inline_query: Optional['InlineQuery']
    chosen_inline_result: Optional['ChosenInlineResult']
    callback_query: Optional['CallbackQuery']
    shipping_query: Optional['ShippingQuery']
    pre_checkout_query: Optional['PreCheckoutQuery']
    poll: Optional['Poll']

    @classmethod
    def parse(cls, data: Dict) -> 'Update':
        message = Message.parse(data.get('message'))
        edited_message = Message.parse(data.get('edited_message'))
        channel_post = Message.parse(data.get('channel_post'))
        edited_channel_post = Message.parse(data.get('edited_channel_post'))
        inline_query = InlineQuery.parse(data.get('inline_query'))
        chosen_inline_result = ChosenInlineResult.parse(data.get('chosen_inline_result'))
        callback_query = CallbackQuery.parse(data.get('callback_query'))
        shipping_query = ShippingQuery.parse(data.get('shipping_query'))
        pre_checkout_query = PreCheckoutQuery.parse(data.get('pre_checkout_query'))
        poll = Poll.parse(data.get('poll'))

        update_type = None
        if 'message' in data:
            update_type = UpdateType.message
        elif 'edited_message' in data:
            update_type = UpdateType.edited_message
        elif 'channel_post' in data:
            update_type = UpdateType.channel_post
        elif 'edited_channel_post' in data:
            update_type = UpdateType.edited_channel_post
        elif 'inline_query' in data:
            update_type = UpdateType.inline_query
        elif 'chosen_inline_result' in data:
            update_type = UpdateType.chosen_inline_result
        elif 'callback_query' in data:
            update_type = UpdateType.callback_query
        elif 'shipping_query' in data:
            update_type = UpdateType.shipping_query
        elif 'pre_checkout_query' in data:
            update_type = UpdateType.pre_checkout_query
        elif 'poll' in data:
            update_type = UpdateType.poll

        return cls(data, data['update_id'], update_type, message, edited_message, channel_post, edited_channel_post,
                   inline_query, chosen_inline_result, callback_query, shipping_query, pre_checkout_query, poll)


@dataclass(frozen=True)
class WebhookInfo:
    """\
    Represents WebhookInfo object:
    https://core.telegram.org/bots/api#getwebhookinfo
    """

    url: str
    has_custom_certificate: bool
    pending_update_count: int
    last_error_date: Optional[datetime]
    last_error_message: Optional[str]
    max_connections: Optional[int]
    allowed_updates: Optional[List['UpdateType']]

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['WebhookInfo']:
        if data is None:
            return None

        last_error_date = datetime.utcfromtimestamp(data['last_error_date']) if 'last_error_date' in data else None
        max_connections = [UpdateType(m) for m in data['max_connections']] if 'max_connections' in data else None

        return cls(data['url'], data['has_custom_certificate'], data['pending_update_count'], last_error_date,
                   data.get('last_error_message'), data.get('max_connections'), max_connections)


@dataclass(frozen=True)
class User:
    """\
    Represents User object:
    https://core.telegram.org/bots/api#user

    Differences in field names:
    id -> user_id
    """

    user_id: int
    is_bot: bool
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    language_code: Optional[str]

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['User']:
        if data is None:
            return None

        return cls(data['id'], data['is_bot'], data['first_name'], data.get('last_name'), data.get('username'),
                   data.get('language_code'))


@dataclass(frozen=True)
class Chat:
    """\
    Represents Chat object:
    https://core.telegram.org/bots/api#chat

    Differences in field names:
    id -> chat_id
    type -> chat_type
    """

    chat_id: int
    chat_type: ChatType
    title: Optional[str]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    all_members_are_administrators: Optional[bool]
    photo: Optional['ChatPhoto']
    description: Optional[str]
    invite_link: Optional[str]
    pinned_message: Optional['Message']
    sticker_set_name: Optional[str]
    can_set_sticker_set: Optional[bool]

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['Chat']:
        if data is None:
            return None

        return cls(data['id'], ChatType(data['type']), data.get('title'), data.get('username'), data.get('first_name'),
                   data.get('last_name'), data.get('all_members_are_administrators'),
                   ChatPhoto.parse(data.get('photo')), data.get('description'), data.get('invite_link'),
                   Message.parse(data.get('pinned_message')), data.get('sticker_set_name'),
                   data.get('can_set_sticker_set'))


@dataclass(frozen=True)
class Message:
    """\
    Represents Message object:
    https://core.telegram.org/bots/api#message

    Differences in field names:
    from -> user

    Additional fields:
    message_type
    """

    message_id: int
    message_type: MessageType
    user: Optional['User']
    date: datetime
    chat: 'Chat'
    forward_from: Optional['User']
    forward_from_chat: Optional['Chat']
    forward_from_message_id: Optional[int]
    forward_signature: Optional[str]
    forward_sender_name: Optional[str]
    forward_date: Optional[datetime]
    reply_to_message: Optional['Message']
    edit_date: Optional[datetime]
    media_group_id: Optional[str]
    author_signature: Optional[str]

    text: Optional[str]
    entities: Optional[List['MessageEntity']]
    caption_entities: Optional[List['MessageEntity']]

    audio: Optional['Audio']
    document: Optional['Document']
    animation: Optional['Animation']
    game: Optional['Game']
    photo: Optional[List['PhotoSize']]
    sticker: Optional['Sticker']
    video: Optional['Video']
    voice: Optional['Voice']
    video_note: Optional['VideoNote']

    caption: Optional[str]

    contact: Optional['Contact']
    location: Optional['Location']
    venue: Optional['Venue']
    poll: Optional['Poll']

    new_chat_members: Optional[List['User']]
    left_chat_member: Optional[User]
    new_chat_title: Optional[str]
    new_chat_photo: Optional[List['PhotoSize']]
    delete_chat_photo: Optional[bool]

    group_chat_created: Optional[bool]
    supergroup_chat_created: Optional[bool]
    channel_chat_created: Optional[bool]

    migrate_to_chat_id: Optional[int]
    migrate_from_chat_id: Optional[int]

    pinned_message: Optional['Message']

    invoice: Optional['Invoice']
    successful_payment: Optional['SuccessfulPayment']

    connected_website: Optional[str]
    passport_data: Optional['PassportData']

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['Message']:
        if data is None:
            return None

        message_id = data['message_id']
        user = User.parse(data.get('from'))
        date = datetime.utcfromtimestamp(data['date'])
        chat = Chat.parse(data['chat'])
        forward_from = User.parse(data.get('forward_from'))
        forward_from_chat = Chat.parse(data.get('forward_from_chat'))
        forward_from_message_id = data.get('forward_from_message_id')
        forward_sender_name = data.get('forward_sender_name')
        forward_signature = data.get('forward_signature')
        forward_date = datetime.utcfromtimestamp(data['forward_date']) if 'forward_date' in data else None
        reply_to_message = Message.parse(data.get('reply_to_message'))
        edit_date = datetime.utcfromtimestamp(data['edit_date']) if 'edit_date' in data else None
        media_group_id = data.get('media_group_id')
        author_signature = data.get('author_signature')

        text = data.get('text')

        entities = [MessageEntity.parse(d) for d in data.get('entities')] if 'entities' in data else None
        caption_entities = [MessageEntity.parse(d) for d in
                            data.get('caption_entities')] if 'caption_entities' in data else None

        audio = Audio.parse(data.get('audio'))
        document = Document.parse(data.get('document'))
        animation = Animation.parse(data.get('animation'))
        if animation is not None:
            document = None
        game = Game.parse(data.get('game'))
        photo = [PhotoSize.parse(d) for d in data.get('photo')] if 'photo' in data else None
        sticker = Sticker.parse(data.get('sticker'))
        video = Video.parse(data.get('video'))
        voice = Voice.parse(data.get('voice'))
        video_note = VideoNote.parse(data.get('video_note'))

        caption = data.get('caption')

        contact = Contact.parse(data.get('contact'))
        location = Location.parse(data.get('location'))
        venue = Venue.parse(data.get('venue'))
        poll = Poll.parse(data.get('poll'))

        new_chat_members = [User.parse(d) for d in
                            data.get('new_chat_members')] if 'new_chat_members' in data else None
        left_chat_member = User.parse(data.get('left_chat_member'))
        new_chat_title = data.get('new_chat_title')
        new_chat_photo = [PhotoSize.parse(d) for d in
                          data.get('new_chat_photo')] if 'new_chat_photo' in data else None
        delete_chat_photo = data.get('delete_chat_photo')

        group_chat_created = data.get('group_chat_created')
        supergroup_chat_created = data.get('supergroup_chat_created')
        channel_chat_created = data.get('channel_chat_created')

        migrate_to_chat_id = data.get('migrate_to_chat_id')
        migrate_from_chat_id = data.get('migrate_from_chat_id')

        pinned_message = Message.parse(data.get('pinned_message'))

        invoice = Invoice.parse(data.get('invoice'))
        successful_payment = SuccessfulPayment.parse(data.get('successful_payment'))

        connected_website = data.get('connected_website')
        passport_data = PassportData.parse(data.get('passport_data'))

        message_type = None

        if text is not None:
            message_type = MessageType.text
        elif audio is not None:
            message_type = MessageType.audio
        elif document is not None and animation is None:
            message_type = MessageType.document
        elif animation is not None:
            message_type = MessageType.animation
        elif game is not None:
            message_type = MessageType.game
        elif photo is not None:
            message_type = MessageType.photo
        elif sticker is not None:
            message_type = MessageType.sticker
        elif video is not None:
            message_type = MessageType.video
        elif voice is not None:
            message_type = MessageType.voice
        elif video_note is not None:
            message_type = MessageType.video_note
        elif new_chat_members is not None:
            message_type = MessageType.new_chat_members
        elif contact is not None:
            message_type = MessageType.contact
        elif location is not None:
            message_type = MessageType.location
        elif venue is not None:
            message_type = MessageType.venue
        elif poll is not None:
            message_type = MessageType.poll
        elif left_chat_member is not None:
            message_type = MessageType.left_chat_member
        elif new_chat_title is not None:
            message_type = MessageType.new_chat_title
        elif new_chat_photo is not None:
            message_type = MessageType.new_chat_photo
        elif delete_chat_photo is not None:
            message_type = MessageType.delete_chat_photo
        elif group_chat_created is not None:
            message_type = MessageType.group_chat_created
        elif supergroup_chat_created is not None:
            message_type = MessageType.supergroup_chat_created
        elif channel_chat_created is not None:
            message_type = MessageType.channel_chat_created
        elif migrate_to_chat_id is not None:
            message_type = MessageType.migrate_to_chat_id
        elif migrate_from_chat_id is not None:
            message_type = MessageType.migrate_from_chat_id
        elif pinned_message is not None:
            message_type = MessageType.pinned_message
        elif invoice is not None:
            message_type = MessageType.invoice
        elif successful_payment is not None:
            message_type = MessageType.successful_payment
        elif connected_website is not None:
            message_type = MessageType.connected_website
        elif passport_data is not None:
            passport_data = MessageType.passport_data

        return cls(message_id, message_type, user, date, chat, forward_from, forward_from_chat, forward_from_message_id,
                   forward_signature, forward_sender_name, forward_date, reply_to_message, edit_date, media_group_id,
                   author_signature, text, entities, caption_entities, audio, document, animation, game, photo, sticker,
                   video, voice, video_note, caption, contact, location, venue, poll, new_chat_members,
                   left_chat_member, new_chat_title, new_chat_photo, delete_chat_photo, group_chat_created,
                   supergroup_chat_created, channel_chat_created, migrate_to_chat_id, migrate_from_chat_id,
                   pinned_message, invoice, successful_payment, connected_website, passport_data)


@dataclass(frozen=True)
class MessageEntity:
    """\
    Represents MessageEntity object:
    https://core.telegram.org/bots/api#messageentity

    Differences in field names:
    type -> entity_type
    """

    entity_type: EntityType
    offset: int
    length: int
    url: Optional[str]
    user: Optional[User]

    @classmethod
    def parse(cls, data: dict) -> Optional['MessageEntity']:
        if data is None:
            return None

        return cls(EntityType(data['type']), data['offset'], data['length'], data.get('url'),
                   User.parse(data.get('user')))


@dataclass(frozen=True)
class PhotoSize:
    """\
    Represents PhotoSize object:
    https://core.telegram.org/bots/api#photosize
    """

    file_id: str
    width: int
    height: int
    file_size: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['PhotoSize']:
        if data is None:
            return None

        return cls(data['file_id'], data['width'], data['height'], data.get('file_size'))


@dataclass(frozen=True)
class Audio:
    """\
    Represents Audio object:
    https://core.telegram.org/bots/api#audio
    """

    file_id: str
    duration: int
    performer: Optional[str]
    title: Optional[str]
    mime_type: Optional[str]
    file_size: Optional[int]
    thumb: Optional[PhotoSize]

    @classmethod
    def parse(cls, data: dict) -> Optional['Audio']:
        if data is None:
            return None

        return cls(data['file_id'], data['duration'], data.get('performer'), data.get('title'),
                   data.get('mime_type'), data.get('file_size'), PhotoSize.parse(data.get('thumb')))


@dataclass(frozen=True)
class Document:
    """\
    Represents Document object:
    https://core.telegram.org/bots/api#document
    """

    file_id: str
    thumb: Optional[PhotoSize]
    file_name: Optional[str]
    mime_type: Optional[str]
    file_size: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['Document']:
        if data is None:
            return None

        return cls(data['file_id'], PhotoSize.parse(data.get('thumb')), data.get('file_name'),
                   data.get('mime_type'), data.get('file_size'))


@dataclass(frozen=True)
class Video:
    """\
    Represents Video object:
    https://core.telegram.org/bots/api#video
    """

    file_id: str
    width: int
    height: int
    duration: int
    thumb: Optional['PhotoSize']
    mime_type: Optional[str]
    file_size: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['Video']:
        if data is None:
            return None

        return cls(data['file_id'], data['width'], data['height'], data['duration'],
                   PhotoSize.parse(data.get('thumb')), data.get('mime_type'), data.get('file_size'))


@dataclass(frozen=True)
class Animation:
    """\
    Represents Animation object:
    https://core.telegram.org/bots/api#animation
    """

    file_id: str
    width: str
    height: str
    duration: str
    thumb: Optional['PhotoSize']
    file_name: Optional[str]
    mime_type: Optional[str]
    file_size: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['Animation']:
        if data is None:
            return None

        return cls(data['file_id'], data['width'], data['height'], data['duration'],
                   PhotoSize.parse(data.get('thumb')), data.get('file_name'),
                   data.get('mime_type'), data.get('file_size'))


@dataclass(frozen=True)
class Voice:
    """\
    Represents Voice object:
    https://core.telegram.org/bots/api#voice
    """

    file_id: str
    duration: int
    mime_type: Optional[str]
    file_size: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['Voice']:
        if data is None:
            return None

        return cls(data['file_id'], data['duration'], data.get('mime_type'), data.get('file_size'))


@dataclass(frozen=True)
class VideoNote:
    """\
    Represents VideoNote object:
    https://core.telegram.org/bots/api#videonote
    """

    file_id: str
    length: int
    duration: int
    thumb: Optional['PhotoSize']
    file_size: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['VideoNote']:
        if data is None:
            return None

        return cls(data['file_id'], data['length'], data['duration'],
                   PhotoSize.parse(data.get('thumb')), data.get('file_size'))


@dataclass(frozen=True)
class Contact:
    """\
    Represents Contact object:
    https://core.telegram.org/bots/api#contact
    """

    phone_number: str
    first_name: str
    last_name: Optional[str]
    user_id: Optional[int]
    vcard: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['Contact']:
        if data is None:
            return None

        return cls(data['phone_number'], data['first_name'], data.get('last_name'),
                   data.get('user_id'), data.get('vcard'))


@dataclass(frozen=True)
class Location:
    """\
    Represents Location object:
    https://core.telegram.org/bots/api#location
    """

    longitude: float
    latitude: float

    @classmethod
    def parse(cls, data: dict) -> Optional['Location']:
        if data is None:
            return None

        return cls(data['longitude'], data['latitude'])


@dataclass(frozen=True)
class Venue:
    """\
    Represents Venue object:
    https://core.telegram.org/bots/api#venue
    """

    location: Location
    title: str
    address: str
    foursquare_id: Optional[str]
    foursquare_type: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['Venue']:
        if data is None:
            return None

        return cls(Location.parse(data['location']), data['title'], data['address'],
                   data.get('foursquare_id'), data.get('foursquare_type'))


@dataclass(frozen=True)
class PollOption:
    """\
    Represents PollOption object:
    https://core.telegram.org/bots/api#polloption
    """

    text: str
    voter_count: int

    @classmethod
    def parse(cls, data: dict) -> Optional['PollOption']:
        if data is None:
            return None

        return cls(data['text'], data['voter_count'])


@dataclass(frozen=True)
class Poll:
    """\
    Represents Poll object:
    https://core.telegram.org/bots/api#poll
    """

    pool_id: str
    question: str
    options: List['PollOption']
    is_closed: bool

    @classmethod
    def parse(cls, data: dict) -> Optional['Poll']:
        if data is None:
            return None

        options = [PollOption.parse(i) for i in data['options']]

        return cls(data['id'], data['question'], options, data['is_closed'])


@dataclass(frozen=True)
class UserProfilePhotos:
    """\
    Represents UserProfilePhotos object:
    https://core.telegram.org/bots/api#userprofilephotos
    """

    total_count: int
    photos: List[List['PhotoSize']]

    @classmethod
    def parse(cls, data: dict) -> Optional['UserProfilePhotos']:
        if data is None:
            return None

        photos = [[PhotoSize.parse(i) for i in p] for p in data['photos']]

        return cls(data['total_count'], photos)


@dataclass(frozen=True)
class File:
    """\
    Represents File object:
    https://core.telegram.org/bots/api#file
    """

    file_id: str
    file_size: Optional[int]
    file_path: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['File']:
        if data is None:
            return None

        return cls(data['file_id'], data.get('file_size'), data.get('file_path'))


@dataclass(frozen=True)
class CallbackQuery:
    """\
    Represents CallbackQuery object:
    https://core.telegram.org/bots/api#callbackquery

    Differences in field names:
    id -> query_id
    from -> user
    """

    query_id: str
    user: 'User'
    message: Optional['Message']
    inline_message_id: Optional[str]
    chat_instance: str
    data: Optional[str]
    game_short_name: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['CallbackQuery']:
        if data is None:
            return None

        return cls(data['id'], User.parse(data['from']), Message.parse(data.get('message')),
                   data.get('inline_message_id'), data['chat_instance'], data.get('data'), data.get('game_short_name'))


@dataclass(frozen=True)
class ChatPhoto:
    """\
    Represents ChatPhoto object:
    https://core.telegram.org/bots/api#chatphoto
    """

    small_file_id: str
    big_file_id: str

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['ChatPhoto']:
        if data is None:
            return None

        return cls(data['small_file_id'], data['big_file_id'])


@dataclass(frozen=True)
class ChatMember:
    """\
    Represents ChatMember object:
    https://core.telegram.org/bots/api#chatmember
    """

    user: 'User'
    status: 'ChatMemberStatusType'
    until_date: Optional[datetime]
    can_be_edited: Optional[bool]
    can_change_info: Optional[bool]
    can_post_messages: Optional[bool]
    can_edit_messages: Optional[bool]
    can_delete_messages: Optional[bool]
    can_invite_users: Optional[bool]
    can_restrict_members: Optional[bool]
    can_pin_messages: Optional[bool]
    can_promote_members: Optional[bool]
    is_member: Optional[bool]
    can_send_messages: Optional[bool]
    can_send_media_messages: Optional[bool]
    can_send_other_messages: Optional[bool]
    can_add_web_page_previews: Optional[bool]

    @classmethod
    def parse(cls, data: dict) -> Optional['ChatMember']:
        if data is None:
            return None

        until_date = datetime.utcfromtimestamp(data['until_date']) if 'until_date' in data else None

        return cls(User.parse(data['user']), ChatMemberStatusType(data['status']), until_date,
                   data.get('can_be_edited'), data.get('can_change_info'), data.get('can_post_messages'),
                   data.get('can_edit_messages'), data.get('can_delete_messages'), data.get('can_invite_users'),
                   data.get('can_restrict_members'), data.get('can_pin_messages'), data.get('can_promote_members'),
                   data.get('is_member'), data.get('can_send_messages'), data.get('can_send_media_messages'),
                   data.get('can_send_other_messages'), data.get('can_add_web_page_previews'))


@dataclass(frozen=True)
class ResponseParameters:
    """\
    Represents ResponseParameters object:
    https://core.telegram.org/bots/api#responseparameters
    """

    migrate_to_chat_id: int
    retry_after: int

    @classmethod
    def parse(cls, data: dict) -> Optional['ResponseParameters']:
        if data is None:
            return None

        return cls(data['migrate_to_chat_id'], data['retry_after'])


@dataclass(frozen=True)
class MaskPosition:
    """\
    Represents MaskPosition object:
    https://core.telegram.org/bots/api#maskposition
    """

    point: MaskPositionPointType
    x_shift: float
    y_shift: float
    scale: float

    @classmethod
    def parse(cls, data: dict) -> Optional['MaskPosition']:
        if data is None:
            return None

        return cls(MaskPositionPointType(data['point']), data['x_shift'], data['y_shift'], data['scale'])


@dataclass(frozen=True)
class StickerSet:
    """\
    Represents StickerSet object:
    https://core.telegram.org/bots/api#stickerset
    """

    name: str
    title: str
    contains_masks: bool
    stickers: List['Sticker']

    @classmethod
    def parse(cls, data: dict) -> Optional['StickerSet']:
        if data is None:
            return None

        stickers = [Sticker.parse(s) for s in data['stickers']]

        return cls(data['name'], data['title'], data['contains_masks'], stickers)


@dataclass(frozen=True)
class Sticker:
    """\
    Represents Sticker object:
    https://core.telegram.org/bots/api#sticker
    """

    file_id: str
    width: int
    height: int
    thumb: Optional[PhotoSize]
    emoji: Optional[str]
    set_name: Optional[str]
    mask_position: Optional[MaskPosition]
    file_size: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['Sticker']:
        if data is None:
            return None

        return cls(data['file_id'], data['width'], data['height'], PhotoSize.parse(data.get('thumb')),
                   data.get('emoji'), data.get('set_name'), MaskPosition.parse(data.get('mask_position')),
                   data.get('file_size'))


@dataclass(frozen=True)
class InlineQuery:
    """\
    Represents InlineQuery object:
    https://core.telegram.org/bots/api#inlinequery

    Differences in field names:
    id -> query_id
    from -> user
    """

    query_id: str
    user: 'User'
    location: Optional['Location']
    query: str
    offset: str

    @classmethod
    def parse(cls, data: dict) -> Optional['InlineQuery']:
        if data is None:
            return None

        return cls(data['id'], User.parse(data['from']), Location.parse(data.get('location')),
                   data['query'], data['offset'])


@dataclass(frozen=True)
class ChosenInlineResult:
    """\
    Represents ChosenInlineResult object:
    https://core.telegram.org/bots/api#choseninlineresult

    Differences in field names:
    from -> user
    """

    result_id: str
    user: 'User'
    location: Optional['Location']
    inline_message_id: Optional[str]
    query: str

    @classmethod
    def parse(cls, data: dict) -> Optional['ChosenInlineResult']:
        if data is None:
            return None

        return cls(data['result_id'], User.parse(data['from']), Location.parse(data.get('location')),
                   data.get('inline_message_id'), data['query'])


@dataclass(frozen=True)
class Invoice:
    """\
    Represents Invoice object:
    https://core.telegram.org/bots/api#invoice
    """

    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: str

    @classmethod
    def parse(cls, data: dict) -> Optional['Invoice']:
        if data is None:
            return None

        return cls(data['title'], data['description'], data['start_parameter'], data['currency'], data['total_amount'])


@dataclass(frozen=True)
class ShippingAddress:
    """\
    Represents ShippingAddress object:
    https://core.telegram.org/bots/api#shippingaddress
    """

    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    post_code: str

    @classmethod
    def parse(cls, data: dict) -> Optional['ShippingAddress']:
        if data is None:
            return None

        return cls(data['country_code'], data['state'], data['city'], data['street_line1'],
                   data['street_line2'], data['post_code'])


@dataclass(frozen=True)
class OrderInfo:
    """\
    Represents OrderInfo object:
    https://core.telegram.org/bots/api#orderinfo
    """

    name: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    shipping_address: Optional['ShippingAddress']

    @classmethod
    def parse(cls, data: dict) -> Optional['OrderInfo']:
        if data is None:
            return None

        return cls(data.get('name'), data.get('phone_number'), data.get('email'),
                   ShippingAddress.parse(data.get('shipping_address')))


@dataclass(frozen=True)
class SuccessfulPayment:
    """\
    Represents SuccessfulPayment object:
    https://core.telegram.org/bots/api#successfulpayment
    """

    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: Optional[str]
    order_info: Optional['OrderInfo']
    telegram_payment_charge_id: str
    provider_payment_charge_id: str

    @classmethod
    def parse(cls, data: dict) -> Optional['SuccessfulPayment']:
        if data is None:
            return None

        return cls(data['currency'], data['total_amount'], data['invoice_payload'], data.get('shipping_option_id'),
                   OrderInfo.parse(data.get('order_info')), data['telegram_payment_charge_id'],
                   data['provider_payment_charge_id'])


@dataclass(frozen=True)
class ShippingQuery:
    """\
    Represents ShippingQuery object:
    https://core.telegram.org/bots/api#successfulpayment

    Differences in field names:
    from -> user
    """

    query_id: str
    user: 'User'
    invoice_payload: str
    shipping_address: 'ShippingAddress'

    @classmethod
    def parse(cls, data: dict) -> Optional['ShippingQuery']:
        if data is None:
            return None

        return cls(data['id'], User.parse(data['from']), data['invoice_payload'],
                   ShippingAddress.parse(data['shipping_address']))


@dataclass(frozen=True)
class PreCheckoutQuery:
    """\
    Represents PreCheckoutQuery object:
    https://core.telegram.org/bots/api#precheckoutquery

    Differences in field names:
    id -> query_id
    from -> user
    """

    query_id: str
    user: 'User'
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: Optional[str]
    order_info: Optional['OrderInfo']

    @classmethod
    def parse(cls, data: dict) -> Optional['PreCheckoutQuery']:
        if data is None:
            return None

        return cls(data['id'], User.parse(data['from']), data['currency'], data['total_amount'],
                   data['invoice_payload'], data.get('shipping_option_id'),
                   OrderInfo.parse(data.get('order_info')))


@dataclass(frozen=True)
class PassportData:
    """\
    Represents PassportData object:
    https://core.telegram.org/bots/api#passportdata
    """

    data: List['EncryptedPassportElement']
    credentials: 'EncryptedCredentials'

    @classmethod
    def parse(cls, data: dict) -> Optional['PassportData']:
        if data is None:
            return None

        list_data = [EncryptedPassportElement.parse(s) for s in data['data']]
        credentials = EncryptedCredentials.parse(data['credentials'])

        return cls(list_data, credentials)


@dataclass(frozen=True)
class PassportFile:
    """\
    Represents PassportFile object:
    https://core.telegram.org/bots/api#passportfile
    """

    file_id: str
    file_size: int
    file_date: datetime

    @classmethod
    def parse(cls, data: dict) -> Optional['PassportFile']:
        if data is None:
            return None

        return cls(data['file_id'], data['file_size'], datetime.utcfromtimestamp(data['file_date']))


@dataclass(frozen=True)
class EncryptedPassportElement:
    """\
    Represents EncryptedPassportElement object:
    https://core.telegram.org/bots/api#encryptedpassportelement

    Differences in field names:
    type -> encrypted_passport_element_type
    """

    encrypted_passport_element_type: 'EncryptedPassportElementType'
    data: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    files: Optional[List['PassportFile']]
    front_side: Optional['PassportFile']
    reverse_side: Optional['PassportFile']
    selfie: Optional['PassportFile']
    translation: Optional[List['PassportFile']]
    hash: str

    @classmethod
    def parse(cls, data: dict) -> Optional['EncryptedPassportElement']:
        if data is None:
            return None

        files = [PassportFile.parse(s) for s in data['files']] if 'files' in data else None
        translation = [PassportFile.parse(s) for s in data['translation']] if 'translation' in data else None

        return cls(EncryptedPassportElementType(data['type']), data.get('data'), data.get('phone_number'),
                   data.get('email'), files, PassportFile.parse(data.get('front_side')),
                   PassportFile.parse(data.get('reverse_side')), PassportFile.parse(data.get('selfie')), translation,
                   data['hash'])


@dataclass(frozen=True)
class EncryptedCredentials:
    """\
    Represents EncryptedCredentials object:
    https://core.telegram.org/bots/api#encryptedcredentials
    """

    data: str
    hash: str
    secret: str

    @classmethod
    def parse(cls, data: dict) -> Optional['EncryptedCredentials']:
        if data is None:
            return None

        return cls(data['data'], data['hash'], data['secret'])


@dataclass(frozen=True)
class Game:
    """\
    Represents Game object:
    https://core.telegram.org/bots/api#game
    """

    title: str
    description: str
    photo: List['PhotoSize']
    text: Optional[str]
    text_entities: Optional[List['MessageEntity']]
    animation: Optional['Animation']

    @classmethod
    def parse(cls, data: dict) -> Optional['Game']:
        if data is None:
            return None

        photo = [PhotoSize.parse(s) for s in data['photo']]
        text_entities = [MessageEntity.parse(s) for s in data['text_entities']] if 'text_entities' in data else None

        return cls(data['title'], data['description'], photo, data.get('text'),
                   text_entities, Animation.parse(data.get('animation')))


@dataclass(frozen=True)
class GameHighScore:
    """\
    Represents GameHighScore object:
    https://core.telegram.org/bots/api#gamehighscore
    """

    position: int
    user: 'User'
    score: int

    @classmethod
    def parse(cls, data: dict) -> Optional['GameHighScore']:
        if data is None:
            return None

        return cls(data['position'], User.parse(data['user']), data.get('score'))
