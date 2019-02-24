# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import enum


class UpdateType(enum.Enum):
    message = enum.auto()
    edited_message = enum.auto()
    channel_post = enum.auto()
    edited_channel_post = enum.auto()
    inline_query = enum.auto()
    chosen_inline_result = enum.auto()
    callback_query = enum.auto()
    shipping_query = enum.auto()
    pre_checkout_query = enum.auto()


class Update:
    """https://core.telegram.org/bots/api#update"""

    def __init__(self, data: dict):
        self.raw = data
        self.update_id = data['update_id']
        self.update_type = None

        if 'message' in data:
            self.message = Message(data['message'])
            self.update_type = UpdateType.message
        elif 'edited_message' in data:
            self.edited_message = Message(data['edited_message'])
            self.update_type = UpdateType.edited_message
        elif 'channel_post' in data:
            self.channel_post = Message(data['channel_post'])
            self.update_type = UpdateType.channel_post
        elif 'edited_channel_post' in data:
            self.edited_channel_post = Message(data['edited_channel_post'])
            self.update_type = UpdateType.edited_channel_post
        elif 'inline_query' in data:
            self.inline_query = InlineQuery(data['inline_query'])
            self.update_type = UpdateType.inline_query
        elif 'chosen_inline_result' in data:
            self.chosen_inline_result = ChosenInlineResult(data['chosen_inline_result'])
            self.update_type = UpdateType.chosen_inline_result
        elif 'callback_query' in data:
            self.callback_query = CallbackQuery(data['callback_query'])
            self.update_type = UpdateType.callback_query
        elif 'shipping_query' in data:
            self.shipping_query = ShippingQuery(data['shipping_query'])
            self.update_type = UpdateType.shipping_query
        elif 'pre_checkout_query' in data:
            self.pre_checkout_query = PreCheckoutQuery(data['pre_checkout_query'])
            self.update_type = UpdateType.pre_checkout_query


class WebhookInfo:
    """https://core.telegram.org/bots/api#getwebhookinfo"""

    def __init__(self, data: dict):
        self.url = data['url']
        self.has_custom_certificate = data['has_custom_certificate']
        self.pending_update_count = data['pending_update_count']
        self.last_error_date = data.get('last_error_date')
        self.last_error_message = data.get('last_error_message')
        self.max_connections = data.get('max_connections')
        self.allowed_updates = data.get('allowed_updates')


class User:
    """https://core.telegram.org/bots/api#user"""

    def __init__(self, data: dict):
        self.user_id = data['id']
        self.first_name = data['first_name']
        self.last_name = data.get('last_name')
        self.username = data.get('username')
        self.language_code = data.get('language_code')


class ChatType(enum.Enum):
    private = enum.auto()
    group = enum.auto()
    supergroup = enum.auto()
    channel = enum.auto()


class Chat:
    """https://core.telegram.org/bots/api#chat"""

    def __init__(self, data: dict):
        self.chat_id = data['id']

        if data['type'] == 'private':
            self._type = ChatType.private
        elif data['type'] == 'group':
            self._type = ChatType.group
        elif data['type'] == 'supergroup':
            self._type = ChatType.supergroup
        elif data['type'] == 'channel':
            self._type = ChatType.channel
        else:
            self._type = None

        self.title = data.get('title')
        self.username = data.get('username')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.all_members_are_administrators = data.get('all_members_are_administrators')


class MessageType(enum.Enum):
    text = enum.auto()
    audio = enum.auto()
    document = enum.auto()
    game = enum.auto()
    photo = enum.auto()
    sticker = enum.auto()
    video = enum.auto()
    voice = enum.auto()
    video_note = enum.auto()
    new_chat_members = enum.auto()
    contact = enum.auto()
    location = enum.auto()
    venue = enum.auto()
    left_chat_member = enum.auto()
    new_chat_title = enum.auto()
    new_chat_photo = enum.auto()
    delete_chat_photo = enum.auto()
    group_chat_created = enum.auto()
    supergroup_chat_created = enum.auto()
    channel_chat_created = enum.auto()
    migrate_to_chat_id = enum.auto()
    migrate_from_chat_id = enum.auto()
    pinned_message = enum.auto()
    invoice = enum.auto()
    successful_payment = enum.auto()


