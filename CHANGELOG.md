# Changelog
All notable changes to this project.


## [Unreleased]

### Added
- The `commonfilters.gamne` filter.

### Changed.
- The Framework now corresponds to Telegram Bot API 6.7.
- The parameter `executor` is now optional for `init`, `shutdown` and `process` methodds of `Bot` class.
- Tz-aware datetime objects are now used instead of raw datetime objects.

### Fixed
- The `commonfilters.callback` filter for case where `game` event has arrived.

### Deprecated
- The next major release will no longer officially support Python 3.7.
- All lists in api classes will be replaced with tuples in the next major version.


## [5.0.1] - 2023-07-03

### Fixed
- default parameters in `AnswerPreCheckoutQuery`.
- default parameters in `AnswerShippingQuery`.
- default parameters in `DeleteMyCommands`.
- default parameters in `GetChatMenuButton`.
- default parameters in `GetMyCommands`.
- default parameters in `SetChatDescription`.
- default parameters in `SetMyDescription`.
- default parameters in `UnbanChatMember`.


## [5.0.0] - 2023-03-11

### Added
- the field `is_forum` to the class `Chat`.
- the fields `is_topic_message` and `message_thread_id` to the class `Message`.
- the fields `forum_topic_created`, `forum_topic_closed` and `forum_topic_reopened` to the class `Message`.
- the classes `ForumTopicCreated`, `ForumTopicClosed`, and `ForumTopicReopened`.
- the field `can_manage_topics` to the classes `ChatAdministratorRights`, `ChatPermissions` and `ChatMember`.
- the parameter `can_manage_topics` to the method `promoteChatMember`.
- the `ForumTopic` class.
- the request classes `CreateForumTopic`, `EditForumTopic`, `CloseForumTopic`, `ReopenForumTopic`, `DeleteForumTopic`, `UnpinAllForumTopicMessages`, and `GetForumTopicIconStickers` for forum topic management.
- the parameter `message_thread_id` to the request classes `SendMessage`, `SendPhoto`, `SendVideo`, `SendAnimation`, `SendAudio`, `SendDocument`, `SendSticker`, `SendVideoNote`, `SendVoice`, `SendLocation`, `SendVenue`, `SendContact`, `SendPoll`, `SendDice`, `SendInvoice`, `SendGame`, `SendMediaGroup`, `CopyMessage`, `ForwardMessage`.
- support for Multiple Usernames via the field `active_usernames` in the class `Chat`.
- the field `emoji_status_custom_emoji_id` to the class `Chat`.
- the field `is_persistent` to the class `ReplyKeyboardMarkup` and persistent parameter to the `ReplyKeyboard` helper class, allowing to control when the keyboard is shown.
- the parameter `has_spoiler` to the request classes `SendPhoto`, `SendVideo`, and `SendAnimation`.
- the field `has_spoiler` to the classes `InputMediaPhoto`, `InputMediaVideo`, and `InputMediaAnimation`.
- the field `has_media_spoiler` to the class `Message`.
- the classes `ForumTopicEdited`, `GeneralForumTopicHidden`, `GeneralForumTopicUnhidden`, and `WriteAccessAllowed` and the fields `forum_topic_edited`, `general_forum_topic_hidden`, `general_forum_topic_unhidden`, and `write_access_allowed` to the class Message.
- the methods `EditGeneralForumTopic`, `CloseGeneralForumTopic`, `ReopenGeneralForumTopic`, `HideGeneralForumTopic`, `UnhideGeneralForumTopic` for managing the General topic in forums.
- the parameter `message_thread_id` to the method `SendChatAction` for sending chat actions to a specific message thread or a forum topic.
- the field `has_hidden_members` and `has_aggressive_anti_spam_enabled` to the class `Chat`.
- the class `KeyboardButtonRequestUser` and the field `request_user` to the class `KeyboardButton`.
- the class `KeyboardButtonRequestChat` and the field `request_chat` to the class `KeyboardButton`.
- the classes `UserShared`, `ChatShared` and the fields `user_shared`, and `chat_shared` to the class `Message`.
- the parameter `use_independent_chat_permissions` to the request classes `RestrictChatMember` and `SetChatPermissions`.
- the field `user_chat_id` to the class `ChatJoinRequest`.
- the request classes `setMyDescription`, `getMyDescription`, `setMyShortDescription` and `getMyShortDescription`.
- the classes `BotDescription` and `BotShortDescription`.
- the parameter `emoji` to the method `SendSticker` to specify an emoji for just uploaded stickers.
- the parameter `needs_repainting` to the method `CreateNewStickerSet` to automatically change the color of emoji based on context.
- the field `needs_repainting` to the class `Sticker`.
- the request class `SetCustomEmojiStickerSetThumbnail` for editing the thumbnail of custom emoji sticker sets created by the bot.
- the request class `SetStickerSetTitle` for editing the title of sticker sets created by the bot.
- the request class `DeleteStickerSet` for complete deletion of a given sticker set that was created by the bot.
- the request class `SetStickerEmojiList` for changing the list of emoji associated with a sticker.
- the request class `SetStickerKeywords` for changing the search keywords assigned to a sticker.
- the request class `SetStickerMaskPosition` for changing the mask position of a mask sticker.
- the request class `SetStickerMaskPosition` for changing the mask position of a mask sticker.

