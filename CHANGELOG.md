# Changelog
All notable changes to this project.


## [Unreleased]


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
- Old context helpers is deprecated. It will be replaced with context2 in version 2.0.


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
