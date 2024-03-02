# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from .parser import Parser
from .style import EmptyStyle, HtmlStyle, MarkdownV2Style, MarkdownStyle

__all__ = [
    'Parser',
    'EmptyStyle',
    'HtmlStyle',
    'MarkdownV2Style',
    'MarkdownStyle',
    'escape_html',
    'escape_markdown',
    'escape_markdown_v2',
    'to_html',
    'to_markdown',
    'to_markdown_v2'
]


def escape_html(text: str) -> str:
    return HtmlStyle.escape(text)


def escape_markdown(text: str) -> str:
    return MarkdownStyle.escape(text)


def escape_markdown_v2(text: str) -> str:
    return MarkdownV2Style.escape(text)


def to_html(text: str, entities: list) -> str:
    return Parser.parse(text, entities).render(HtmlStyle)


def to_markdown(text: str, entities: list) -> str:
    return Parser.parse(text, entities).render(MarkdownStyle)


def to_markdown_v2(text: str, entities: list) -> str:
    return Parser.parse(text, entities).render(MarkdownV2Style)
