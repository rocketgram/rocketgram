# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from io import BytesIO

from rocketgram import api


def test_GetUpdates():
    req = api.GetUpdates()
    assert req.render() == {}
    assert req.render(with_method=True) == {'method': 'GetUpdates'}
    assert req.files() == []

    req = api.GetUpdates(offset=1000, limit=10, timeout=30,
                              allowed_updates=[api.UpdateType.message, api.UpdateType.channel_post])

    assert req.render() == {'allowed_updates': ['message', 'channel_post'], 'limit': 10, 'offset': 1000, 'timeout': 30}


def test_SetWebhook():
    req = api.SetWebhook(url='https://www.example.com/bot')

    assert req.render() == {'url': 'https://www.example.com/bot'}
    assert req.render(with_method=True) == {'method': 'SetWebhook', 'url': 'https://www.example.com/bot'}
    assert req.files() == []

    req = api.SetWebhook(url='https://www.example.com/bot',
                              certificate='https://www.example.com/cert/cert.crt', max_connections=10,
                              allowed_updates=[api.UpdateType.message, api.UpdateType.channel_post])

    assert req.render() == {'url': 'https://www.example.com/bot',
                            'allowed_updates': ['message', 'channel_post'], 'max_connections': 10,
                            'certificate': 'https://www.example.com/cert/cert.crt'}

    file = api.InputFile('cert.crt', 'application/x-x509-ca-cert', BytesIO())
    req = api.SetWebhook(url='https://www.example.com/bot', certificate=file)

    assert req.render() == {'url': 'https://www.example.com/bot',
                            'certificate': 'attach://cert.crt'}
    assert req.files() == [file]


def test_DeleteWebhook():
    req = api.DeleteWebhook()
    assert req.render() == {}
    assert req.render(with_method=True) == {'method': 'DeleteWebhook'}
    assert req.files() == []


def test_GetWebhookInfo():
    req = api.GetWebhookInfo()
    assert req.render() == {}
    assert req.render(with_method=True) == {'method': 'GetWebhookInfo'}
    assert req.files() == []


def test_GetMe():
    req = api.GetMe()
    assert req.render() == {}
    assert req.render(with_method=True) == {'method': 'GetMe'}
    assert req.files() == []