### Changed.
- Framework is now corresponds to Telegram Bot API 6.3.
- Framework is now corresponds to Telegram Bot API 6.4.
- Framework is now corresponds to Telegram Bot API 6.5.
- Replaced the fields `can_send_media_messages` in the classes `ChatMember` and `ChatPermissions` with separate fields `can_send_audios`, `can_send_documents`, `can_send_photos`, `can_send_videos`, `can_send_video_notes`, and `can_send_voice_notes` for different media types.
- Replaced the parameters `png_sticker`, `tgs_sticker`, `webm_sticker`, `emojis` and `mask_position` in the request class `CreateNewStickerSet` with the parameters `stickers` and `sticker_format`.
- Replaced the parameters `png_sticker`, `tgs_sticker`, `webm_sticker`, `emojis` and `mask_position` in the request class `AddStickerToSet` with the parameter sticker of the type `InputSticker`.
- Replaced the parameter `png_sticker` in the request class `UploadStickerFile` with the parameters `sticker` and `sticker_format`.
- Renamed the field `thumb` in the classes `Animation`, `Audio`, `Document`, `Sticker`, `Video`, `VideoNote`, `InputMediaAnimation`, `InputMediaAudio`, `InputMediaDocument`, `InputMediaVideo`, `StickerSet` to `thumbnail`.
- Renamed the parameter `thumb` in the request classes `SendAnimation`, `SendAudio`, `SendDocument`, `SendVideo`, `SendVideoNote` to `thumbnail`.
- Renamed the request class `SetStickerSetThumb` to `SetStickerSetThumbnail` and its parameter `thumb` to `thumbnail`.
- Renamed the fields `thumb_url`, `thumb_width`, and `thumb_height` in the classes `InlineQueryResultArticle`, `InlineQueryResultContact`, `InlineQueryResultDocument`, `InlineQueryResultLocation`, and `InlineQueryResultVenue` to `thumbnail_url`, `thumbnail_width`, and `thumbnail_height` respectively.
- Renamed the field `thumb_url` in the classes `InlineQueryResultPhoto` and `InlineQueryResultVideo` to `thumbnail_url`.
- Renamed the fields `thumb_url` and `thumb_mime_type` in the classes `InlineQueryResultGif`, and `InlineQueryResultMpeg4Gif` to `thumbnail_url` and `thumbnail_mime_type` respectively.
- Framework is now corresponds to Telegram Bot API 6.6.
- `Executor` are now available in `init` and `shutdown` events through `context`.

### Fixed
- `WebhookInfo` parsing issue.
- Crush on shutdown.

### Removed
- `can_send_media_messages` from classes `ChatMember` and `ChatPermissions`.
- `contains_masks` from the class `StickerSet`.


## [4.1.1] - 2022-11-05

### Fixed
- Removed redundant Timeout exception.


## [4.1.0] - 2022-08-19

### Added
- The `EntityType.custom_emoji` entity type.
- The field custom_emoji_id to the class MessageEntity.
- The field `has_restricted_voice_and_video_messages` to the class `Chat`.
- The `StickerType` enum.
- The `GetCustomEmojiStickers` request class.
- The field `custom_emoji_id` to the class `Sticker`. 
- The field `sticker_type` to `StickerSet` and `CreateNewStickerSet` classes. 

### Changed.
- Framework is now corresponds to Telegram Bot API 6.2.

