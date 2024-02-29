# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, Optional, List

from .animation import Animation
from .audio import Audio
from .chat import Chat
from .chat_boost_added import ChatBoostAdded
from .chat_shared import ChatShared
from .contact import Contact
from .dice import Dice
from .document import Document
from .external_reply_info import ExternalReplyInfo
from .forum_topic_closed import ForumTopicClosed
from .forum_topic_created import ForumTopicCreated
from .forum_topic_edited import ForumTopicEdited
from .forum_topic_reopened import ForumTopicReopened
from .game import Game
from .general_forum_topic_hidden import GeneralForumTopicHidden
from .general_forum_topic_unhidden import GeneralForumTopicUnhidden
from .giveaway import Giveaway
from .giveaway_completed import GiveawayCompleted
from .giveaway_created import GiveawayCreated
from .giveaway_winners import GiveawayWinners
from .inline_keyboard_markup import InlineKeyboardMarkup
from .invoice import Invoice
from .link_preview_options import LinkPreviewOptions
from .location import Location
from .message_auto_delete_timer_changed import MessageAutoDeleteTimerChanged
from .message_entity import MessageEntity
from .message_origin import MessageOrigin
from .message_type import MessageType
from .passport_data import PassportData
from .photo_size import PhotoSize
from .poll import Poll
from .proximity_alert_triggered import ProximityAlertTriggered
from .sticker import Sticker
from .story import Story
from .successful_payment import SuccessfulPayment
from .text_quote import TextQuote
from .user import User
from .user_shared import UserShared
from .venue import Venue
from .video import Video
from .video_chat_ended import VideoChatEnded
from .video_chat_participants_invited import VideoChatParticipantsInvited
from .video_chat_scheduled import VideoChatScheduled
from .video_chat_started import VideoChatStarted
from .video_note import VideoNote
from .voice import Voice
from .web_app_data import WebAppData
from .write_access_allowed import WriteAccessAllowed


