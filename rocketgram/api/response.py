# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional, Union
from .. import api


@dataclass(frozen=True)
class Response:
    """\
    Represents Response object:
    https://core.telegram.org/bots/api#making-requests

    Additional fields:
    method
    raw
    """

    method: 'api.Request'
    raw: dict
    ok: bool
    error_code: Optional[int]
    description: Optional[str]
    result: Optional[Union[bool, int, str, 'api.Chat', 'api.ChatMember', 'api.File', 'api.Message',
                           List['api.GameHighScore'], List['api.Update'], 'api.StickerSet', 'api.User',
                           'api.WebhookInfo', 'api.UserProfilePhotos', List['api.ChatMember'], List['api.BotCommand']]]
    parameters: Optional['api.ResponseParameters']

    @classmethod
    def parse(cls, data: dict, method: 'api.Request') -> Optional['Response']:
        if data is None:
            return None

        ok = data['ok']
        error_code = data.get('error_code')
        description = data.get('description')
        parameters = api.ResponseParameters.parse(data.get('parameters'))

        if error_code is not None:
            return cls(method, data, ok, error_code, description, None, parameters)

        result = None

        if isinstance(method, api.GetUpdates):
            result = [api.Update.parse(r) for r in data['result']]
        elif isinstance(method,
                        (api.SetWebhook, api.DeleteWebhook, api.SendChatAction, api.KickChatMember, api.UnbanChatMember,
                         api.RestrictChatMember, api.PromoteChatMember, api.SetChatPhoto, api.DeleteChatPhoto,
                         api.SetChatTitle, api.SetChatDescription, api.PinChatMessage, api.UnpinChatMessage,
                         api.LeaveChat, api.SetChatStickerSet, api.DeleteChatStickerSet, api.DeleteMessage,
                         api.CreateNewStickerSet, api.AddStickerToSet, api.SetStickerPositionInSet,
                         api.DeleteStickerFromSet, api.SetPassportDataErrors, api.SetGameScore,
                         api.ExportChatInviteLink, api.GetChatMembersCount, api.AnswerCallbackQuery,
                         api.AnswerInlineQuery, api.AnswerPreCheckoutQuery, api.AnswerShippingQuery)):
            result = data['result']
        elif isinstance(method, api.GetMyCommands):
            result = [api.BotCommand.parse(r) for r in data['result']]
        elif isinstance(method, api.SetMyCommands):
            result = data['result']
        elif isinstance(method, api.GetWebhookInfo):
            result = api.WebhookInfo.parse(data['result'])
        elif isinstance(method, api.GetMe):
            result = api.User.parse(data['result'])
        elif isinstance(method, (api.SendMessage, api.ForwardMessage, api.SendPhoto, api.SendAudio, api.SendDocument,
                                 api.SendVideo, api.SendAnimation, api.SendVoice, api.SendVideoNote, api.SendLocation,
                                 api.SendVenue, api.SendContact, api.SendPoll, api.SendDice, api.SendSticker,
                                 api.SendInvoice, api.SendGame)):
            result = api.Message.parse(data['result'])
        elif isinstance(method, (api.EditMessageLiveLocation, api.StopMessageLiveLocation, api.EditMessageText,
                                 api.EditMessageCaption, api.EditMessageMedia, api.EditMessageReplyMarkup)):
            r = data['result']
            if isinstance(r, bool):
                result = r
            else:
                result = api.Message.parse(r)
        elif isinstance(method, api.StopPoll):
            result = api.Poll.parse(data['result'])
        elif isinstance(method, api.SendMediaGroup):
            result = [api.Message.parse(r) for r in data['result']]
        elif isinstance(method, api.GetUserProfilePhotos):
            result = api.UserProfilePhotos.parse(data['result'])
        elif isinstance(method, (api.GetFile, api.UploadStickerFile)):
            result = api.File.parse(data['result'])
        elif isinstance(method, api.GetChat):
            result = api.Chat.parse(data['result'])
        elif isinstance(method, api.GetChatMember):
            result = api.ChatMember.parse(data['result'])
        elif isinstance(method, api.GetChatAdministrators):
            result = [api.ChatMember.parse(r) for r in data['result']]
        elif isinstance(method, api.GetStickerSet):
            result = api.StickerSet.parse(data['result'])
        elif isinstance(method, api.GetGameHighScores):
            result = [api.GameHighScore.parse(r) for r in data['result']]

        assert result is not None, "Should have value here! This probably means api was changed."

        return cls(method, data, ok, error_code, description, result, parameters)