def test_SendMessage():
    req = api.SendMessage(1000, "Hello, World!")
    assert req.render() == {'chat_id': 1000, 'text': 'Hello, World!'}
    assert req.render(with_method=True) == {'method': 'SendMessage', 'chat_id': 1000, 'text': 'Hello, World!'}
    assert req.files() == []

    kb = api.InlineKeyboardMarkup([[api.InlineKeyboardButton('Button', callback_data='data')]])
    req = api.SendMessage(1000, "Hello, World!", parse_mode=api.ParseModeType.html,
                               disable_web_page_preview=True, disable_notification=True, reply_to_message_id=100,
                               reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'text': 'Hello, World!', 'disable_notification': True,
                            'disable_web_page_preview': True, 'parse_mode': 'html', 'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}
    assert req.files() == []


def test_ForwardMessage():
    req = api.ForwardMessage(1000, 1234, 100)
    assert req.render() == {'chat_id': 1000, 'from_chat_id': 1234, 'message_id': 100}
    assert req.render(with_method=True) == {'method': 'ForwardMessage', 'chat_id': 1000, 'from_chat_id': 1234,
                                            'message_id': 100}
    assert req.files() == []

    req = api.ForwardMessage(1000, 1234, 100, disable_notification=True)
    assert req.render() == {'chat_id': 1000, 'from_chat_id': 1234, 'message_id': 100, 'disable_notification': True}
    assert req.files() == []


def test_SendPhoto():
    req = api.SendPhoto(1000, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert req.render() == {'chat_id': 1000, 'photo': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.render(with_method=True) == {'method': 'SendPhoto', 'chat_id': 1000,
                                            'photo': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.files() == []

    photo_file = api.InputFile('photo.jpg', 'image/jpeg', BytesIO())

    kb = api.InlineKeyboardMarkup([[api.InlineKeyboardButton('Button', callback_data='data')]])
    req = api.SendPhoto(1000, photo_file, caption="Hello, World!", parse_mode=api.ParseModeType.html,
                             disable_notification=True, reply_to_message_id=100, reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'photo': 'attach://photo.jpg', 'disable_notification': True,
                            'caption': 'Hello, World!', 'parse_mode': 'html', 'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}
    assert req.files() == [photo_file]


def test_SendAudio():
    req = api.SendAudio(1000, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert req.render() == {'chat_id': 1000, 'audio': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.render(with_method=True) == {'method': 'SendAudio', 'chat_id': 1000,
                                            'audio': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.files() == []

    audio_file = api.InputFile('audio.mp3', 'audio/mpeg', BytesIO())
    thumb_file = api.InputFile('thumb.jpg', 'image/jpeg', BytesIO())

    kb = api.InlineKeyboardMarkup([[api.InlineKeyboardButton('Button', callback_data='data')]])
    req = api.SendAudio(1000, audio_file, duration=300, performer="Beethoven", title="Symphony No. 5",
                             thumb=thumb_file, caption="Hello, World!", parse_mode=api.ParseModeType.html,
                             disable_notification=True, reply_to_message_id=100, reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'audio': 'attach://audio.mp3', 'duration': 300, 'performer': "Beethoven",
                            'title': "Symphony No. 5", 'thumb': 'attach://thumb.jpg', 'caption': 'Hello, World!',
                            'parse_mode': 'html', 'disable_notification': True, 'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == [audio_file, thumb_file]


def test_SendDocument():
    req = api.SendDocument(1000, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert req.render() == {'chat_id': 1000, 'document': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.render(with_method=True) == {'method': 'SendDocument', 'chat_id': 1000,
                                            'document': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.files() == []

    document_file = api.InputFile('document.pdf', 'application/pdf', BytesIO())
    thumb_file = api.InputFile('thumb.jpg', 'image/jpeg', BytesIO())

    kb = api.InlineKeyboardMarkup([[api.InlineKeyboardButton('Button', callback_data='data')]])
    req = api.SendDocument(1000, document_file, thumb=thumb_file, caption="Hello, World!",
                                parse_mode=api.ParseModeType.html, disable_notification=True, reply_to_message_id=100,
                                reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'document': 'attach://document.pdf', 'thumb': 'attach://thumb.jpg',
                            'caption': 'Hello, World!', 'parse_mode': 'html', 'disable_notification': True,
                            'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == [document_file, thumb_file]


def test_SendVideo():
    req = api.SendVideo(1000, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert req.render() == {'chat_id': 1000, 'video': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.render(with_method=True) == {'method': 'SendVideo', 'chat_id': 1000,
                                            'video': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.files() == []

    video_file = api.InputFile('video.mp4', 'video/mp4', BytesIO())
    thumb_file = api.InputFile('thumb.jpg', 'image/jpeg', BytesIO())

    kb = api.InlineKeyboardMarkup([[api.InlineKeyboardButton('Button', callback_data='data')]])
    req = api.SendVideo(1000, video_file, duration=300, width=640, height=480, supports_streaming=True,
                             thumb=thumb_file, caption="Hello, World!", parse_mode=api.ParseModeType.html,
                             disable_notification=True, reply_to_message_id=100, reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'video': 'attach://video.mp4', 'duration': 300, 'width': 640,
                            'height': 480, 'supports_streaming': True, 'thumb': 'attach://thumb.jpg',
                            'caption': 'Hello, World!', 'parse_mode': 'html', 'disable_notification': True,
                            'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == [video_file, thumb_file]


def test_SendAnimation():
    req = api.SendAnimation(1000, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert req.render() == {'chat_id': 1000, 'animation': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.render(with_method=True) == {'method': 'SendAnimation', 'chat_id': 1000,
                                            'animation': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.files() == []

    animation_file = api.InputFile('animation.mp4', 'video/mp4', BytesIO())
    thumb_file = api.InputFile('thumb.jpg', 'image/jpeg', BytesIO())

    kb = api.InlineKeyboardMarkup([[api.InlineKeyboardButton('Button', callback_data='data')]])
    req = api.SendAnimation(1000, animation_file, duration=300, width=640, height=480,
                                 thumb=thumb_file, caption="Hello, World!", parse_mode=api.ParseModeType.html,
                                 disable_notification=True, reply_to_message_id=100, reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'animation': 'attach://animation.mp4', 'duration': 300, 'width': 640,
                            'height': 480, 'thumb': 'attach://thumb.jpg',
                            'caption': 'Hello, World!', 'parse_mode': 'html', 'disable_notification': True,
                            'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == [animation_file, thumb_file]


def test_SendVoice():
    req = api.SendVoice(1000, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert req.render() == {'chat_id': 1000, 'voice': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.render(with_method=True) == {'method': 'SendVoice', 'chat_id': 1000,
                                            'voice': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.files() == []

    voice_file = api.InputFile('voice.opus', 'audio/ogg', BytesIO())

    kb = api.InlineKeyboardMarkup([[api.InlineKeyboardButton('Button', callback_data='data')]])
    req = api.SendVoice(1000, voice_file, duration=300, caption="Hello, World!",
                             parse_mode=api.ParseModeType.html, disable_notification=True, reply_to_message_id=100,
                             reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'voice': 'attach://voice.opus', 'duration': 300,
                            'caption': 'Hello, World!', 'parse_mode': 'html', 'disable_notification': True,
                            'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == [voice_file]


def test_SendVideoNote():
    req = api.SendVideoNote(1000, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert req.render() == {'chat_id': 1000, 'video_note': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.render(with_method=True) == {'method': 'SendVideoNote', 'chat_id': 1000,
                                            'video_note': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.files() == []

    note_file = api.InputFile('voice.opus', 'audio/ogg', BytesIO())
    thumb_file = api.InputFile('thumb.jpg', 'image/jpeg', BytesIO())

    kb = api.InlineKeyboardMarkup([[api.InlineKeyboardButton('Button', callback_data='data')]])
    req = api.SendVideoNote(1000, note_file, duration=300, length=500, thumb=thumb_file,
                                 disable_notification=True, reply_to_message_id=100, reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'video_note': 'attach://voice.opus', 'duration': 300, 'length': 500,
                            'thumb': 'attach://thumb.jpg', 'disable_notification': True, 'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == [note_file, thumb_file]


def test_SendMediaGroupe():
    photo = api.InputMediaPhoto("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    req = api.SendMediaGroup(1000, [photo])
    assert req.render() == {'chat_id': 1000, 'media': [{'media': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'type': 'photo'}]}
    assert req.render(with_method=True) == {'method': 'SendMediaGroup', 'chat_id': 1000,
                                            'media': [{'media': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'type': 'photo'}]}
    assert req.files() == []

    photo_file_1 = api.InputFile('photo1.jpg', 'image/jpeg', BytesIO())
    photo1 = api.InputMediaPhoto(photo_file_1, caption="Hello, World!", parse_mode=api.ParseModeType.html)

    photo_file_2 = api.InputFile('photo2.jpg', 'image/jpeg', BytesIO())
    photo2 = api.InputMediaPhoto(photo_file_2, caption="Hello, World!", parse_mode=api.ParseModeType.html)

    req = api.SendMediaGroup(1000, [photo1, photo2], disable_notification=True, reply_to_message_id=100)

    assert req.render() == {'chat_id': 1000,
                            'media': [{'media': 'attach://photo1.jpg', 'type': 'photo', 'caption': 'Hello, World!',
                                       'parse_mode': 'html'},
                                      {'media': 'attach://photo2.jpg', 'type': 'photo', 'caption': 'Hello, World!',
                                       'parse_mode': 'html'}],
                            'disable_notification': True, 'reply_to_message_id': 100}

    assert req.files() == [photo_file_1, photo_file_2]


def test_SendLocation():
    req = api.SendLocation(1000, latitude=31.7767, longitude=35.2345)
    assert req.render() == {'chat_id': 1000, 'latitude': 31.7767, 'longitude': 35.2345}
    assert req.render(with_method=True) == {'method': 'SendLocation', 'chat_id': 1000,
                                            'latitude': 31.7767, 'longitude': 35.2345}
    assert req.files() == []

    kb = api.InlineKeyboardMarkup([[api.InlineKeyboardButton('Button', callback_data='data')]])
    req = api.SendLocation(1000, latitude=31.7767, longitude=35.2345, live_period=300,
                                disable_notification=True, reply_to_message_id=100, reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'latitude': 31.7767, 'longitude': 35.2345, 'disable_notification': True,
                            'live_period': 300, 'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == []


def test_EditMessageLiveLocation():
    req = api.EditMessageLiveLocation(chat_id=1000, message_id=300, latitude=31.7767, longitude=35.2345)
    assert req.render() == {'chat_id': 1000, 'message_id': 300, 'latitude': 31.7767, 'longitude': 35.2345}
    assert req.render(with_method=True) == {'method': 'EditMessageLiveLocation', 'chat_id': 1000, 'message_id': 300,
                                            'latitude': 31.7767, 'longitude': 35.2345}
    assert req.files() == []

    req = api.EditMessageLiveLocation(inline_message_id='ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                           latitude=31.7767, longitude=35.2345)
    assert req.render() == {'inline_message_id': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                            'latitude': 31.7767, 'longitude': 35.2345}
    assert req.render(with_method=True) == {'method': 'EditMessageLiveLocation',
                                            'inline_message_id': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                            'latitude': 31.7767, 'longitude': 35.2345}
    assert req.files() == []

    kb = api.InlineKeyboardMarkup([[api.InlineKeyboardButton('Button', callback_data='data')]])
    req = api.EditMessageLiveLocation(chat_id=1000, message_id=300, latitude=31.7767, longitude=35.2345,
                                           reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'message_id': 300, 'latitude': 31.7767, 'longitude': 35.2345,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == []


def test_StopMessageLiveLocation():
    req = api.StopMessageLiveLocation(chat_id=1000, message_id=300)
    assert req.render() == {'chat_id': 1000, 'message_id': 300}
    assert req.render(with_method=True) == {'method': 'StopMessageLiveLocation', 'chat_id': 1000, 'message_id': 300}
    assert req.files() == []

    req = api.StopMessageLiveLocation(inline_message_id='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    assert req.render() == {'inline_message_id': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.render(with_method=True) == {'method': 'StopMessageLiveLocation',
                                            'inline_message_id': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    assert req.files() == []

    kb = api.InlineKeyboardMarkup([[api.InlineKeyboardButton('Button', callback_data='data')]])
    req = api.StopMessageLiveLocation(chat_id=1000, message_id=300, reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'message_id': 300,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == []


def test_SendVenue():
    req = api.SendVenue(1000, latitude=31.7767, longitude=35.2345, title='Earth', address='Solar system')
    assert req.render() == {'chat_id': 1000, 'latitude': 31.7767, 'longitude': 35.2345, 'title': 'Earth',
                            'address': 'Solar system'}
    assert req.render(with_method=True) == {'method': 'SendVenue', 'chat_id': 1000, 'latitude': 31.7767,
                                            'longitude': 35.2345, 'title': 'Earth', 'address': 'Solar system'}
    assert req.files() == []

    kb = api.InlineKeyboardMarkup([[api.InlineKeyboardButton('Button', callback_data='data')]])
    req = api.SendVenue(1000, latitude=31.7767, longitude=35.2345, title='Earth', address='Solar system',
                             foursquare_id='ABCDE123', foursquare_type='food/icecream',
                             disable_notification=True, reply_to_message_id=100, reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'latitude': 31.7767, 'longitude': 35.2345, 'title': 'Earth',
                            'address': 'Solar system', 'foursquare_id': 'ABCDE123', 'foursquare_type': 'food/icecream',
                            'disable_notification': True, 'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == []


def test_SendContact():
    req = api.SendContact(1000, phone_number='+1234567890', first_name='John')
    assert req.render() == {'chat_id': 1000, 'phone_number': '+1234567890', 'first_name': 'John'}
    assert req.render(with_method=True) == {'method': 'SendContact', 'chat_id': 1000, 'phone_number': '+1234567890',
                                            'first_name': 'John'}
    assert req.files() == []

    vcard = "BEGIN:VCARD\nVERSION:4.0\nN:Gump;Forrest;;Mr.;\nFN:Forrest Gump\n" \
            "EMAIL:forrestgump@example.com\nEND:VCARD"

    kb = api.InlineKeyboardMarkup([[api.InlineKeyboardButton('Button', callback_data='data')]])
    req = api.SendContact(1000, phone_number='+1234567890', first_name='Forrest', last_name='Gump', vcard=vcard,
                               disable_notification=True, reply_to_message_id=100, reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'phone_number': '+1234567890', 'first_name': 'Forrest',
                            'last_name': 'Gump', 'vcard': vcard, 'disable_notification': True,
                            'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == []


def test_SendPoll():
    req = api.SendPoll(1000, question='Do it?', options=['Yes', 'No'])
    assert req.render() == {'chat_id': 1000, 'question': 'Do it?', 'options': ['Yes', 'No']}
    assert req.render(with_method=True) == {'method': 'SendPoll', 'chat_id': 1000, 'question': 'Do it?',
                                            'options': ['Yes', 'No']}
    assert req.files() == []

    kb = api.InlineKeyboardMarkup([[api.InlineKeyboardButton('Button', callback_data='data')]])
    req = api.SendPoll(1000, question='Do it?', options=['Yes', 'No'],
                            disable_notification=True, reply_to_message_id=100, reply_markup=kb)

    assert req.render() == {'chat_id': 1000, 'question': 'Do it?', 'options': ['Yes', 'No'],
                            'disable_notification': True, 'reply_to_message_id': 100,
                            'reply_markup': {'inline_keyboard': [[{'callback_data': 'data', 'text': 'Button'}]]}}

    assert req.files() == []


def test_SendChatAction():
    req = api.SendChatAction(1000, action=api.ChatActionType.typing)
    assert req.render() == {'chat_id': 1000, 'action': 'typing'}
    assert req.render(with_method=True) == {'method': 'SendChatAction', 'chat_id': 1000, 'action': 'typing'}
    assert req.files() == []


def test_GetUserProfilePhotos():
    req = api.GetUserProfilePhotos(10000, offset=10, limit=20)
    assert req.render() == {'user_id': 10000, 'offset': 10, 'limit': 20}
    assert req.render(with_method=True) == {'method': 'GetUserProfilePhotos', 'user_id': 10000, 'offset': 10,
                                            'limit': 20}
    assert req.files() == []


def test_GetFile():
    req = api.GetFile('ABCDEFG12345')
    assert req.render() == {'file_id': 'ABCDEFG12345'}
    assert req.render(with_method=True) == {'method': 'GetFile', 'file_id': 'ABCDEFG12345'}
    assert req.files() == []