class Message:
    """https://core.telegram.org/bots/api#message"""

    def __init__(self, data: dict):
        self.message_id = data['message_id']
        self.user = User(data['from']) if data.get('from') is not None else None
        self.date = data['date']
        self.chat = Chat(data['chat'])
        self.forward_from = User(data['forward_from']) if data.get('forward_from') is not None else None
        self.forward_from_chat = Chat(data['forward_from_chat']) if data.get('forward_from_chat') is not None else None
        self.forward_from_message_id = data.get('forward_from_message_id')
        self.forward_date = data.get('forward_date')
        self.reply_to_message = Message(data['reply_to_message']) if data.get('reply_to_message') is not None else None
        self.edit_date = data.get('edit_date')
        self.text = data.get('text')

        if data.get('entities') is not None:
            self.entities = []
            for p in data.get('entities'):
                self.entities.append(MessageEntity(p))
        else:
            self.entities = None

        self.audio = Audio(data['audio']) if data.get('audio') is not None else None
        self.document = Document(data['document']) if data.get('document') is not None else None
        self.game = Game(data['game']) if data.get('game') is not None else None

        if data.get('photo') is not None:
            self.photo = []
            for p in data.get('photo'):
                self.photo.append(PhotoSize(p))
        else:
            self.photo = None

        self.sticker = Sticker(data['sticker']) if data.get('sticker') is not None else None
        self.video = Video(data['video']) if data.get('video') is not None else None
        self.voice = Voice(data['voice']) if data.get('voice') is not None else None
        self.video_note = VideoNote(data['video_note']) if data.get('video_note') is not None else None

        if data.get('new_chat_members') is not None:
            self.new_chat_members = []
            for p in data.get('new_chat_members'):
                self.new_chat_members.append(User(p))
        else:
            self.new_chat_members = None

        self.caption = data.get('caption')
        self.contact = Contact(data['contact']) if data.get('contact') is not None else None
        self.location = Location(data['location']) if data.get('location') is not None else None
        self.venue = Venue(data['venue']) if data.get('venue') is not None else None
        self.left_chat_member = User(data['left_chat_member']) if data.get('left_chat_member') is not None else None
        self.new_chat_title = data.get('new_chat_title')

        if data.get('new_chat_photo') is not None:
            self.new_chat_photo = []
            for p in data.get('new_chat_photo'):
                self.new_chat_photo.append(PhotoSize(p))
        else:
            self.new_chat_photo = None

        self.delete_chat_photo = data.get('delete_chat_photo')
        self.group_chat_created = data.get('group_chat_created')
        self.supergroup_chat_created = data.get('supergroup_chat_created')
        self.channel_chat_created = data.get('channel_chat_created')
        self.migrate_to_chat_id = data.get('migrate_to_chat_id')
        self.migrate_from_chat_id = data.get('migrate_from_chat_id')
        self.pinned_message = Message(data['pinned_message']) if data.get('pinned_message') is not None else None
        self.invoice = Invoice(data['invoice']) if data.get('invoice') is not None else None
        self.successful_payment = SuccessfulPayment(data['successful_payment']) if data.get(
            'successful_payment') is not None else None

        self.message_type = None

        if self.text is not None:
            self.message_type = MessageType.text
        elif self.audio is not None:
            self.message_type = MessageType.audio
        elif self.document is not None:
            self.message_type = MessageType.document
        elif self.game is not None:
            self.message_type = MessageType.game
        elif self.photo is not None:
            self.message_type = MessageType.photo
        elif self.sticker is not None:
            self.message_type = MessageType.sticker
        elif self.video is not None:
            self.message_type = MessageType.video
        elif self.voice is not None:
            self.message_type = MessageType.voice
        elif self.video_note is not None:
            self.message_type = MessageType.video_note
        elif self.new_chat_members is not None:
            self.message_type = MessageType.new_chat_members
        elif self.contact is not None:
            self.message_type = MessageType.contact
        elif self.location is not None:
            self.message_type = MessageType.location
        elif self.venue is not None:
            self.message_type = MessageType.venue
        elif self.left_chat_member is not None:
            self.message_type = MessageType.left_chat_member
        elif self.new_chat_title is not None:
            self.message_type = MessageType.new_chat_title
        elif self.new_chat_photo is not None:
            self.message_type = MessageType.new_chat_photo
        elif self.delete_chat_photo is not None:
            self.message_type = MessageType.delete_chat_photo
        elif self.group_chat_created is not None:
            self.message_type = MessageType.group_chat_created
        elif self.supergroup_chat_created is not None:
            self.message_type = MessageType.supergroup_chat_created
        elif self.channel_chat_created is not None:
            self.message_type = MessageType.channel_chat_created
        elif self.migrate_to_chat_id is not None:
            self.message_type = MessageType.migrate_to_chat_id
        elif self.migrate_from_chat_id is not None:
            self.message_type = MessageType.migrate_from_chat_id
        elif self.pinned_message is not None:
            self.message_type = MessageType.pinned_message
        elif self.invoice is not None:
            self.message_type = MessageType.invoice
        elif self.successful_payment is not None:
            self.message_type = MessageType.successful_payment


