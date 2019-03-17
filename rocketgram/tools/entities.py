# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).

import sys
from collections import namedtuple

from . import escape


def get(text, entity):
    if sys.maxunicode == 0xffff:
        return text[entity.offset:entity.offset + entity.length]

    text = text.encode('utf-16-le')
    text = text[entity.offset * 2:(entity.offset + entity.length) * 2]

    return text.decode('utf-16-le')


Item = namedtuple('Item', ('type', 'text', 'url', 'user'))


def parse(text, entities):
    if not entities:
        return [Item('text', text, None, None)]

    if sys.maxunicode == 0xffff:
        encoded = False
    else:
        encoded = True
        text = text.encode('utf-16-le')

    parsed = list()
    idx = 0
    for e in entities:
        offset = e.offset * 2 if encoded else e.offset
        length = e.length * 2 if encoded else e.length

        if idx < offset:
            t = text[idx:offset]
            if encoded:
                t = t.decode('utf-16-le')
            parsed.append(Item('text', t, None, None))

        t = text[offset:offset + length]
        if encoded:
            t = t.decode('utf-16-le')
        parsed.append(Item(e.entity_type, t, e.url, e.user))

        idx = offset + length

    if idx < len(text):
        t = text[idx:len(text)]
        if encoded:
            t = t.decode('utf-16-le')
        parsed.append(Item('text', t, None, None))

    return parsed


def to_html(text, entities, escape_html=True):
    if escape_html:
        escape_func = escape.html
    else:
        escape_func = lambda t: t

    parsed = parse(text, entities)

    result = str()
    for i in parsed:
        t = escape_func(i.text)
        if i.type == 'bold':
            result += '<b>%s</b>' % t
        elif i.type == 'italic':
            result += '<i>%s</i>' % t
        elif i.type == 'code':
            result += '<code>%s</code>' % t
        elif i.type == 'pre':
            result += '<pre>%s</pre>' % t
        elif i.type == 'text_link':
            result += '<a href="%s">%s</a>' % (i.url, t)
        else:
            result += t

    return result


def to_markdown(text, entities, escape_markdown=True):
    if escape_markdown:
        escape_func = escape.markdown
    else:
        escape_func = lambda t: t

    parsed = parse(text, entities)

    result = str()
    for i in parsed:
        t = escape_func(i.text)
        if i.type == 'bold':
            result += '*%s*' % t
        elif i.type == 'italic':
            result += '_%s_' % t
        elif i.type == 'code':
            result += '`%s`' % t
        elif i.type == 'pre':
            result += '```\n%s```' % t
        elif i.type == 'text_link':
            result += '[%s](%s)' % (t, i.url)
        else:
            result += t

    return result