### Deprecated
- `StickerSet.contains_masks` is deprecated and will be removed in version 5.
- `CreateNewStickerSet.contains_masks` is deprecated and will be removed in version 5.


## [4.0.1] - 2022-07-16

### Fixed
- The `Sticker` class.


## [4.0.0] - 2022-06-25

### Added
- `orjson` support version `3.6.8` and above.
- Adapter classes to be able to explicitly select a json parser.
- The fields `join_to_send_messages` and `join_by_request` to the class `Chat`.
- The `CreateInvoiceLink` request class.
- The field `is_premium` to the class `User`. 
- The field `premium_animation` to the class `Sticker`.
- The field `added_to_attachment_menu` to the class `User`. 
- The field `secret_token` to the class `SetWebhook`.
- The `secret_token` parameter to `__init__`, `add_bot` and `run` functions in `WebhookExecutor` executor class.
- The `secret_token` parameter to the `run` function in `AioHttpExecutor` executor class.

### Changed
- The minimum required version of `aiohttp` is now `3.8.1`.
- The minimum required version of `ujson` is now `5.2.0`.
- Framework is now corresponds to Telegram Bot API 6.1.

### Fixed
- The `SendInvoice` request class.

### Removed
- Tornado support: `TornadoExecutor` and `TornadoConnector` classes.
- `VoiceChatStarted` class.
- `VoiceChatScheduled` class.
- `VoiceChatParticipantsInvited` class.
- `VoiceChatEnded` class.
- `user_id` field from `User` class.
- `update_type` field from `Update` class.
- `query_id` field from `ShippingQuery` class.
- `send2` method from `Request` and child classes.
- `can_manage_voice_chats` field from `PromoteChatMember` class.
- `query_id` field from `PreCheckoutQuery` class.
- `pool_id` and `poll_type` fields from `Poll` class.
- `entity_type` field from `MessageEntity` class.
- `voice_chat_scheduled`, `voice_chat_started`, `voice_chat_ended`, `voice_chat_participants_invited` and `message_type` fields from `Message` class.
- `query_id` field from `InlineQuery` class.
- `encrypted_passport_element_type` field from `EncryptedPassportElement` class.
- `can_manage_voice_chats` field from `ChatMember` class.
- `chat_id` and `chat_type` fields from `Chat` class.
- `query_id` field from `CallbackQuery` class.
- `voice_chat_scheduled`, `voice_chat_started`, `voice_chat_ended` and `voice_chat_participants_invited` variants from `MessageType` enum class.
- `GetChatMembersCount` class.
- `KickChatMember` class.


## [3.7.0] - 2022-04-22

### Added
- `RocketgramNetworkTimeoutError` exception class.
- `WebAppInfo` class.
- `web_app` field to `KeyboardButton` and `InlineKeyboardButton` classes.
- `web` method to `ReplyKeyboard` and `InlineKeyboard` keyboard classes.
- `WebAppData` class.
- `web_app_data` field to `Message` class.
- `MessageType.web_app_data` message type.
- `MenuButtonCommands`, `MenuButtonDefault` and `MenuButtonWebApp` classes.
- `SetChatMenuButton` and `GetChatAdministrators` request classes.
- `ChatAdministratorRights` class.
- `SetMyDefaultAdministratorRights` and `GetMyDefaultAdministratorRights` request classes.
- `last_synchronization_error_date` field to `WebhookInfo` class.
- `MessageType.voice_chat_scheduled` message type.
- `MessageType.voice_chat_started` message type.
- `MessageType.voice_chat_ended` message type.
- `MessageType.voice_chat_participants_invited` message type.
- `voice_chat_scheduled` field to `Message` class.
- `voice_chat_started` field to `Message` class.
- `voice_chat_ended` field to `Message` class.
- `voice_chat_participants_invited` field to `Message` class.
- `can_manage_voice_chats` field to `ChatMember` class.
- `can_manage_voice_chats` field to `PromoteChatMember` class.
- `AnswerWebAppQuery` request class.
- `SentWebAppMessage` class.

### Changed
- Framework is now corresponds to Telegram Bot API 6.0.

### Fixed
- Avoid throwing unnecessary `RocketgramNetworkError` exceptions in poll mode.
- Replaced deprecated `Task.all_tasks` call to `asyncio.all_tasks` call.
- Typing in middlewares.

