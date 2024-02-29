# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from . import animation
from . import audio
from . import chat
from . import contact
from . import dice
from . import document
from . import game
from . import giveaway
from . import giveaway_winners
from . import invoice
from . import link_preview_options
from . import location
from . import message_origin
from . import message_type
from . import photo_size
from . import poll
from . import sticker
from . import story
from . import venue
from . import video
from . import video_note
from . import voice


@dataclass(frozen=True)
class ExternalReplyInfo:
    """\
    Represents ExternalReplyInfo object:
    https://core.telegram.org/bots/api#externalreplyinfo

    Additional fields:
    type
    """

    type: 'message_type.MessageType'

    origin: 'message_origin.MessageOrigin'
    chat: Optional['chat.Chat']
    message_id: Optional[int]
    link_preview_options: Optional['link_preview_options.LinkPreviewOptions']
    animation: Optional['animation.Animation']
    audio: Optional['audio.Audio']
    document: Optional['document.Document']
    photo: Optional[List['photo_size.PhotoSize']]
    sticker: Optional['sticker.Sticker']
    story: Optional['story.Story']
    video: Optional['video.Video']
    video_note: Optional['video_note.VideoNote']
    voice: Optional['voice.Voice']
    has_media_spoiler: Optional[bool]
    contact: Optional['contact.Contact']
    dice: Optional['dice.Dice']
    game: Optional['game.Game']
    giveaway: Optional['giveaway.Giveaway']
    giveaway_winners: Optional['giveaway_winners.GiveawayWinners']
    invoice: Optional['invoice.Invoice']
    location: Optional['location.Location']
    poll: Optional['poll.Poll']
    venue: Optional['venue.Venue']

    @classmethod
    def parse(cls, data: dict) -> Optional['ExternalReplyInfo']:
        if data is None:
            return None

        origin_ = message_origin.MessageOrigin.parse(data['origin'])
        chat_ = chat.Chat.parse(data.get('chat'))
        message_id_ = data.get('message_id')
        link_preview_options_ = link_preview_options.LinkPreviewOptions.parse(data.get('link_preview_options'))
        animation_ = animation.Animation.parse(data.get('animation'))
        audio_ = audio.Audio.parse(data.get('audio'))
        document_ = document.Document.parse(data.get('document'))
        photo_size_ = [photo_size.PhotoSize.parse(e) for e in data['photo']] if 'photo' in data else None
        sticker_ = sticker.Sticker.parse(data.get('sticker'))
        story_ = story.Story.parse(data.get('story'))
        video_ = video.Video.parse(data.get('video'))
        video_note_ = video_note.VideoNote.parse(data.get('video_note'))
        voice_ = voice.Voice.parse(data.get('voice'))
        has_media_spoiler_ = data.get('has_media_spoiler')
        contact_ = contact.Contact.parse(data.get('contact'))
        dice_ = dice.Dice.parse(data.get('dice'))
        game_ = game.Game.parse(data.get('game'))
        giveaway_ = giveaway.Giveaway.parse(data.get('giveaway'))
        giveaway_winners_ = giveaway_winners.GiveawayWinners.parse(data.get('giveaway_winners'))
        invoice_ = invoice.Invoice.parse(data.get('invoice'))
        location_ = location.Location.parse(data.get('location'))
        poll_ = poll.Poll.parse(data.get('poll'))
        venue_ = venue.Venue.parse(data.get('venue'))

        message_type_ = message_type.MessageType.unknown

        if audio_:
            message_type_ = message_type.MessageType.audio
        elif document_:
            message_type_ = message_type.MessageType.document
        elif animation_:
            message_type_ = message_type.MessageType.animation
        elif game_:
            message_type_ = message_type.MessageType.game
        elif photo_size_:
            message_type_ = message_type.MessageType.photo
        elif sticker_:
            message_type_ = message_type.MessageType.sticker
        elif story_:
            message_type_ = message_type.MessageType.story
        elif video_:
            message_type_ = message_type.MessageType.video
        elif voice_:
            message_type_ = message_type.MessageType.voice
        elif video_note_:
            message_type_ = message_type.MessageType.video_note
        elif contact_:
            message_type_ = message_type.MessageType.contact
        elif location_:
            message_type_ = message_type.MessageType.location
        elif venue_:
            message_type_ = message_type.MessageType.venue
        elif poll_:
            message_type_ = message_type.MessageType.poll
        elif dice_:
            message_type_ = message_type.MessageType.dice
        elif invoice_:
            message_type_ = message_type.MessageType.invoice
        elif giveaway_:
            message_type_ = message_type.MessageType.giveaway
        elif giveaway_winners_:
            message_type_ = message_type.MessageType.giveaway_winners

        return cls(
            message_type_,
            origin_,
            chat_,
            message_id_,
            link_preview_options_,
            animation_,
            audio_,
            document_,
            photo_size_,
            sticker_,
            story_,
            video_,
            video_note_,
            voice_,
            has_media_spoiler_,
            contact_,
            dice_,
            game_,
            giveaway_,
            giveaway_winners_,
            invoice_,
            location_,
            poll_,
            venue_
        )