class MessageEntity:
    """https://core.telegram.org/bots/api#messageentity"""

    def __init__(self, data: dict):
        self._type = data['type']
        self.offset = data['offset']
        self.length = data['length']
        self.url = data.get('url')
        self.user = User(data['user']) if data.get('user') is not None else None


class PhotoSize:
    """https://core.telegram.org/bots/api#photosize"""

    def __init__(self, data: dict):
        self.file_id = data['file_id']
        self.width = data['width']
        self.height = data['height']
        self.file_size = data.get('file_size')


class Audio:
    """https://core.telegram.org/bots/api#audio"""

    def __init__(self, data: dict):
        self.file_id = data['file_id']
        self.duration = data['duration']
        self.performer = data.get('performer')
        self.title = data.get('title')
        self.mime_type = data.get('mime_type')
        self.file_size = data.get('file_size')


class Document:
    """https://core.telegram.org/bots/api#document"""

    def __init__(self, data: dict):
        self.file_id = data['file_id']
        self.thumb = PhotoSize(data['thumb']) if data.get('thumb') is not None else None
        self.file_name = data.get('file_name')
        self.mime_type = data.get('mime_type')
        self.file_size = data.get('file_size')


class Sticker:
    """https://core.telegram.org/bots/api#sticker"""

    def __init__(self, data: dict):
        self.file_id = data['file_id']
        self.width = data['width']
        self.height = data['height']
        self.thumb = PhotoSize(data['thumb']) if data.get('thumb') is not None else None
        self.emoji = data.get('emoji')
        self.file_size = data.get('file_size')


class Video:
    """https://core.telegram.org/bots/api#video"""

    def __init__(self, data: dict):
        self.file_id = data['file_id']
        self.width = data['width']
        self.height = data['height']
        self.duration = data['duration']
        self.thumb = PhotoSize(data['thumb']) if data.get('thumb') is not None else None
        self.mime_type = data.get('mime_type')
        self.file_size = data.get('file_size')


class Voice:
    """https://core.telegram.org/bots/api#voice"""

    def __init__(self, data: dict):
        self.file_id = data['file_id']
        self.duration = data['duration']
        self.mime_type = data.get('mime_type')
        self.file_size = data.get('file_size')


class VideoNote:
    """https://core.telegram.org/bots/api#videonote"""

    def __init__(self, data: dict):
        self.file_id = data['file_id']
        self.length = int(data['length'])
        self.duration = int(data['duration'])
        self.thumb = PhotoSize(data['thumb']) if data.get('thumb') is not None else None
        self.file_size = data.get('file_size')


class Contact:
    """https://core.telegram.org/bots/api#contact"""

    def __init__(self, data):
        self.phone_number = data['phone_number']
        self.first_name = data['first_name']
        self.last_name = data.get('last_name')
        self.user_id = data.get('user_id')


class Location:
    """https://core.telegram.org/bots/api#location"""

    def __init__(self, data: dict):
        self.longitude = data['longitude']
        self.latitude = data['latitude']


class Venue:
    """https://core.telegram.org/bots/api#venue"""

    def __init__(self, data: dict):
        self.location = Location(data['location'])
        self.title = data['title']
        self.address = data['address']
        self.foursquare_id = data.get('foursquare_id')


class UserProfilePhotos:
    """https://core.telegram.org/bots/api#userprofilephotos"""

    def __init__(self, data: dict):
        self.total_count = data['total_count']
        self.photos = []
        for p in data['photos']:
            photo = []
            for i in p:
                photo.append(PhotoSize(i))
            self.photos.append(photo)