### Deprecated
- `TornadoConnector` is deprecated and will be removed in version 4.
- `TornadoExecutor` is deprecated and will be removed in version 4.
- `VoiceChatStarted` is deprecated and will be removed in version 4.
- `VoiceChatEnded` is deprecated and will be removed in version 4.
- `VoiceChatParticipantsInvited` is deprecated and will be removed in version 4.
- `VoiceChatScheduled` is deprecated and will be removed in version 4.
- `MessageType.voice_chat_scheduled` is deprecated and will be removed in version 4.
- `MessageType.voice_chat_started` is deprecated and will be removed in version 4.
- `MessageType.voice_chat_ended` is deprecated and will be removed in version 4.
- `MessageType.voice_chat_participants_invited` is deprecated and will be removed in version 4.
- `Message.voice_chat_scheduled` is deprecated and will be removed in version 4.
- `Message.voice_chat_started` is deprecated and will be removed in version 4.
- `Message.voice_chat_ended` is deprecated and will be removed in version 4.
- `Message.voice_chat_participants_invited` is deprecated and will be removed in version 4.
- `ChatMember.can_manage_voice_chats` is deprecated and will be removed in version 4.
- `PromoteChatMember.can_manage_voice_chats` is deprecated and will be removed in version 4.


## [3.6.0] - 2022-02-16

### Added
- `webm_sticker` field to `CreateNewStickerSet` and `AddStickerToSet` request classes.
- `is_video` field to `Sticker` and `StickerSet` classes.

### Changed
- Framework is now corresponds to Telegram Bot API 5.7.

### Fixed
- Added missed `is_animated` field to `StickerSet` class.


## [3.5.0] - 2022-01-08

### Added
- `ChatType.sender` and `ChatType.unknown` variants.
- `RocketgramRequest403Error` exception class.
- `ChatActionType.choose_sticker`. 
- `ApproveChatJoinRequest` request class.
- `DeclineChatJoinRequest` request class.
- `ChatJoinRequest` class.
- `chat_join_request` field to `Update` class.
- `chat_join_request` to `UpdateType`.
- `creates_join_request` field to `ChatInviteLink` class.
- `name` field to `ChatInviteLink` class.
- `pending_join_request_count` field to `ChatInviteLink` class.
- `name` field to `CreateChatInviteLink` and `EditChatInviteLink` request classes.
- `creates_join_request` field to `CreateChatInviteLink` and `EditChatInviteLink` request classes.
- `BanChatSenderChat` request class.
- `UnbanChatSenderChat` request class.
- `has_private_forwards` field to `Chat` class.
- `message_auto_delete_time` field to `Chat` class.
- `has_protected_content` field to `Chat` class.
- `has_protected_content` field to `Message` class.
- `is_automatic_forward` field to `Message` class.
- support of `spoiler` entity type.
- `protect_content` field to several request classes.

### Changed
- Framework is now corresponds to Telegram Bot API 5.4.
- Framework is now corresponds to Telegram Bot API 5.5.
- Framework is now corresponds to Telegram Bot API 5.6.

### Fixed
- The `command` and `deeplink` filters now only catch messages with `UpdateType.message`.
- The typing for `context` object.
- `chat_type` field parsing for inline queries in case when the query is made from a secret chat.
- Escaping text there are no entities in the message.


## [3.4.0] - 2021-08-07

### Deprecated
- `MessageEntity.entity_type` is deprecated and will be removed in version 4. Use `MessageEntity.type` instead.
- `CallbackQuery.query_id` is deprecated and will be removed in version 4. Use `CallbackQuery.id` instead.
- `Chat.chat_id` is deprecated and will be removed in version 4. Use `Chat.id` instead.
- `Chat.chat_type` is deprecated and will be removed in version 4. Use `Chat.type` instead.
- `EncryptedPassportElement.encrypted_passport_element_type` is deprecated and will be removed in version 4. Use `EncryptedPassportElement.type` instead.
- `InlineQuery.query_id` is deprecated and will be removed in version 4. Use `InlineQuery.id` instead.
- `Message.message_type` is deprecated and will be removed in version 4. Use `Message.type` instead.
- `Poll.pool_id` is deprecated and will be removed in version 4. Use `Poll.id` instead.
- `Poll.poll_type` is deprecated and will be removed in version 4. Use `Poll.type` instead.
- `PreCheckoutQuery.query_id` is deprecated and will be removed in version 4. Use `PreCheckoutQuery.id` instead.
- `ShippingQuery.query_id` is deprecated and will be removed in version 4. Use `ShippingQuery.id` instead.
- `User.user_id` is deprecated and will be removed in version 4. Use `User.id` instead.
- `Update.chat_type` is deprecated and will be removed in version 4. Use `Update.type` instead.

