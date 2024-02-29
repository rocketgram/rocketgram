# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from .add_sticker_to_set import AddStickerToSet
from .animation import Animation
from .answer_callback_query import AnswerCallbackQuery
from .answer_inline_query import AnswerInlineQuery
from .answer_pre_checkout_query import AnswerPreCheckoutQuery
from .answer_shipping_query import AnswerShippingQuery
from .answer_web_app_query import AnswerWebAppQuery
from .approve_chat_join_request import ApproveChatJoinRequest
from .audio import Audio
from .ban_chat_member import BanChatMember
from .ban_chat_sender_chat import BanChatSenderChat
from .bot_command import BotCommand
from .bot_command_scope import BotCommandScope
from .bot_command_scope_all_chat_administrators import BotCommandScopeAllChatAdministrators
from .bot_command_scope_all_group_chats import BotCommandScopeAllGroupChats
from .bot_command_scope_all_private_chats import BotCommandScopeAllPrivateChats
from .bot_command_scope_chat import BotCommandScopeChat
from .bot_command_scope_chat_administrators import BotCommandScopeChatAdministrators
from .bot_command_scope_chat_member import BotCommandScopeChatMember
from .bot_command_scope_default import BotCommandScopeDefault
from .bot_description import BotDescription
from .bot_name import BotName
from .bot_short_description import BotShortDescription
from .callback_query import CallbackQuery
from .chat import Chat
from .chat_action_type import ChatActionType
from .chat_administrator_rights import ChatAdministratorRights
from .chat_boost import ChatBoost
from .chat_boost_added import ChatBoostAdded
from .chat_boost_removed import ChatBoostRemoved
from .chat_boost_source import ChatBoostSource
from .chat_boost_source_type import ChatBoostSourceType
from .chat_boost_updated import ChatBoostUpdated
from .chat_invite_link import ChatInviteLink
from .chat_join_request import ChatJoinRequest
from .chat_location import ChatLocation
from .chat_member import ChatMember
from .chat_member_status_type import ChatMemberStatusType
from .chat_member_updated import ChatMemberUpdated
from .chat_permissions import ChatPermissions
from .chat_photo import ChatPhoto
from .chat_shared import ChatShared
from .chat_type import ChatType
from .chosen_inline_result import ChosenInlineResult
from .close import Close
from .close_forum_topic import CloseForumTopic
from .close_general_forum_topic import CloseGeneralForumTopic
from .contact import Contact
from .copy_message import CopyMessage
from .create_chat_invite_link import CreateChatInviteLink
from .create_forum_topic import CreateForumTopic
from .create_invoice_link import CreateInvoiceLink
from .create_new_sticker_set import CreateNewStickerSet
from .decline_chat_join_request import DeclineChatJoinRequest
from .delete_chat_photo import DeleteChatPhoto
from .delete_chat_sticker_set import DeleteChatStickerSet
from .delete_forum_topic import DeleteForumTopic
from .delete_message import DeleteMessage
from .delete_my_commands import DeleteMyCommands
from .delete_sticker_from_set import DeleteStickerFromSet
from .delete_sticker_set import DeleteStickerSet
from .delete_webhook import DeleteWebhook
from .dice import Dice
from .dice_type import DiceType
from .document import Document
from .edit_chat_invite_link import EditChatInviteLink
from .edit_forum_topic import EditForumTopic
from .edit_general_forum_topic import EditGeneralForumTopic
from .edit_message_caption import EditMessageCaption
from .edit_message_live_location import EditMessageLiveLocation
from .edit_message_media import EditMessageMedia
from .edit_message_reply_markup import EditMessageReplyMarkup
from .edit_message_text import EditMessageText
from .encrypted_credentials import EncryptedCredentials
from .encrypted_passport_element import EncryptedPassportElement
from .encrypted_passport_element_type import EncryptedPassportElementType
from .entity_type import EntityType
from .export_chat_invite_link import ExportChatInviteLink
from .external_reply_info import ExternalReplyInfo
from .file import File
from .force_reply import ForceReply
from .forum_topic import ForumTopic
from .forum_topic_closed import ForumTopicClosed
from .forum_topic_created import ForumTopicCreated
from .forum_topic_edited import ForumTopicEdited
from .forum_topic_reopened import ForumTopicReopened
from .forward_message import ForwardMessage
from .game import Game
from .game_high_score import GameHighScore
from .general_forum_topic_hidden import GeneralForumTopicHidden
from .general_forum_topic_unhidden import GeneralForumTopicUnhidden
from .get_chat import GetChat
from .get_chat_administrators import GetChatAdministrators
from .get_chat_member import GetChatMember
from .get_chat_member_count import GetChatMemberCount
from .get_chat_menu_button import GetChatMenuButton
from .get_custom_emoji_stickers import GetCustomEmojiStickers
from .get_file import GetFile
from .get_forum_topic_icon_stickers import GetForumTopicIconStickers
from .get_game_high_scores import GetGameHighScores
from .get_me import GetMe
from .get_my_commands import GetMyCommands
from .get_my_default_administrator_rights import GetMyDefaultAdministratorRights
from .get_my_description import GetMyDescription
from .get_my_name import GetMyName
from .get_my_short_description import GetMyShortDescription
from .get_sticker_set import GetStickerSet
from .get_updates import GetUpdates
from .get_user_chat_boosts import GetUserChatBoosts
from .get_user_profile_photos import GetUserProfilePhotos
from .get_webhook_info import GetWebhookInfo
from .giveaway import Giveaway
from .giveaway_completed import GiveawayCompleted
from .giveaway_created import GiveawayCreated
from .giveaway_winners import GiveawayWinners
from .hide_general_forum_topic import HideGeneralForumTopic
from .inline_keyboard_button import InlineKeyboardButton
from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query import InlineQuery
from .inline_query_result_article import InlineQueryResultArticle
from .inline_query_result_audio import InlineQueryResultAudio
from .inline_query_result_cached_audio import InlineQueryResultCachedAudio
from .inline_query_result_cached_document import InlineQueryResultCachedDocument
from .inline_query_result_cached_gif import InlineQueryResultCachedGif
from .inline_query_result_cached_mpeg4_gif import InlineQueryResultCachedMpeg4Gif
from .inline_query_result_cached_photo import InlineQueryResultCachedPhoto
from .inline_query_result_cached_sticker import InlineQueryResultCachedSticker
from .inline_query_result_cached_video import InlineQueryResultCachedVideo
from .inline_query_result_cached_voice import InlineQueryResultCachedVoice
from .inline_query_result_contact import InlineQueryResultContact
from .inline_query_result_document import InlineQueryResultDocument
from .inline_query_result_game import InlineQueryResultGame
from .inline_query_result_gif import InlineQueryResultGif
from .inline_query_result_location import InlineQueryResultLocation
from .inline_query_result_mpeg4_gif import InlineQueryResultMpeg4Gif
from .inline_query_result_photo import InlineQueryResultPhoto
from .inline_query_result_venue import InlineQueryResultVenue
from .inline_query_result_video import InlineQueryResultVideo
from .inline_query_result_voice import InlineQueryResultVoice
from .inline_query_results_button import InlineQueryResultsButton
from .input_contact_message_content import InputContactMessageContent
from .input_file import InputFile
from .input_invoice_message_content import InputInvoiceMessageContent
from .input_location_message_content import InputLocationMessageContent
from .input_media_animation import InputMediaAnimation
from .input_media_audio import InputMediaAudio
from .input_media_document import InputMediaDocument
from .input_media_photo import InputMediaPhoto
from .input_media_video import InputMediaVideo
from .input_sticker import InputSticker
from .input_text_message_content import InputTextMessageContent
from .input_venue_message_content import InputVenueMessageContent
from .invoice import Invoice
from .keyboard_button import KeyboardButton
from .keyboard_button_poll_type import KeyboardButtonPollType
from .keyboard_button_request_chat import KeyboardButtonRequestChat
from .keyboard_button_request_users import KeyboardButtonRequestUsers
from .labeled_price import LabeledPrice
from .leave_chat import LeaveChat
from .link_preview_options import LinkPreviewOptions
from .location import Location
from .log_out import LogOut
from .login_url import LoginUrl
from .mask_position import MaskPosition
from .mask_position_point_type import MaskPositionPointType
from .menu_button_commands import MenuButtonCommands
from .menu_button_default import MenuButtonDefault
from .menu_button_web_app import MenuButtonWebApp
from .message import Message
from .message_auto_delete_timer_changed import MessageAutoDeleteTimerChanged
from .message_entity import MessageEntity
from .message_id import MessageId
from .message_origin import MessageOrigin
from .message_origin_type import MessageOriginType
from .message_reaction_count_updated import MessageReactionCountUpdated
from .message_reaction_updated import MessageReactionUpdated
from .message_type import MessageType
from .order_info import OrderInfo
from .parse_mode_type import ParseModeType
from .passport_data import PassportData
from .passport_element_error_data_field import PassportElementErrorDataField
from .passport_element_error_file import PassportElementErrorFile
from .passport_element_error_files import PassportElementErrorFiles
from .passport_element_error_front_side import PassportElementErrorFrontSide
from .passport_element_error_reverse_side import PassportElementErrorReverseSide
from .passport_element_error_selfie import PassportElementErrorSelfie
from .passport_element_error_translation_file import PassportElementErrorTranslationFile
from .passport_element_error_translation_files import PassportElementErrorTranslationFiles
from .passport_element_error_unspecified import PassportElementErrorUnspecified
from .password_file import PassportFile
from .photo_size import PhotoSize
from .pin_chat_message import PinChatMessage
from .poll import Poll
from .poll_answer import PollAnswer
from .poll_option import PollOption
from .poll_type import PollType
from .pre_checkout_query import PreCheckoutQuery
from .promote_chat_member import PromoteChatMember
from .proximity_alert_triggered import ProximityAlertTriggered
from .reaction_count import ReactionCount
from .reaction_type import ReactionType
from .reaction_type_type import ReactionTypeType
from .reopen_forum_topic import ReopenForumTopic
from .reopen_general_forum_topic import ReopenGeneralForumTopic
from .reply_keyboard_markup import ReplyKeyboardMarkup
from .reply_keyboard_remove import ReplyKeyboardRemove
from .request import Request
from .response import Response
from .response_parameters import ResponseParameters
from .restrict_chat_member import RestrictChatMember
from .revoke_chat_invite_link import RevokeChatInviteLink
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
from .sent_web_app_message import SentWebAppMessage
from .set_chat_administrator_custom_title import SetChatAdministratorCustomTitle
from .set_chat_description import SetChatDescription
from .set_chat_menu_button import SetChatMenuButton
from .set_chat_permissions import SetChatPermissions
from .set_chat_photo import SetChatPhoto
from .set_chat_sticker_set import SetChatStickerSet
from .set_chat_title import SetChatTitle
from .set_custom_emoji_sticker_set_thumbnail import SetCustomEmojiStickerSetThumbnail
from .set_game_score import SetGameScore
from .set_my_commands import SetMyCommands
from .set_my_default_administrator_rights import SetMyDefaultAdministratorRights
from .set_my_description import SetMyDescription
from .set_my_name import SetMyName
from .set_my_short_description import SetMyShortDescription
from .set_passport_data_errors import SetPassportDataErrors
from .set_sticker_emoji_list import SetStickerEmojiList
from .set_sticker_keywords import SetStickerKeywords
from .set_sticker_mask_position import SetStickerMaskPosition
from .set_sticker_position_in_set import SetStickerPositionInSet
from .set_sticker_set_thumbnail import SetStickerSetThumbnail
from .set_sticker_set_title import SetStickerSetTitle
from .set_webhook import SetWebhook
from .shipping_address import ShippingAddress
from .shipping_option import ShippingOption
from .shipping_query import ShippingQuery
from .sticker import Sticker
from .sticker_format import StickerFormat
from .sticker_set import StickerSet
from .sticker_type import StickerType
from .stop_message_live_location import StopMessageLiveLocation
from .stop_poll import StopPoll
from .story import Story
from .successful_payment import SuccessfulPayment
from .switch_inline_query_chosen_chat import SwitchInlineQueryChosenChat
from .text_quote import TextQuote
from .thumbnail_mime_type import ThumbnailMimeType
from .unban_chat_member import UnbanChatMember
from .unban_chat_sender_chat import UnbanChatSenderChat
from .unhide_general_forum_topic import UnhideGeneralForumTopic
from .unpin_all_chat_messages import UnpinAllChatMessages
from .unpin_all_forum_topic_messages import UnpinAllForumTopicMessages
from .unpin_all_general_forum_topic_messages import UnpinAllGeneralForumTopicMessages
from .unpin_chat_message import UnpinChatMessage
from .update import Update
from .update_type import UpdateType
from .upload_sticker_file import UploadStickerFile
from .user import User
from .user_chat_boosts import UserChatBoosts
from .user_profile_photos import UserProfilePhotos
from .user_shared import UserShared
from .venue import Venue
from .video import Video
from .video_chat_ended import VideoChatEnded
from .video_chat_participants_invited import VideoChatParticipantsInvited
from .video_chat_scheduled import VideoChatScheduled
from .video_chat_started import VideoChatStarted
from .video_note import VideoNote
from .voice import Voice
from .web_app_data import WebAppData
from .web_app_info import WebAppInfo
from .webhook_info import WebhookInfo
from .write_access_allowed import WriteAccessAllowed