class File:
    """https://core.telegram.org/bots/api#file"""

    def __init__(self, data: dict):
        self.file_id = data['file_id']
        self.file_size = data.get('file_size')
        self.file_path = data.get('file_path')


class CallbackQuery:
    """https://core.telegram.org/bots/api#callbackquery"""

    def __init__(self, data: dict):
        self.query_id = data['id']
        self.user = User(data['from'])
        self.message = Message(data['message']) if data.get('message') is not None else None
        self.inline_message_id = data.get('inline_message_id')
        self.chat_instance = data['chat_instance']
        self.data = data['data']
        self.game_short_name = data.get('game_short_name')


class ChatMember:
    """https://core.telegram.org/bots/api#chatmember"""

    def __init__(self, data: dict):
        self.user = User(data['user'])
        self.status = data['status']


class ResponseParameters:
    """https://core.telegram.org/bots/api#responseparameters"""

    def __init__(self, data: dict):
        self.migrate_to_chat_id = data.get('migrate_to_chat_id')
        self.retry_after = data.get('retry_after')


class InlineQuery:
    """https://core.telegram.org/bots/api#inlinequery"""

    def __init__(self, data: dict):
        self.query_id = data['id']
        self.user = User(data['from'])
        self.location = Location(data['location']) if data.get('location') is not None else None
        self.query = data['query']
        self.offset = data.get('offset')


class ChosenInlineResult:
    """https://core.telegram.org/bots/api#choseninlineresult"""

    def __init__(self, data: dict):
        self.result_id = data['result_id']
        self.user = User(data['from'])
        self.location = Location(data['location']) if data.get('location') is not None else None
        self.inline_message_id = data.get('inline_message_id')
        self.query = data['query']


class LabeledPrice:
    """https://core.telegram.org/bots/api#labeledprice"""

    def __init__(self, data: dict):
        self.label = data['label']
        self.amount = data['amount']


class Invoice:
    """https://core.telegram.org/bots/api#invoice"""

    def __init__(self, data: dict):
        self.title = data['title']
        self.description = data['description']
        self.start_parameter = data['start_parameter']
        self.currency = data['currency']
        self.total_amount = data['total_amount']


class ShippingAddress:
    """https://core.telegram.org/bots/api#shippingaddress"""

    def __init__(self, data: dict):
        self.country_code = data['country_code']
        self.state = data['state']
        self.city = data['city']
        self.street_line1 = data['street_line1']
        self.street_line2 = data['street_line2']
        self.post_code = data['post_code']


class OrderInfo:
    """https://core.telegram.org/bots/api#orderinfo"""

    def __init__(self, data: dict):
        self.name = data.get('name')
        self.phone_number = data.get('phone_number')
        self.email = data.get('email')
        self.shipping_address = ShippingAddress(data['shipping_address']) if data.get(
            'shipping_address') is not None else None


class ShippingOption:
    """https://core.telegram.org/bots/api#shippingoption"""

    def __init__(self, data: dict):
        self.id = data['id']
        self.title = data['title']

        if data.get('prices') is not None:
            self.prices = []
            for p in data.get('prices'):
                self.prices.append(LabeledPrice(p))
        else:
            self.prices = None


class SuccessfulPayment:
    """https://core.telegram.org/bots/api#successfulpayment"""

    def __init__(self, data: dict):
        self.currency = data['currency']
        self.total_amount = data['total_amount']
        self.invoice_payload = data['invoice_payload']
        self.shipping_option_id = data.get('shipping_option_id')
        self.order_info = OrderInfo(data['order_info']) if data.get('order_info') is not None else None
        self.telegram_payment_charge_id = data['telegram_payment_charge_id']
        self.provider_payment_charge_id = data['provider_payment_charge_id']


class ShippingQuery:
    """https://core.telegram.org/bots/api#successfulpayment"""

    def __init__(self, data: dict):
        self.query_id = data['id']
        self.user = User(data['from'])
        self.invoice_payload = data['invoice_payload']
        self.shipping_address = ShippingAddress(data['shipping_address'])