### Fixed
- Bug in entity parser tool.
- Reuse of the message entity object when sending messages.
- Typing in `CopyMessage` class.
- Missing default values in `SetMyCommands` class.
- Parser method in `InlineKeyboardMarkup` class.


## [3.3.1] - 2021-06-26

### Fixed
- bug in `Message` object.


## [3.3.0] - 2021-06-26

### Added
- `BotCommandScope` classes.
- `scope` and `language_code` fields to `GetMyCommands` request class.
- `scope` and `language_code` fields to `SetMyCommands` request class.
- `DeleteMyCommands` request class.
- `input_field_placeholder` field to `ReplyKeyboardMarkup` and `ForceReply` class.
- `placeholder` field and parameter to `ReplyKeyboard` helper class.

### Changed
- `KickChatMember` renamed to `BanChatMember`. The old method name can still be used.
- `GetChatMembersCount` renamed to `GetChatMemberCount`. The old method name can still be used.
- Framework now corresponds to Telegram Bot API 5.3.

### Deprecated
- `KickChatMember` is deprecated and will be removed in version 4.
- `GetChatMembersCount` is deprecated and will be removed in version 4.

### Fixed
- typing for `Message` object.


## [3.2.0] - 2021-05-01

### Added
- `ChatActionType.record_voice` and `ChatActionType.upload_voice`. 
- `MessageType.voice_chat_scheduled` message type.
- `voice_chat_scheduled` field to `Message` class.
- `VoiceChatScheduled` class.
- `chat_type` field to `InlineQuery` class.
- `max_tip_amount` and `suggested_tip_amounts` fields to `SendInvoice` request class.
- `InputInvoiceMessageContent` class.

### Changed
- Refactored `Connector` class and subclasses.
- `start_parameter` field of `SendInvoice` request class is now optional.
- Framework now corresponds to Telegram Bot API 5.2.

### Deprecated
- `API_URL` and `API_FILE_URL` constants is deprecated and will be removed in version 4.0. Use the appropriate constants from `Connector` class.
- `ChatActionType.record_audio` and `ChatActionType.upload_audio` types is deprecated and will be removed in version 4.0. Use `ChatActionType.record_voice` or `ChatActionType.upload_voice` instead. 


## [3.1.0] - 2021-03-27

### Added
- `allowed_updates` field to `Executor` class and subclasses.
- `certificate` and `ip_address` fields to `AioHttpExecutor` and `TornadoExecutor` classes.
- `WebhookExecutor` class that now holds common code from `AioHttpExecutor` and `TornadoExecutor` classes.
- `resolve_file_url` method to `Connector` class and subclasses.
- `api_file_url` parameter to `Connector` class and subclasses.
- `inline` and `result` context helpers.

### Fixed
- Fixed typing for base `Executor`.
- Typing for `SetWebhook` request class.
- `Context.member()` was not properly set.

### Changed
- Refactored `AiohttpExecutor`.
- A minimal version of `aiohttp` is now `3.6.2`.
- `File.url()` method now calls `Connector.resolve_file_url()` to resolve file's url.
- `Context.chat_member()` renamed to `Context.member()`


## [3.0.1] - 2021-03-14

### Fixed
- Fixed import bug.


## [3.0.0] - 2021-03-14

