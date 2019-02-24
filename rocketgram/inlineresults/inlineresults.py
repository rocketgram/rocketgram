# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


import time


class InlineQueryResults:
    """https://core.telegram.org/bots/api#inlinequeryresult"""

    def __init__(self):
        self._items = list()

    def __assign_id(self):
        return str(int(time.time() * 10000))

    def article(self, _id, title, input_message_content, reply_markup=None, url=None, hide_url=None, description=None,
                thumb_url=None, thumb_width=None, thumb_height=None):
        """https://core.telegram.org/bots/api#inlinequeryresultarticle"""
        item = dict()

        item['type'] = 'article'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['title'] = title
        item['input_message_content'] = input_message_content.render()
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if url:
            item['url'] = url
        if hide_url:
            item['hide_url'] = hide_url
        if description:
            item['description'] = description
        if thumb_url:
            item['thumb_url'] = thumb_url
        if thumb_width:
            item['thumb_width'] = thumb_width
        if thumb_height:
            item['thumb_height'] = thumb_height

        self._items.append(item)
        return self

    def photo(self, _id, photo_url, thumb_url, photo_width=None, photo_height=None, title=None, description=None,
              caption=None, reply_markup=None, input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultphoto"""
        item = dict()

        item['type'] = 'photo'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['photo_url'] = photo_url
        item['thumb_url'] = thumb_url
        if photo_width:
            item['photo_width'] = photo_width
        if photo_height:
            item['photo_height'] = photo_height
        if title:
            item['title'] = title
        if description:
            item['description'] = description
        if caption:
            item['caption'] = caption
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def gif(self, _id, gif_url, thumb_url, gif_width=None, gif_height=None, gif_duration=None, title=None, caption=None,
            reply_markup=None, input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultgif"""
        item = dict()

        item['type'] = 'gif'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['gif_url'] = gif_url
        item['thumb_url'] = thumb_url
        if gif_width:
            item['gif_width'] = gif_width
        if gif_height:
            item['gif_height'] = gif_height
        if gif_duration:
            item['gif_duration'] = gif_duration
        if title:
            item['title'] = title
        if caption:
            item['caption'] = caption
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def mpeg4gif(self, _id, mpeg4_url, thumb_url, mpeg4_width=None, mpeg4_height=None, mpeg4_duration=None, title=None,
                 caption=None, reply_markup=None, input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif"""
        item = dict()

        item['type'] = 'mpeg4_gif'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['mpeg4_url'] = mpeg4_url
        item['thumb_url'] = thumb_url
        if mpeg4_width:
            item['mpeg4_width'] = mpeg4_width
        if mpeg4_height:
            item['mpeg4_height'] = mpeg4_height
        if mpeg4_duration:
            item['mpeg4_duration'] = mpeg4_duration
        if title:
            item['title'] = title
        if caption:
            item['caption'] = caption
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def video(self, _id, video_url, mime_type, thumb_url, title, caption=None, video_width=None, video_height=None,
              video_duration=None, description=None, reply_markup=None, input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultvideo"""
        item = dict()

        item['type'] = 'video'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['video_url'] = video_url
        item['mime_type'] = mime_type
        item['thumb_url'] = thumb_url
        item['title'] = title
        if caption:
            item['caption'] = caption
        if video_width:
            item['video_width'] = video_width
        if video_height:
            item['video_height'] = video_height
        if video_duration:
            item['video_duration'] = video_duration
        if description:
            item['description'] = description
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def audio(self, _id, audio_url, title, caption=None, performer=None, audio_duration=None, reply_markup=None,
              input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultaudio"""
        item = dict()

        item['type'] = 'audio'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['audio_url'] = audio_url
        item['title'] = title
        if caption:
            item['caption'] = caption
        if performer:
            item['performer'] = performer
        if audio_duration:
            item['audio_duration'] = audio_duration
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def voice(self, _id, voice_url, title, caption=None, voice_duration=None, reply_markup=None,
              input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultvoice"""
        item = dict()

        item['type'] = 'voice'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['voice_url'] = voice_url
        item['title'] = title
        if caption:
            item['caption'] = caption
        if voice_duration:
            item['voice_duration'] = voice_duration
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def document(self, _id, document_url, mime_type, title, caption=None, description=None, thumb_url=None,
                 thumb_width=None, thumb_height=None, reply_markup=None, input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultdocument"""
        item = dict()

        item['type'] = 'document'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['document_url'] = document_url
        item['mime_type'] = mime_type
        item['title'] = title
        if caption:
            item['caption'] = caption
        if description:
            item['description'] = description
        if thumb_url:
            item['thumb_url'] = thumb_url
        if thumb_width:
            item['thumb_width'] = thumb_width
        if thumb_height:
            item['thumb_height'] = thumb_height
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def location(self, _id, latitude, longitude, title, thumb_url=None, thumb_width=None, thumb_height=None,
                 reply_markup=None, input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultlocation"""
        item = dict()

        item['type'] = 'location'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['latitude'] = latitude
        item['longitude'] = longitude
        item['title'] = title
        if thumb_url:
            item['thumb_url'] = thumb_url
        if thumb_width:
            item['thumb_width'] = thumb_width
        if thumb_height:
            item['thumb_height'] = thumb_height
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def venue(self, _id, latitude, longitude, title, address, foursquare_id, thumb_url=None, thumb_width=None,
              thumb_height=None, reply_markup=None, input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultvenue"""
        item = dict()

        item['type'] = 'venue'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['latitude'] = latitude
        item['longitude'] = longitude
        item['title'] = title
        item['address'] = address
        item['foursquare_id'] = foursquare_id
        if thumb_url:
            item['thumb_url'] = thumb_url
        if thumb_width:
            item['thumb_width'] = thumb_width
        if thumb_height:
            item['thumb_height'] = thumb_height
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def contact(self, _id, phone_number, first_name, last_name=None, thumb_url=None, thumb_width=None,
                thumb_height=None, reply_markup=None, input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultcontact"""
        item = dict()

        item['type'] = 'contact'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['phone_number'] = phone_number
        item['first_name'] = first_name
        if last_name:
            item['last_name'] = last_name
        if thumb_url:
            item['thumb_url'] = thumb_url
        if thumb_width:
            item['thumb_width'] = thumb_width
        if thumb_height:
            item['thumb_height'] = thumb_height
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def game(self, _id, game_short_name, reply_markup=None):
        """https://core.telegram.org/bots/api#inlinequeryresultgame"""
        item = dict()

        item['type'] = 'contact'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['game_short_name'] = game_short_name
        if reply_markup:
            item['reply_markup'] = reply_markup.render()

        self._items.append(item)
        return self

    def cached_photo(self, _id, photo_file_id, title=None, description=None, caption=None, reply_markup=None,
                     input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultcachedphoto"""
        item = dict()

        item['type'] = 'photo'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['photo_file_id'] = photo_file_id
        if title:
            item['title'] = title
        if description:
            item['description'] = description
        if caption:
            item['caption'] = caption
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def cached_gif(self, _id, gif_file_id, title=None, caption=None, reply_markup=None, input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultcachedgif"""
        item = dict()

        item['type'] = 'gif'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['gif_file_id'] = gif_file_id
        if title:
            item['title'] = title
        if caption:
            item['caption'] = caption
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def cached_mpeg4gif(self, _id, mpeg4_file_id, title=None, caption=None, reply_markup=None,
                        input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif"""
        item = dict()

        item['type'] = 'mpeg4_gif'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['mpeg4_file_id'] = mpeg4_file_id
        if title:
            item['title'] = title
        if caption:
            item['caption'] = caption
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def cached_sticker(self, _id, sticker_file_id, reply_markup=None, input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultcachedsticker"""
        item = dict()

        item['type'] = 'sticker'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['sticker_file_id'] = sticker_file_id
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def cached_document(self, _id, document_file_id, title, description=None, caption=None, reply_markup=None,
                        input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultcacheddocument"""
        item = dict()

        item['type'] = 'document'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['document_file_id'] = document_file_id
        item['title'] = title
        if description:
            item['description'] = description
        if caption:
            item['caption'] = caption
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def cached_video(self, _id, video_file_id, title, description=None, caption=None, reply_markup=None,
                     input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultcachedvideo"""
        item = dict()

        item['type'] = 'video'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['video_file_id'] = video_file_id
        item['title'] = title
        if description:
            item['description'] = description
        if caption:
            item['caption'] = caption
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def cached_voice(self, _id, voice_file_id, title, caption=None, reply_markup=None, input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultcachedvoice"""
        item = dict()

        item['type'] = 'voice'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['voice_file_id'] = voice_file_id
        item['title'] = title
        if caption:
            item['caption'] = caption
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def cached_audio(self, _id, audio_file_id, caption=None, reply_markup=None, input_message_content=None):
        """https://core.telegram.org/bots/api#inlinequeryresultcachedaudio"""
        item = dict()

        item['type'] = 'audio'
        if _id:
            item['id'] = _id
        else:
            item['id'] = self.__assign_id()

        item['audio_file_id'] = audio_file_id
        if caption:
            item['caption'] = caption
        if reply_markup:
            item['reply_markup'] = reply_markup.render()
        if input_message_content:
            item['input_message_content'] = input_message_content.render()

        self._items.append(item)
        return self

    def render(self):
        results = list()
        cnt = 0
        for items in self._items:
            results.append(items)

        return results
