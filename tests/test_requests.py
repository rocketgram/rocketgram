# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from io import BytesIO

from rocketgram import requests
from rocketgram import types


def test_GetUpdates():
    req = requests.GetUpdates()
    assert req.render() == {}
    assert req.method == 'getUpdates'
    assert req.render(with_method=True) == {'method': 'getUpdates'}
    assert req.files() == []

    req = requests.GetUpdates(offset=1000, limit=10, timeout=30,
                              allowed_updates=[types.UpdateType.message, types.UpdateType.channel_post])

    assert req.render() == {'allowed_updates': ['message', 'channel_post'], 'limit': 10, 'offset': 1000, 'timeout': 30}


def test_SetWebhook():
    req = requests.SetWebhook(url='https://www.example.com/bot')

    assert req.render() == {'url': 'https://www.example.com/bot'}
    assert req.method == 'setWebhook'
    assert req.render(with_method=True) == {'method': 'setWebhook', 'url': 'https://www.example.com/bot'}
    assert req.files() == []

    req = requests.SetWebhook(url='https://www.example.com/bot',
                              certificate='https://www.example.com/cert/cert.crt', max_connections=10,
                              allowed_updates=[types.UpdateType.message, types.UpdateType.channel_post])

    assert req.render() == {'url': 'https://www.example.com/bot',
                            'allowed_updates': ['message', 'channel_post'], 'max_connections': 10,
                            'certificate': 'https://www.example.com/cert/cert.crt'}

    file = types.InputFile('cert.crt', 'application/x-x509-ca-cert', BytesIO())
    req = requests.SetWebhook(url='https://www.example.com/bot', certificate=file)

    assert req.render() == {'url': 'https://www.example.com/bot',
                            'certificate': 'attach://cert.crt'}
    assert req.files() == [file]


def test_DeleteWebhook():
    req = requests.DeleteWebhook()
    assert req.render() == {}
    assert req.method == 'deleteWebhook'
    assert req.render(with_method=True) == {'method': 'deleteWebhook'}
    assert req.files() == []


def test_GetWebhookInfo():
    req = requests.GetWebhookInfo()
    assert req.render() == {}
    assert req.method == 'getWebhookInfo'
    assert req.render(with_method=True) == {'method': 'getWebhookInfo'}
    assert req.files() == []


def test_GetMe():
    req = requests.GetMe()
    assert req.render() == {}
    assert req.method == 'getMe'
    assert req.render(with_method=True) == {'method': 'getMe'}
    assert req.files() == []


def test_SendMessage():
    req = requests.SendMessage(1000, "Hello, World!")
    assert req.render() == {'chat_id': 1000, 'text': 'Hello, World!'}
    assert req.method == 'sendMessage'
    assert req.render(with_method=True) == {'method': 'sendMessage', 'chat_id': 1000, 'text': 'Hello, World!'}
    assert req.files() == []

    kb = types.InlineKeyboardMarkup([[types.InlineKeyboardButton('Button', callback_data='data')]])
    req = requests.SendMessage(1000, "Hello, World!", parse_mode=types.ParseModeType.html,
                               disable_web_page_preview=True, disable_notification=True, reply_to_message_id=100,
                               reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'text': 'Hello, World!', 'disable_notification': True,
                            'disable_web_page_preview': True, 'parse_mode': 'html', 'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}


def test_ForwardMessage():
    req = requests.ForwardMessage(1000, 1234, 100)
    assert req.render() == {'chat_id': 1000, 'from_chat_id': 1234, 'message_id': 100}
    assert req.method == 'forwardMessage'
    assert req.render(with_method=True) == {'method': 'forwardMessage', 'chat_id': 1000, 'from_chat_id': 1234,
                                            'message_id': 100}
    assert req.files() == []

    req = requests.ForwardMessage(1000, 1234, 100, disable_notification=True)
    assert req.render() == {'chat_id': 1000, 'from_chat_id': 1234, 'message_id': 100, 'disable_notification': True}
    assert req.files() == []