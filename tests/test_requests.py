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


def test_SendPhoto():
    req = requests.SendPhoto(1000, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert req.render() == {'chat_id': 1000, 'photo': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.method == 'sendPhoto'
    assert req.render(with_method=True) == {'method': 'sendPhoto', 'chat_id': 1000,
                                            'photo': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.files() == []

    photo_file = types.InputFile('photo.jpg', 'image/jpeg', BytesIO())

    kb = types.InlineKeyboardMarkup([[types.InlineKeyboardButton('Button', callback_data='data')]])
    req = requests.SendPhoto(1000, photo_file, caption="Hello, World!", parse_mode=types.ParseModeType.html,
                             disable_notification=True, reply_to_message_id=100, reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'photo': 'attach://photo.jpg', 'disable_notification': True,
                            'caption': 'Hello, World!', 'parse_mode': 'html', 'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}
    assert req.files() == [photo_file]


def test_SendAudio():
    req = requests.SendAudio(1000, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert req.render() == {'chat_id': 1000, 'audio': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.method == 'sendAudio'
    assert req.render(with_method=True) == {'method': 'sendAudio', 'chat_id': 1000,
                                            'audio': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.files() == []

    audio_file = types.InputFile('audio.mp3', 'audio/mpeg', BytesIO())
    thumb_file = types.InputFile('thumb.jpg', 'image/jpeg', BytesIO())

    kb = types.InlineKeyboardMarkup([[types.InlineKeyboardButton('Button', callback_data='data')]])
    req = requests.SendAudio(1000, audio_file, duration=300, performer="Beethoven", title="Symphony No. 5",
                             thumb=thumb_file, caption="Hello, World!", parse_mode=types.ParseModeType.html,
                             disable_notification=True, reply_to_message_id=100, reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'audio': 'attach://audio.mp3', 'duration': 300, 'performer': "Beethoven",
                            'title': "Symphony No. 5", 'thumb': 'attach://thumb.jpg', 'caption': 'Hello, World!',
                            'parse_mode': 'html', 'disable_notification': True, 'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == [audio_file, thumb_file]


def test_SendDocument():
    req = requests.SendDocument(1000, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert req.render() == {'chat_id': 1000, 'document': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.method == 'sendDocument'
    assert req.render(with_method=True) == {'method': 'sendDocument', 'chat_id': 1000,
                                            'document': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.files() == []

    document_file = types.InputFile('document.pdf', 'application/pdf', BytesIO())
    thumb_file = types.InputFile('thumb.jpg', 'image/jpeg', BytesIO())

    kb = types.InlineKeyboardMarkup([[types.InlineKeyboardButton('Button', callback_data='data')]])
    req = requests.SendDocument(1000, document_file, thumb=thumb_file, caption="Hello, World!",
                                parse_mode=types.ParseModeType.html, disable_notification=True, reply_to_message_id=100,
                                reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'document': 'attach://document.pdf', 'thumb': 'attach://thumb.jpg',
                            'caption': 'Hello, World!', 'parse_mode': 'html', 'disable_notification': True,
                            'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == [document_file, thumb_file]


def test_SendVideo():
    req = requests.SendVideo(1000, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert req.render() == {'chat_id': 1000, 'video': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.method == 'sendVideo'
    assert req.render(with_method=True) == {'method': 'sendVideo', 'chat_id': 1000,
                                            'video': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.files() == []

    video_file = types.InputFile('video.mp4', 'video/mp4', BytesIO())
    thumb_file = types.InputFile('thumb.jpg', 'image/jpeg', BytesIO())

    kb = types.InlineKeyboardMarkup([[types.InlineKeyboardButton('Button', callback_data='data')]])
    req = requests.SendVideo(1000, video_file, duration=300, width=640, height=480, supports_streaming=True,
                             thumb=thumb_file, caption="Hello, World!", parse_mode=types.ParseModeType.html,
                             disable_notification=True, reply_to_message_id=100, reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'video': 'attach://video.mp4', 'duration': 300, 'width': 640,
                            'height': 480, 'supports_streaming': True, 'thumb': 'attach://thumb.jpg',
                            'caption': 'Hello, World!', 'parse_mode': 'html', 'disable_notification': True,
                            'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == [video_file, thumb_file]


def test_SendAnimation():
    req = requests.SendAnimation(1000, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert req.render() == {'chat_id': 1000, 'animation': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.method == 'sendAnimation'
    assert req.render(with_method=True) == {'method': 'sendAnimation', 'chat_id': 1000,
                                            'animation': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.files() == []

    animation_file = types.InputFile('animation.mp4', 'video/mp4', BytesIO())
    thumb_file = types.InputFile('thumb.jpg', 'image/jpeg', BytesIO())

    kb = types.InlineKeyboardMarkup([[types.InlineKeyboardButton('Button', callback_data='data')]])
    req = requests.SendAnimation(1000, animation_file, duration=300, width=640, height=480,
                                 thumb=thumb_file, caption="Hello, World!", parse_mode=types.ParseModeType.html,
                                 disable_notification=True, reply_to_message_id=100, reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'animation': 'attach://animation.mp4', 'duration': 300, 'width': 640,
                            'height': 480, 'thumb': 'attach://thumb.jpg',
                            'caption': 'Hello, World!', 'parse_mode': 'html', 'disable_notification': True,
                            'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == [animation_file, thumb_file]


def test_SendVoice():
    req = requests.SendVoice(1000, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert req.render() == {'chat_id': 1000, 'voice': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.method == 'sendVoice'
    assert req.render(with_method=True) == {'method': 'sendVoice', 'chat_id': 1000,
                                            'voice': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.files() == []

    voice_file = types.InputFile('voice.opus', 'audio/ogg', BytesIO())

    kb = types.InlineKeyboardMarkup([[types.InlineKeyboardButton('Button', callback_data='data')]])
    req = requests.SendVoice(1000, voice_file, duration=300, caption="Hello, World!",
                             parse_mode=types.ParseModeType.html, disable_notification=True, reply_to_message_id=100,
                             reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'voice': 'attach://voice.opus', 'duration': 300,
                            'caption': 'Hello, World!', 'parse_mode': 'html', 'disable_notification': True,
                            'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == [voice_file]


def test_SendVideoNote():
    req = requests.SendVideoNote(1000, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert req.render() == {'chat_id': 1000, 'video_note': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.method == 'sendVideoNote'
    assert req.render(with_method=True) == {'method': 'sendVideoNote', 'chat_id': 1000,
                                            'video_note': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.files() == []

    note_file = types.InputFile('voice.opus', 'audio/ogg', BytesIO())
    thumb_file = types.InputFile('thumb.jpg', 'image/jpeg', BytesIO())

    kb = types.InlineKeyboardMarkup([[types.InlineKeyboardButton('Button', callback_data='data')]])
    req = requests.SendVideoNote(1000, note_file, duration=300, length=500, thumb=thumb_file,
                                 disable_notification=True, reply_to_message_id=100, reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'video_note': 'attach://voice.opus', 'duration': 300, 'length': 500,
                            'thumb': 'attach://thumb.jpg', 'disable_notification': True, 'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == [note_file, thumb_file]


def test_SendMediaGroupe():
    photo = types.InputMediaPhoto("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    req = requests.SendMediaGroup(1000, [photo])
    assert req.render() == {'chat_id': 1000, 'media': [{'media': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'type': 'photo'}]}
    assert req.method == 'sendMediaGroup'
    assert req.render(with_method=True) == {'method': 'sendMediaGroup', 'chat_id': 1000,
                                            'media': [{'media': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'type': 'photo'}]}
    assert req.files() == []

    photo_file_1 = types.InputFile('photo1.jpg', 'image/jpeg', BytesIO())
    photo1 = types.InputMediaPhoto(photo_file_1, caption="Hello, World!", parse_mode=types.ParseModeType.html)

    photo_file_2 = types.InputFile('photo2.jpg', 'image/jpeg', BytesIO())
    photo2 = types.InputMediaPhoto(photo_file_2, caption="Hello, World!", parse_mode=types.ParseModeType.html)

    req = requests.SendMediaGroup(1000, [photo1, photo2], disable_notification=True, reply_to_message_id=100)

    assert req.render() == {'chat_id': 1000,
                            'media': [{'media': 'attach://photo1.jpg', 'type': 'photo', 'caption': 'Hello, World!',
                                       'parse_mode': 'html'},
                                      {'media': 'attach://photo2.jpg', 'type': 'photo', 'caption': 'Hello, World!',
                                       'parse_mode': 'html'}],
                            'disable_notification': True, 'reply_to_message_id': 100}

    assert req.files() == [photo_file_1, photo_file_2]


def test_SendLocation():
    req = requests.SendLocation(1000, latitude=31.7767, longitude=35.2345)
    assert req.render() == {'chat_id': 1000, 'latitude': 31.7767, 'longitude': 35.2345}
    assert req.method == 'sendLocation'
    assert req.render(with_method=True) == {'method': 'sendLocation', 'chat_id': 1000,
                                            'latitude': 31.7767, 'longitude': 35.2345}
    assert req.files() == []

    kb = types.InlineKeyboardMarkup([[types.InlineKeyboardButton('Button', callback_data='data')]])
    req = requests.SendLocation(1000, latitude=31.7767, longitude=35.2345, live_period=300,
                                disable_notification=True, reply_to_message_id=100, reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'latitude': 31.7767, 'longitude': 35.2345, 'disable_notification': True,
                            'live_period': 300, 'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == []
