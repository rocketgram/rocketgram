# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, List, Optional

from .user import User


@dataclass(frozen=True)
class RichText:
    """\
    Represents RichText and its supported object variants:
    https://core.telegram.org/bots/api#richtext
    """

    @classmethod
    def parse(cls, data: Any) -> Any:
        if isinstance(data, str):
            return data
        if isinstance(data, list):
            return [cls.parse(d) for d in data]
        if data is None:
            return None

        rich_text_class = _RICH_TEXT_CLASSES.get(data.get('type'))
        if rich_text_class is None:
            return None
        return rich_text_class.parse(data)


@dataclass(frozen=True)
class _TextRichText(RichText):
    text: Any

    @classmethod
    def parse(cls, data: dict):
        return cls(RichText.parse(data['text']))


@dataclass(frozen=True)
class RichTextBold(_TextRichText):
    type: str = field(init=False, default='bold')


@dataclass(frozen=True)
class RichTextItalic(_TextRichText):
    type: str = field(init=False, default='italic')


@dataclass(frozen=True)
class RichTextUnderline(_TextRichText):
    type: str = field(init=False, default='underline')


@dataclass(frozen=True)
class RichTextStrikethrough(_TextRichText):
    type: str = field(init=False, default='strikethrough')


@dataclass(frozen=True)
class RichTextSpoiler(_TextRichText):
    type: str = field(init=False, default='spoiler')


@dataclass(frozen=True)
class RichTextSubscript(_TextRichText):
    type: str = field(init=False, default='subscript')


@dataclass(frozen=True)
class RichTextSuperscript(_TextRichText):
    type: str = field(init=False, default='superscript')


@dataclass(frozen=True)
class RichTextMarked(_TextRichText):
    type: str = field(init=False, default='marked')


@dataclass(frozen=True)
class RichTextCode(_TextRichText):
    type: str = field(init=False, default='code')


@dataclass(frozen=True)
class RichTextDateTime(RichText):
    text: Any
    unix_time: datetime
    date_time_format: str
    type: str = field(init=False, default='date_time')

    @classmethod
    def parse(cls, data: dict) -> 'RichTextDateTime':
        return cls(
            RichText.parse(data['text']),
            datetime.fromtimestamp(data['unix_time'], tz=timezone.utc),
            data['date_time_format'],
        )


@dataclass(frozen=True)
class RichTextTextMention(RichText):
    text: Any
    user: User
    type: str = field(init=False, default='text_mention')

    @classmethod
    def parse(cls, data: dict) -> 'RichTextTextMention':
        return cls(RichText.parse(data['text']), User.parse(data['user']))


@dataclass(frozen=True)
class RichTextCustomEmoji(RichText):
    custom_emoji_id: str
    alternative_text: str
    type: str = field(init=False, default='custom_emoji')

    @classmethod
    def parse(cls, data: dict) -> 'RichTextCustomEmoji':
        return cls(data['custom_emoji_id'], data['alternative_text'])


@dataclass(frozen=True)
class RichTextMathematicalExpression(RichText):
    expression: str
    type: str = field(init=False, default='mathematical_expression')

    @classmethod
    def parse(cls, data: dict) -> 'RichTextMathematicalExpression':
        return cls(data['expression'])


@dataclass(frozen=True)
class RichTextUrl(RichText):
    text: Any
    url: str
    type: str = field(init=False, default='url')

    @classmethod
    def parse(cls, data: dict) -> 'RichTextUrl':
        return cls(RichText.parse(data['text']), data['url'])


@dataclass(frozen=True)
class RichTextEmailAddress(RichText):
    text: Any
    email_address: str
    type: str = field(init=False, default='email_address')

    @classmethod
    def parse(cls, data: dict) -> 'RichTextEmailAddress':
        return cls(RichText.parse(data['text']), data['email_address'])


