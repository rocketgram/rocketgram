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