class PreCheckoutQuery:
    """https://core.telegram.org/bots/api#precheckoutquery"""

    def __init__(self, data: dict):
        self.query_id = data['id']
        self.user = User(data['from'])
        self.currency = data['currency']
        self.total_amount = data['total_amount']
        self.invoice_payload = data['invoice_payload']
        self.shipping_option_id = data.get('shipping_option_id')
        self.order_info = OrderInfo(data['order_info']) if data.get('order_info') is not None else None


class Game:
    """https://core.telegram.org/bots/api#game"""

    def __init__(self, data: dict):
        self.title = data['title']
        self.description = data['description']

        if data.get('photo') is not None:
            self.photo = []
            for p in data.get('photo'):
                self.photo.append(PhotoSize(p))
        else:
            self.photo = None

        self.text = data.get('text')

        if data.get('text_entities') is not None:
            self.text_entities = []
            for p in data.get('text_entities'):
                self.text_entities.append(MessageEntity(p))
        else:
            self.text_entities = None

        self.animation = Animation(data['animation']) if data.get('animation') is not None else None


class Animation:
    """https://core.telegram.org/bots/api#animation"""

    def __init__(self, data: dict):
        self.file_id = data['file_id']
        self.thumb = PhotoSize(data['thumb']) if data.get('thumb') is not None else None
        self.file_name = data.get('file_name')
        self.mime_type = data.get('mime_type')
        self.file_size = data.get('file_size')


class GameHighScore:
    """https://core.telegram.org/bots/api#gamehighscore"""

    def __init__(self, data: dict):
        self.position = data['position']
        self.user = User(data['user'])
        self.score = data['score']


class Response:
    def __init__(self, data: dict, method: str):
        self.ok = data['ok']
        self.description = data.get('description')
        self.error_code = data.get('error_code')
        self.result_raw = data
        self.result = None

        if self.error_code:
            return

        if method is 'getMe':
            self.result = User(data['result'])
        elif method is 'getUpdates':
            self.result = list()
            for update in data['result']:
                self.result.append(Update(update))
        elif method is 'setWebhook':
            self.result = data['result']
        elif method is 'deleteWebhook':
            self.result = data['result']
        elif method is 'getWebhookInfo':
            self.result = WebhookInfo(data['result'])
        elif method is 'sendMessage':
            self.result = Message(data['result'])
        elif method is 'sendPhoto':
            self.result = Message(data['result'])
        elif method is 'sendAudio':
            self.result = Message(data['result'])
        elif method is 'sendDocument':
            self.result = Message(data['result'])
        elif method is 'sendSticker':
            self.result = Message(data['result'])
        elif method is 'sendVideo':
            self.result = Message(data['result'])
        elif method is 'sendVoice':
            self.result = Message(data['result'])
        elif method is 'sendVideoNote':
            self.result = Message(data['result'])
        elif method is 'sendLocation':
            self.result = Message(data['result'])
        elif method is 'sendVenue':
            self.result = Message(data['result'])
        elif method is 'sendContact':
            self.result = Message(data['result'])
        elif method is 'sendChatAction':
            self.result = data['result']
        elif method is 'getUserProfilePhotos':
            self.result = UserProfilePhotos(data['result'])
        elif method is 'getFile':
            self.result = File(data['result'])
        elif method is 'kickChatMember':
            self.result = data['result']
        elif method is 'leaveChat':
            self.result = data['result']
        elif method is 'unbanChatMember':
            self.result = data['result']
        elif method is 'getChat':
            self.result = Chat(data['result'])
        elif method is 'getChatAdministrators':
            self.result = list()
            for member in data['result']:
                self.result.append(ChatMember(member))
        elif method is 'getChatMember':
            self.result = ChatMember(data['result'])
        elif method is 'answerCallbackQuery':
            self.result = data['result']
        elif method is 'editMessageText':
            if data['result'] is True:
                self.result = data['result']
            else:
                self.result = Message(data['result'])
        elif method is 'editMessageCaption':
            if data['result'] is True:
                self.result = data['result']
            else:
                self.result = Message(data['result'])
        elif method is 'editMessageReplyMarkup':
            if data['result'] is True:
                self.result = data['result']
            else:
                self.result = Message(data['result'])
        elif method is 'answerInlineQuery':
            self.result = data['result']

        self.R = self.result

    def __repr__(self):
        return "Response: ok=%s, error_code=%s, description=%s" % (self.ok, self.error_code, self.description)
