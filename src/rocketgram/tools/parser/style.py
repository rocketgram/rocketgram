# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import re
from typing import Dict, Callable, Optional

from ... import MessageEntity
from ...api import EntityType


class Style:
    _STYLER_ATTR = '_styler'
    _stylers: Dict[EntityType, Callable[[MessageEntity, str], str]] = None

    @classmethod
    def styler(cls, entity_type: EntityType):
        def inner(f: Callable[[MessageEntity, str], str]):
            setattr(f, cls._STYLER_ATTR, entity_type)
            return f

        return inner

    def __init_subclass__(cls, **kwargs):
        stylers: Dict[EntityType, Callable] = {}

        for member_name in dir(cls):
            member = getattr(cls, member_name)
            entity_type = getattr(member, cls._STYLER_ATTR, None)
            if not entity_type:
                continue
            stylers[entity_type] = member

        cls._stylers = stylers

    @classmethod
    def get(cls, entity_type: Optional[EntityType]) -> Optional[Callable[[MessageEntity, str], str]]:
        return cls._stylers.get(entity_type)

    @classmethod
    def escape(cls, text: str) -> str:
        return text

    @classmethod
    def apply(cls, message_entity: Optional[MessageEntity], text: str) -> str:
        if not message_entity:
            return text
        styler = cls.get(message_entity.type)
        if not styler:
            return text
        return styler(message_entity, text)


class EmptyStyle(Style):
    pass


class HtmlStyle(Style):
    @classmethod
    def escape(cls, text: str) -> str:
        return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    @classmethod
    @Style.styler(EntityType.bold)
    def _bold(cls, _: MessageEntity, text: str) -> str:
        return f"<b>{text}</b>"

    @classmethod
    @Style.styler(EntityType.italic)
    def _italic(cls, _: MessageEntity, text: str) -> str:
        return f"<i>{text}</i>"

    @classmethod
    @Style.styler(EntityType.underline)
    def _underline(cls, _: MessageEntity, text: str) -> str:
        return f"<u>{text}</u>"

    @classmethod
    @Style.styler(EntityType.spoiler)
    def _spoiler(cls, _: MessageEntity, text: str) -> str:
        return f'<span class="tg-spoiler">{text}</span>'

    @classmethod
    @Style.styler(EntityType.strikethrough)
    def _strikethrough(cls, _: MessageEntity, text: str) -> str:
        return f"<s>{text}</s>"

    @classmethod
    @Style.styler(EntityType.text_link)
    def _text_link(cls, entity: MessageEntity, text: str) -> str:
        return f'<a href="{entity.url}">{text}</a>'

    @classmethod
    @Style.styler(EntityType.text_mention)
    def _text_mention(cls, entity: MessageEntity, text: str) -> str:
        return f'<a href="tg://user?id={entity.user.id}">{text}</a>'

    @classmethod
    @Style.styler(EntityType.custom_emoji)
    def _custom_emoji(cls, entity: MessageEntity, text: str) -> str:
        return f'<tg-emoji emoji-id="{entity.custom_emoji_id}">{text}</a>'

    @classmethod
    @Style.styler(EntityType.code)
    def _code(cls, _: MessageEntity, text: str) -> str:
        return f"<code>{text}</code>"

    @classmethod
    @Style.styler(EntityType.pre)
    def _pre(cls, entity: MessageEntity, text: str) -> str:
        if entity.language:
            return f'<pre><code class="language-{entity.language}">{text}</code></pre>'
        return f"<pre>{text}</pre>"

    @classmethod
    @Style.styler(EntityType.blockquote)
    def _blockquote(cls, _: MessageEntity, text: str) -> str:
        return f"<blockquote>{text}</blockquote>"


class MarkdownStyle(Style):
    _RE = re.compile(r"([*_`\[])")

    @classmethod
    def escape(cls, text: str) -> str:
        return cls._RE.sub(r'\\\1', text)

    @classmethod
    @Style.styler(EntityType.bold)
    def _bold(cls, _: MessageEntity, text: str) -> str:
        return f"*{text}*"

    @classmethod
    @Style.styler(EntityType.italic)
    def _italic(cls, _: MessageEntity, text: str) -> str:
        return f"_{text}_"

    @classmethod
    @Style.styler(EntityType.text_link)
    def _text_link(cls, entity: MessageEntity, text: str) -> str:
        return f"[{text}]({entity.url})"

    @classmethod
    @Style.styler(EntityType.text_mention)
    def _text_mention(cls, entity: MessageEntity, text: str) -> str:
        return f"[{text}](tg://user?id={entity.user.id})"

    @classmethod
    @Style.styler(EntityType.code)
    def _code(cls, _: MessageEntity, text: str) -> str:
        return f"```\n{text}```"

    @classmethod
    @Style.styler(EntityType.pre)
    def _pre(cls, entity: MessageEntity, text: str) -> str:
        code = entity.language or ""
        return f"```{code}\n{text}```"


class MarkdownV2Style(Style):
    _RE = re.compile(r"([_*\[\]()~`>#+\-=|{}.!\\])")

    @classmethod
    def escape(cls, text: str) -> str:
        return cls._RE.sub(r'\\\1', text)

    @classmethod
    @Style.styler(EntityType.bold)
    def _bold(cls, _: MessageEntity, text: str) -> str:
        return f"*{text}*"

    @classmethod
    @Style.styler(EntityType.italic)
    def _italic(cls, _: MessageEntity, text: str) -> str:
        return f"_{text}_"

    @classmethod
    @Style.styler(EntityType.underline)
    def _underline(cls, _: MessageEntity, text: str) -> str:
        return f"\r__\r{text}\r__\r"

    @classmethod
    @Style.styler(EntityType.strikethrough)
    def _strikethrough(cls, _: MessageEntity, text: str) -> str:
        return f"~{text}~"

    @classmethod
    @Style.styler(EntityType.spoiler)
    def _spoiler(cls, _: MessageEntity, text: str) -> str:
        return f"||{text}||"

    @classmethod
    @Style.styler(EntityType.text_link)
    def _text_link(cls, entity: MessageEntity, text: str) -> str:
        return f"[{text}]({entity.url})"

    @classmethod
    @Style.styler(EntityType.text_mention)
    def _text_mention(cls, entity: MessageEntity, text: str) -> str:
        return f"[{text}](tg://user?id={entity.user.id})"

    @classmethod
    @Style.styler(EntityType.custom_emoji)
    def _custom_emoji(cls, entity: MessageEntity, text: str) -> str:
        return f"![{text}](tg://emoji?id={entity.custom_emoji_id})"

    @classmethod
    @Style.styler(EntityType.code)
    def _code(cls, _: MessageEntity, text: str) -> str:
        return f"`{text}`"

    @classmethod
    @Style.styler(EntityType.pre)
    def _pre(cls, entity: MessageEntity, text: str) -> str:
        code = entity.language or ""
        return f"```{code}\n{text}```"

    @classmethod
    @Style.styler(EntityType.blockquote)
    def _blockquote(cls, _: MessageEntity, text: str) -> str:
        text = text.replace("\n", "\n>")
        return f">{text}\r"
