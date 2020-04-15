# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List, Optional, Union

from .add_sticker_to_set import AddStickerToSet
from .answer_callback_query import AnswerCallbackQuery
from .answer_inline_query import AnswerInlineQuery
from .answer_pre_checkout_query import AnswerPreCheckoutQuery
from .answer_shipping_query import AnswerShippingQuery
from .bot_command import BotCommand
from .chat import Chat
from .chat_member import ChatMember
from .create_new_sticker_set import CreateNewStickerSet
from .delete_chat_photo import DeleteChatPhoto
from .delete_chat_sticker_set import DeleteChatStickerSet
from .delete_message import DeleteMessage
from .delete_sticker_from_set import DeleteStickerFromSet
from .delete_webhook import DeleteWebhook
from .edit_message_caption import EditMessageCaption
from .edit_message_live_location import EditMessageLiveLocation
from .edit_message_media import EditMessageMedia
from .edit_message_reply_markup import EditMessageReplyMarkup
from .edit_message_text import EditMessageText
from .export_chat_invite_link import ExportChatInviteLink
from .file import File
from .forward_message import ForwardMessage
from .game_high_score import GameHighScore
from .get_chat import GetChat
from .get_chat_administrators import GetChatAdministrators
from .get_chat_member import GetChatMember
from .get_chat_members_count import GetChatMembersCount
from .get_file import GetFile
from .get_game_high_scores import GetGameHighScores
from .get_me import GetMe
from .get_my_commands import GetMyCommands
from .get_sticker_set import GetStickerSet
from .get_updates import GetUpdates
from .get_user_profile_photos import GetUserProfilePhotos
from .get_webhook_info import GetWebhookInfo
from .kick_chat_member import KickChatMember
from .leave_chat import LeaveChat
from .message import Message
from .pin_chat_message import PinChatMessage
from .poll import Poll
from .promote_chat_member import PromoteChatMember
from .request import Request
from .response_parameters import ResponseParameters
from .restrict_chat_member import RestrictChatMember
from .send_animation import SendAnimation
from .send_audio import SendAudio
from .send_chat_action import SendChatAction
from .send_contact import SendContact
from .send_dice import SendDice
from .send_document import SendDocument
from .send_game import SendGame
from .send_invoice import SendInvoice
from .send_location import SendLocation
from .send_media_group import SendMediaGroup
from .send_message import SendMessage
from .send_photo import SendPhoto
from .send_poll import SendPoll
from .send_sticker import SendSticker
from .send_venue import SendVenue
from .send_video import SendVideo
from .send_video_note import SendVideoNote
from .send_voice import SendVoice
from .set_chat_description import SetChatDescription
from .set_chat_photo import SetChatPhoto
from .set_chat_sticker_set import SetChatStickerSet
from .set_chat_title import SetChatTitle
from .set_game_score import SetGameScore
from .set_my_commands import SetMyCommands
from .set_passport_data_errors import SetPassportDataErrors
from .set_sticker_position_in_set import SetStickerPositionInSet
from .set_webhook import SetWebhook
from .sticker_set import StickerSet
from .stop_message_live_location import StopMessageLiveLocation
from .stop_poll import StopPoll
from .unban_chat_member import UnbanChatMember
from .unpin_chat_message import UnpinChatMessage
from .update import Update
from .upload_sticker_file import UploadStickerFile
from .user import User
from .user_profile_photos import UserProfilePhotos
from .webhook_info import WebhookInfo


@dataclass(frozen=True)
class Response:
    """\
    Represents Response object:
    https://core.telegram.org/bots/api#making-requests

    Additional fields:
    method
    raw
    """

    method: Request
    raw: dict
    ok: bool
    error_code: Optional[int]
    description: Optional[str]
    result: Optional[Union[bool, int, str, Chat, ChatMember, File, Message, List[GameHighScore],
                           List[Update], StickerSet, User, WebhookInfo, UserProfilePhotos,
                           List[ChatMember], List[BotCommand]]]
    parameters: Optional[ResponseParameters]

    @classmethod
    def parse(cls, data: dict, method: Request) -> Optional['Response']:
        if data is None:
            return None

        ok = data['ok']
        error_code = data.get('error_code')
        description = data.get('description')
        parameters = ResponseParameters.parse(data.get('parameters'))

        if error_code is not None:
            return cls(method, data, ok, error_code, description, None, parameters)

        result = None

        if isinstance(method, GetUpdates):
            result = [Update.parse(r) for r in data['result']]
        elif isinstance(method, (SetWebhook, DeleteWebhook, SendChatAction, KickChatMember, UnbanChatMember,
                                 RestrictChatMember, PromoteChatMember, SetChatPhoto, DeleteChatPhoto, SetChatTitle,
                                 SetChatDescription, PinChatMessage, UnpinChatMessage, LeaveChat, SetChatStickerSet,
                                 DeleteChatStickerSet, DeleteMessage, CreateNewStickerSet, AddStickerToSet,
                                 SetStickerPositionInSet, DeleteStickerFromSet, SetPassportDataErrors, SetGameScore,
                                 ExportChatInviteLink, GetChatMembersCount, AnswerCallbackQuery, AnswerInlineQuery,
                                 AnswerPreCheckoutQuery, AnswerShippingQuery)):
            result = data['result']
        elif isinstance(method, GetMyCommands):
            result = [BotCommand.parse(r) for r in data['result']]
        elif isinstance(method, SetMyCommands):
            result = data['result']
        elif isinstance(method, GetWebhookInfo):
            result = WebhookInfo.parse(data['result'])
        elif isinstance(method, GetMe):
            result = User.parse(data['result'])
        elif isinstance(method, (SendMessage, ForwardMessage, SendPhoto, SendAudio, SendDocument, SendVideo,
                                 SendAnimation, SendVoice, SendVideoNote, SendLocation, SendVenue, SendContact,
                                 SendPoll, SendDice, SendSticker, SendInvoice, SendGame)):
            result = Message.parse(data['result'])
        elif isinstance(method, (EditMessageLiveLocation, StopMessageLiveLocation, EditMessageText, EditMessageCaption,
                                 EditMessageMedia, EditMessageReplyMarkup)):
            r = data['result']
            if isinstance(r, bool):
                result = r
            else:
                result = Message.parse(r)
        elif isinstance(method, StopPoll):
            result = Poll.parse(data['result'])
        elif isinstance(method, SendMediaGroup):
            result = [Message.parse(r) for r in data['result']]
        elif isinstance(method, GetUserProfilePhotos):
            result = UserProfilePhotos.parse(data['result'])
        elif isinstance(method, (GetFile, UploadStickerFile)):
            result = File.parse(data['result'])
        elif isinstance(method, GetChat):
            result = Chat.parse(data['result'])
        elif isinstance(method, GetChatMember):
            result = ChatMember.parse(data['result'])
        elif isinstance(method, GetChatAdministrators):
            result = [ChatMember.parse(r) for r in data['result']]
        elif isinstance(method, GetStickerSet):
            result = StickerSet.parse(data['result'])
        elif isinstance(method, GetGameHighScores):
            result = [GameHighScore.parse(r) for r in data['result']]

        assert result is not None, "Should have value here! This probably means api was changed."

        return cls(method, data, ok, error_code, description, result, parameters)
