# Changelog
All notable changes to this project.


## [Unreleased]

### Changed
- Final fix optional module imports.


## [1.3] - 2019-07-13

### Added
- Added new context2 context helpers.

### Changed
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