### Added
- `via_bot` field to `Message` class.
- `ThumbMimeType` class.
- `thumb_mime_type` field to `InlineQueryResultGif` and `InlineQueryResultMpeg4Gif` classes.
- `DiceType` class.
- `MessageId` class.
- `CopyMessage` request class.
- `caption_entities` or `entites` fields to many api classes.
- `google_place_id` and `google_place_type` fields to `Venue`, `InlineQueryResultVenue`, `InputVenueMessageContent`, `SendVenue` classes.
- `allow_sending_without_reply` field to many api classes.
- `sender_chat` field to `Message` class.
- `is_anonymous` field to `ChatMember` and `PromoteChatMember` classes.
- `live_period` field to `Location` class.
- `heading`, `proximity_alert_radius` and `horizontal_accuracy` fields to `Location`, `InlineQueryResultLocation`, `InputLocationMessageContent`, `SendLocation` and `EditMessageLiveLocation` classes.
- `ProximityAlertTriggered` class.
- `proximity_alert_triggered` field to `Message` class.
- `proximity_alert_triggered` type to `MessageType` class.
- `message_id` field to `UnpinChatMessage` request class.
- `UnpinAllChatMessages` request class.
- `file_name` field to `Audio` and `Video` classes.
- `disable_content_type_detection` field to `SendDocument` and `InputMediaDocument` classes.
- `only_if_banned` field to `UnbanChatMember` request class.
- `ChatLocation` class.
- `bio`, `linked_chat_id` and `location` fields to `Chat` class.
- `ip_address` field to `SetWebhook` and `WebhookInfo` classes.
- `drop_pending_updates` field to `SetWebhook` and `DeleteWebhook` classes.
- `LogOut` request class.
- `Close` request class.
- `my_chat_member` and `chat_member` to `UpdateType`.
- `ChatInviteLink` class.
- `ChatMemberUpdated` class.
- `my_chat_member`, `chat_member` and `unknown` fields to `Update` class.
- `CreateChatInviteLink` request class.
- `EditChatInviteLink` request class.
- `RevokeChatInviteLink` request class.
- `VoiceChatStarted` class.
- `VoiceChatEnded` class.
- `VoiceChatParticipantsInvited` class.
- `voice_chat_started`, `voice_chat_ended` and `voice_chat_participants_invited` fields to `Message` class.
- `can_manage_voice_chats` field to `ChatMember` class.
- `can_manage_voice_chats` field to `PromoteChatMember` request class.
- `MessageType.unknown` that will indicate unknown new type of message.
- `MessageAutoDeleteTimerChanged` class.
- `message_auto_delete_timer_changed` field to `Message` class.
- `message_auto_delete_timer_changed`, `voice_chat_started`, `voice_chat_ended` and `voice_chat_participants_invited` message types.
- `revoke_messages` field to `KickChatMember` request class.
- `can_manage_chat` field to `ChatMember` and `PromoteChatMember` classes.
- `context.chat_member` context helper field.

### Changed
- `SendDice` and `Dice` classes now using `DiceType`.
- `Request.send()` method implementation was replaced. Now it returns `result` directly.
- `webhook` parameter in executors is replaced with `set_webhook` or `delete_webhook`.
- `drop_updates` parameter executors is replaced with `drop_pending_updates`.
- Updates now dropping through setting corresponding parameter instead of getUpdates hack.
- Framework now corresponds to Telegram Bot API 4.9.
- Framework now corresponds to Telegram Bot API 5.0.
- Framework now corresponds to Telegram Bot API 5.1.

### Removed
- Assert in Update parser. Now unknown update types will be `UpdateType.unknown`.
- `context2`
- `Response.method`
- `BaseDispatcherProxy`
- `BaseDispatcher.from_proxy`

### Deprecated
- `Request.send2()` method is deprecated and will be removed in version 4.0. Use `Request.send()` instead.


## [2.0.1] - 2020-05-16

### Fixed
- Fixed bug in `ResponseParameters` response class.
- Fixed typing.


## [2.0] - 2020-05-02

### Added
- Added `callback` context helper.
- Added `shipping` context helper.
- Added `checkout` context helper.
- Added `poll` context helper.
- Added `answer` context helper.
- Added well typed `Request.send2()` method. This method returns result directly instead of `Response` object.
- Added well typed `Response.method` property.
- Added `File.url` property. This property return url of a file requested by `GetFile` method.
- Ability to use callable classes and instances as handlers.
- `explanation`, `explanation_entities`, `open_period`, `close_date` fields to `Poll` class.
- `explanation`, `explanation_parse_mode`, `open_period`, `close_date` fields to `sendPoll` request class.
- `emoji` field to `sendDice` request class.
- `emoji` field to `Dice` class.

### Fixed
- Minor bugfixes.

### Changed
- Refactored api.

### Removed
- Old `context` helper functions. Now `context` and `context2` is the same.

### Deprecated
- `context2` is deprecated and will be removed in version 2.3.
- `Request.send()` method is deprecated and will be removed in version 2.3. Use `Request.send2()` instead.
- `Response.method` property is deprecated and will be removed in version 2.3. Use `Response.request` instead.
- `BaseDispatcherProxy` class is deprecated and will be removed in version 3.0. Use `BaseDispatcher` instead.
- `BaseDispatcher.from_proxy` method is deprecated and will be removed in version 3.0. Use `from_dispatcher` instead.