@dataclass(frozen=True)
class RichTextPhoneNumber(RichText):
    text: Any
    phone_number: str
    type: str = field(init=False, default='phone_number')

    @classmethod
    def parse(cls, data: dict) -> 'RichTextPhoneNumber':
        return cls(RichText.parse(data['text']), data['phone_number'])


@dataclass(frozen=True)
class RichTextBankCardNumber(RichText):
    text: Any
    bank_card_number: str
    type: str = field(init=False, default='bank_card_number')

    @classmethod
    def parse(cls, data: dict) -> 'RichTextBankCardNumber':
        return cls(RichText.parse(data['text']), data['bank_card_number'])


@dataclass(frozen=True)
class RichTextMention(RichText):
    text: Any
    username: str
    type: str = field(init=False, default='mention')

    @classmethod
    def parse(cls, data: dict) -> 'RichTextMention':
        return cls(RichText.parse(data['text']), data['username'])


@dataclass(frozen=True)
class RichTextHashtag(RichText):
    text: Any
    hashtag: str
    type: str = field(init=False, default='hashtag')

    @classmethod
    def parse(cls, data: dict) -> 'RichTextHashtag':
        return cls(RichText.parse(data['text']), data['hashtag'])


@dataclass(frozen=True)
class RichTextCashtag(RichText):
    text: Any
    cashtag: str
    type: str = field(init=False, default='cashtag')

    @classmethod
    def parse(cls, data: dict) -> 'RichTextCashtag':
        return cls(RichText.parse(data['text']), data['cashtag'])


@dataclass(frozen=True)
class RichTextBotCommand(RichText):
    text: Any
    bot_command: str
    type: str = field(init=False, default='bot_command')

    @classmethod
    def parse(cls, data: dict) -> 'RichTextBotCommand':
        return cls(RichText.parse(data['text']), data['bot_command'])


@dataclass(frozen=True)
class RichTextAnchor(RichText):
    name: str
    type: str = field(init=False, default='anchor')

    @classmethod
    def parse(cls, data: dict) -> 'RichTextAnchor':
        return cls(data['name'])


@dataclass(frozen=True)
class RichTextAnchorLink(RichText):
    text: Any
    anchor_name: str
    type: str = field(init=False, default='anchor_link')

    @classmethod
    def parse(cls, data: dict) -> 'RichTextAnchorLink':
        return cls(RichText.parse(data['text']), data['anchor_name'])


@dataclass(frozen=True)
class RichTextReference(RichText):
    text: Any
    name: str
    type: str = field(init=False, default='reference')

    @classmethod
    def parse(cls, data: dict) -> 'RichTextReference':
        return cls(RichText.parse(data['text']), data['name'])


@dataclass(frozen=True)
class RichTextReferenceLink(RichText):
    text: Any
    reference_name: str
    type: str = field(init=False, default='reference_link')

    @classmethod
    def parse(cls, data: dict) -> 'RichTextReferenceLink':
        return cls(RichText.parse(data['text']), data['reference_name'])


_RICH_TEXT_CLASSES = {
    'bold': RichTextBold,
    'italic': RichTextItalic,
    'underline': RichTextUnderline,
    'strikethrough': RichTextStrikethrough,
    'spoiler': RichTextSpoiler,
    'date_time': RichTextDateTime,
    'text_mention': RichTextTextMention,
    'subscript': RichTextSubscript,
    'superscript': RichTextSuperscript,
    'marked': RichTextMarked,
    'code': RichTextCode,
    'custom_emoji': RichTextCustomEmoji,
    'mathematical_expression': RichTextMathematicalExpression,
    'url': RichTextUrl,
    'email_address': RichTextEmailAddress,
    'phone_number': RichTextPhoneNumber,
    'bank_card_number': RichTextBankCardNumber,
    'mention': RichTextMention,
    'hashtag': RichTextHashtag,
    'cashtag': RichTextCashtag,
    'bot_command': RichTextBotCommand,
    'anchor': RichTextAnchor,
    'anchor_link': RichTextAnchorLink,
    'reference': RichTextReference,
    'reference_link': RichTextReferenceLink,
}