@dataclass(frozen=True)
class Message:
    """\
    Represents Message object:
    https://core.telegram.org/bots/api#message

    Differences in field names:
    from -> user

    Additional fields:
    type
    """

    type: MessageType

    message_id: int
    message_thread_id: Optional[int]
    user: Optional[User]
    sender_chat: Optional[Chat]
    sender_boost_count: Optional[int]
    date: datetime
    chat: Chat
    forward_origin: Optional[MessageOrigin]
    is_topic_message: Optional[bool]
    is_automatic_forward: Optional[bool]
    reply_to_message: Optional['Message']
    external_reply: Optional[ExternalReplyInfo]
    quote: Optional[TextQuote]
    reply_to_story: Optional[Story]
    via_bot: Optional[User]
    edit_date: Optional[datetime]
    has_protected_content: Optional[bool]
    media_group_id: Optional[str]
    author_signature: Optional[str]

    text: Optional[str]
    entities: Optional[List[MessageEntity]]

    link_preview_options: Optional[LinkPreviewOptions]

    animation: Optional[Animation]
    audio: Optional[Audio]
    document: Optional[Document]
    photo: Optional[List[PhotoSize]]
    sticker: Optional[Sticker]
    story: Optional[Story]
    video: Optional[Video]
    video_note: Optional[VideoNote]
    voice: Optional[Voice]

    caption: Optional[str]
    caption_entities: Optional[List[MessageEntity]]

    has_media_spoiler: Optional[bool]

    contact: Optional[Contact]
    dice: Optional[Dice]
    game: Optional[Game]
    poll: Optional[Poll]
    venue: Optional[Venue]
    location: Optional[Location]

    new_chat_members: Optional[List[User]]
    left_chat_member: Optional[User]

    new_chat_title: Optional[str]

    new_chat_photo: Optional[List[PhotoSize]]
    delete_chat_photo: Optional[bool]

    group_chat_created: Optional[bool]
    supergroup_chat_created: Optional[bool]
    channel_chat_created: Optional[bool]

    message_auto_delete_timer_changed: Optional[MessageAutoDeleteTimerChanged]

    migrate_to_chat_id: Optional[int]
    migrate_from_chat_id: Optional[int]

    pinned_message: Optional['Message']

    invoice: Optional[Invoice]
    successful_payment: Optional[SuccessfulPayment]

    user_shared: Optional[UserShared]
    chat_shared: Optional[ChatShared]

    connected_website: Optional[str]

    write_access_allowed: Optional[WriteAccessAllowed]

    passport_data: Optional[PassportData]

    proximity_alert_triggered: Optional[ProximityAlertTriggered]

    boost_added: Optional[ChatBoostAdded]

    forum_topic_created: Optional[ForumTopicCreated]
    forum_topic_edited: Optional[ForumTopicEdited]
    forum_topic_closed: Optional[ForumTopicClosed]
    forum_topic_reopened: Optional[ForumTopicReopened]

    general_forum_topic_hidden: Optional[GeneralForumTopicHidden]
    general_forum_topic_unhidden: Optional[GeneralForumTopicUnhidden]

    giveaway_created: Optional[GiveawayCreated]
    giveaway: Optional[Giveaway]
    giveaway_winners: Optional[GiveawayWinners]
    giveaway_completed: Optional[GiveawayCompleted]

    video_chat_scheduled: Optional[VideoChatScheduled]
    video_chat_started: Optional[VideoChatStarted]
    video_chat_ended: Optional[VideoChatEnded]
    video_chat_participants_invited: Optional[VideoChatParticipantsInvited]

    web_app_data: Optional[WebAppData]

    reply_markup: Optional[InlineKeyboardMarkup]

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['Message']:
        if data is None:
            return None

        message_id = data['message_id']
        message_thread_id = data.get('message_thread_id')
        user = User.parse(data.get('from'))
        sender_chat = Chat.parse(data.get('sender_chat'))
        sender_boost_count = data.get('sender_boost_count')
        date = datetime.fromtimestamp(data['date'], tz=timezone.utc)
        chat = Chat.parse(data["chat"])
        forward_origin = MessageOrigin.parse(data.get('forward_origin'))
        is_topic_message = data.get('is_topic_message')
        is_automatic_forward = data.get('is_automatic_forward')
        reply_to_message = Message.parse(data.get('reply_to_message'))
        external_reply = ExternalReplyInfo.parse(data.get('external_reply'))
        quote = TextQuote.parse(data.get('quote'))
        reply_to_story = Story.parse(data.get('reply_to_story'))
        via_bot = User.parse(data.get('via_bot'))
        edit_date = datetime.fromtimestamp(data['edit_date'], tz=timezone.utc) if 'edit_date' in data else None
        has_protected_content = data.get('has_protected_content')
        media_group_id = data.get('media_group_id')
        author_signature = data.get('author_signature')

        text = data.get('text')
        entities = [MessageEntity.parse(d) for d in data['entities']] if 'entities' in data else None

        link_preview_options = LinkPreviewOptions.parse(data.get('link_preview_options'))

        animation = Animation.parse(data.get('animation'))
        audio = Audio.parse(data.get('audio'))
        document = Document.parse(data.get('document'))
        if animation is not None:
            document = None
        photo = [PhotoSize.parse(d) for d in data['photo']] if 'photo' in data else None
        sticker = Sticker.parse(data.get('sticker'))
        story = Story.parse(data.get('story'))
        video = Video.parse(data.get('video'))
        video_note = VideoNote.parse(data.get('video_note'))
        voice = Voice.parse(data.get('voice'))

        caption = data.get('caption')
        caption_entities = [MessageEntity.parse(d) for d in data['caption_entities']] \
            if 'caption_entities' in data else None

        has_media_spoiler = data.get('has_media_spoiler')

        contact = Contact.parse(data.get('contact'))
        dice = Dice.parse(data.get('dice'))
        game = Game.parse(data.get('game'))
        poll = Poll.parse(data.get('poll'))
        venue = Venue.parse(data.get('venue'))
        location = Location.parse(data.get('location'))

        new_chat_members = [User.parse(d) for d in data['new_chat_members']] \
            if 'new_chat_members' in data else None
        left_chat_member = User.parse(data.get('left_chat_member'))

        new_chat_title = data.get('new_chat_title')

        new_chat_photo = [PhotoSize.parse(d) for d in data['new_chat_photo']] if 'new_chat_photo' in data else None
        delete_chat_photo = data.get('delete_chat_photo')

        group_chat_created = data.get('group_chat_created')
        supergroup_chat_created = data.get('supergroup_chat_created')
        channel_chat_created = data.get('channel_chat_created')

        message_auto_delete_timer_changed = MessageAutoDeleteTimerChanged.parse(
            data.get('message_auto_delete_timer_changed'))

        migrate_to_chat_id = data.get('migrate_to_chat_id')
        migrate_from_chat_id = data.get('migrate_from_chat_id')

        pinned_message = Message.parse(data.get('pinned_message'))

        invoice = Invoice.parse(data.get('invoice'))
        successful_payment = SuccessfulPayment.parse(data.get('successful_payment'))

        user_shared = UserShared.parse(data.get('user_shared'))
        chat_shared = ChatShared.parse(data.get('chat_shared'))

        connected_website = data.get('connected_website')

        write_access_allowed = WriteAccessAllowed.parse(data.get('write_access_allowed'))

        passport_data = PassportData.parse(data.get('passport_data'))

        proximity_alert_triggered = ProximityAlertTriggered.parse(data.get('proximity_alert_triggered'))

        boost_added = ChatBoostAdded.parse(data.get('boost_added'))

        forum_topic_created = ForumTopicCreated.parse(data.get('forum_topic_created'))
        forum_topic_edited = ForumTopicCreated.parse(data.get('forum_topic_edited'))
        forum_topic_closed = ForumTopicClosed.parse(data.get('forum_topic_closed'))
        forum_topic_reopened = ForumTopicReopened.parse(data.get('forum_topic_reopened'))

        general_forum_topic_hidden = GeneralForumTopicHidden.parse(data.get('general_forum_topic_hidden'))
        general_forum_topic_unhidden = GeneralForumTopicUnhidden.parse(data.get('general_forum_topic_unhidden'))

        giveaway_created = GiveawayCreated.parse(data.get('giveaway_created'))
        giveaway = Giveaway.parse(data.get('giveaway'))
        giveaway_winners = GiveawayWinners.parse(data.get('giveaway_winners'))
        giveaway_completed = GiveawayCompleted.parse(data.get('giveaway_completed'))

        video_chat_scheduled = VideoChatScheduled.parse(data.get('video_chat_scheduled'))
        video_chat_started = VideoChatStarted.parse(data.get('video_chat_started'))
        video_chat_ended = VideoChatEnded.parse(data.get('video_chat_ended'))
        video_chat_participants_invited = VideoChatParticipantsInvited.parse(
            data.get('video_chat_participants_invited'))

        web_app_data = WebAppData.parse(data.get('web_app_data'))

        reply_markup = InlineKeyboardMarkup.parse(data.get('reply_markup'))

        message_type = MessageType.unknown

        if text:
            message_type = MessageType.text
        elif audio:
            message_type = MessageType.audio
        elif document:
            message_type = MessageType.document
        elif animation:
            message_type = MessageType.animation
        elif game:
            message_type = MessageType.game
        elif photo:
            message_type = MessageType.photo
        elif sticker:
            message_type = MessageType.sticker
        elif story:
            message_type = MessageType.story
        elif video:
            message_type = MessageType.video
        elif voice:
            message_type = MessageType.voice
        elif video_note:
            message_type = MessageType.video_note
        elif new_chat_members:
            message_type = MessageType.new_chat_members
        elif contact:
            message_type = MessageType.contact
        elif location:
            message_type = MessageType.location
        elif venue:
            message_type = MessageType.venue
        elif poll:
            message_type = MessageType.poll
        elif dice:
            message_type = MessageType.dice
        elif left_chat_member:
            message_type = MessageType.left_chat_member
        elif new_chat_title:
            message_type = MessageType.new_chat_title
        elif new_chat_photo:
            message_type = MessageType.new_chat_photo
        elif delete_chat_photo:
            message_type = MessageType.delete_chat_photo
        elif group_chat_created:
            message_type = MessageType.group_chat_created
        elif supergroup_chat_created:
            message_type = MessageType.supergroup_chat_created
        elif channel_chat_created:
            message_type = MessageType.channel_chat_created
        elif migrate_to_chat_id:
            message_type = MessageType.migrate_to_chat_id
        elif migrate_from_chat_id:
            message_type = MessageType.migrate_from_chat_id
        elif pinned_message:
            message_type = MessageType.pinned_message
        elif invoice:
            message_type = MessageType.invoice
        elif successful_payment:
            message_type = MessageType.successful_payment
        elif user_shared:
            message_type = MessageType.user_shared
        elif chat_shared:
            message_type = MessageType.chat_shared
        elif connected_website:
            message_type = MessageType.connected_website
        elif write_access_allowed:
            message_type = MessageType.write_access_allowed
        elif passport_data:
            message_type = MessageType.passport_data
        elif proximity_alert_triggered:
            message_type = MessageType.proximity_alert_triggered
        elif boost_added:
            message_type = MessageType.boost_added
        elif forum_topic_created:
            message_type = MessageType.forum_topic_created
        elif forum_topic_edited:
            message_type = MessageType.forum_topic_edited
        elif forum_topic_closed:
            message_type = MessageType.forum_topic_closed
        elif forum_topic_reopened:
            message_type = MessageType.forum_topic_reopened
        elif general_forum_topic_hidden:
            message_type = MessageType.general_forum_topic_hidden
        elif general_forum_topic_unhidden:
            message_type = MessageType.general_forum_topic_unhidden
        elif giveaway_created:
            message_type = MessageType.giveaway_created
        elif giveaway:
            message_type = MessageType.giveaway
        elif giveaway_winners:
            message_type = MessageType.giveaway_winners
        elif giveaway_completed:
            message_type = MessageType.giveaway_completed
        elif video_chat_scheduled:
            message_type = MessageType.video_chat_scheduled
        elif video_chat_started:
            message_type = MessageType.video_chat_started
        elif video_chat_ended:
            message_type = MessageType.video_chat_ended
        elif video_chat_participants_invited:
            message_type = MessageType.video_chat_participants_invited
        elif message_auto_delete_timer_changed:
            message_type = MessageType.message_auto_delete_timer_changed
        elif web_app_data:
            message_type = MessageType.web_app_data

        return cls(
            message_type,
            message_id,
            message_thread_id,
            user,
            sender_chat,
            sender_boost_count,
            date,
            chat,
            forward_origin,
            is_topic_message,
            is_automatic_forward,
            reply_to_message,
            external_reply,
            quote,
            reply_to_story,
            via_bot,
            edit_date,
            has_protected_content,
            media_group_id,
            author_signature,
            text,
            entities,
            link_preview_options,
            animation,
            audio,
            document,
            photo,
            sticker,
            story,
            video,
            video_note,
            voice,
            caption,
            caption_entities,
            has_media_spoiler,
            contact,
            dice,
            game,
            poll,
            venue,
            location,
            new_chat_members,
            left_chat_member,
            new_chat_title,
            new_chat_photo,
            delete_chat_photo,
            group_chat_created,
            supergroup_chat_created,
            channel_chat_created,
            message_auto_delete_timer_changed,
            migrate_to_chat_id,
            migrate_from_chat_id,
            pinned_message,
            invoice,
            successful_payment,
            user_shared,
            chat_shared,
            connected_website,
            write_access_allowed,
            passport_data,
            proximity_alert_triggered,
            boost_added,
            forum_topic_created,
            forum_topic_edited,
            forum_topic_closed,
            forum_topic_reopened,
            general_forum_topic_hidden,
            general_forum_topic_unhidden,
            giveaway_created,
            giveaway,
            giveaway_winners,
            giveaway_completed,
            video_chat_scheduled,
            video_chat_started,
            video_chat_ended,
            video_chat_participants_invited,
            web_app_data,
            reply_markup
        )