### Changed
- Framework now corresponds to Telegram Bot API 4.8.


## [1.8] - 2020-04-11

### Added
- Added `SendDice` request class.
- Added `Dice` update class.
- Added `dice` field to `Message` class.
- Added `SetMyCommands` request class.
- Added `GetMyCommands` request class.
- Added `GetStickerSetThumb` request class.
- Added `tgs_sticker` field to `AddStickerToSet` request class.
- Added `tgs_sticker` and `thumb` fields to `StickerSet` request class.

### Changed
- Framework now corresponds to Telegram Bot API 4.7.


## [1.7] - 2020-02-29

### Added
- More typing.
- `language` field to `MessageEntity` class.
- New `PollType` class.
- `can_join_groups` field to `User` class.
- `can_read_all_group_messages` field to `User` class.
- `can_join_groups` field to `User` class.
- New `PollAnswer` class.
- New update type `poll_answer` in `UpdateType` class.
- `poll_answer` to `Update` class.
- `poll` method to `ReplyKeyboard` class.
- `is_anonymous` field to `SendPoll` request class.
- `type` field to `SendPoll` request class.
- `allows_multiple_answers` field to `SendPoll` request class.
- `correct_option_id` field to `SendPoll` request class.
- `is_closed` field to `SendPoll` request class.

### Fixed
- Bug when use middlewares.
- Bug in ChatMember object.
- `first_name` in `User` class now mandatory as expected.

### Changed
- Framework now corresponds to Telegram Bot API 4.6.


## [1.6.1] - 2020-01-04

### Fixed
- Import bug quickfix.


## [1.6] - 2020-01-04

### Added
- `Keyboard` object now can be passed to request without rendering.
- Support new entity types `underline` and `strikethrough`.
- Support parse mode type `markdownv2`.
- New `file_unique_id` field to various objects.
- New `small_file_unique_id` and `big_file_unique_id` to `ChatPhoto` object.
- New `custom_title` to `ChatMember` object.
- New `slow_mode_delay` to `Chat` object.
- New `setChatAdministratorCustomTitle` request object.
- Support nested entities.

### Fixed
- Fixed bug in webhook-reply in `TornadoExecutor`.

### Changed
- Framework now corresponds to Telegram Bot API 4.5.


## [1.5] - 2019-08-04

### Added
- `permissions` field to `RestrictChatMember` request object.
- `SetChatPermissions` request object.
- `permissions` field to `Chat` object.
- `can_send_polls` field to `ChatMember` object.
- `ChatPermissions` object.
- `is_animated` field to `Sticker` request object.

### Changed
- Framework now corresponds to Telegram Bot API 4.4.

### Removed
- `can_send_messages` field from `RestrictChatMember` request object.
- `can_send_media_messages` field from `RestrictChatMember` request object.
- `can_send_other_messages` field from `RestrictChatMember` request object.
- `can_add_web_page_previews` field from `RestrictChatMember` request object.
- `all_members_are_administrators` field from `Chat` request object.


## [1.4] - 2019-07-26

### Fixed
- Final fix optional module imports.
- Fix issue in message_type filter.
- Fix issue in Connector with the inability to send files with unicode names.


## [1.3] - 2019-07-13

### Added
- Added new context2 context helpers.

### Fixed
- Fix optional module imports.

### Deprecated
- Old context helpers is deprecated. It will be replaced with `context2` in version 2.0.


## [1.2] - 2019-06-01

### Added
- Added LoginUrl type.
- InlineKeyboardButton now accepts LoginUrl.
- Added login() method to InlineKeyboard.
- Added parse() to InlineKeyboardButton, LoginUrl InlineKeyboardMarkup.
- Added reply_markup field to Message.

### Changed
- Framework now corresponds to Telegram Bot API 4.3.


## [1.1] - 2019-05-31

### Added
- Start using "changelog".
- Added some tests.
- Added travis.
- Fixed types in types.py
- Fixed bug in EditMessageMedia.

### Changed
- context-helpers now have optional types.

### Fixed
- Fixed logger names in executor.py and aiohttp.py.
- Fixed waiters cleaner routine.
- Fixed MediaGroups's default values.


## [1.0] - 2019-04-26

### Added
- Released version 1.0.
