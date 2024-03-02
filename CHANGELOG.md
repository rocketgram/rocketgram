# Changelog
All notable changes to this project.


## [6.0.0] - 2024-03-02

### Added
- The `commonfilters.game` filter.

### Changed.
- The Framework now corresponds to Telegram Bot API 6.7.
- The Framework now corresponds to Telegram Bot API 6.8.
- The Framework now corresponds to Telegram Bot API 6.9.
- The Framework now corresponds to Telegram Bot API 7.0.
- The Framework now corresponds to Telegram Bot API 7.1.
- The parameter `executor` is now optional for `init`, `shutdown` and `process` methods of `Bot` class.
- Tz-aware datetime objects are now used instead of raw datetime objects.
- Dropped support for Python 3.7.
- The new entity parser.

### Fixed
- The `commonfilters.callback` filter for case where `game` event has arrived.
- Passing update types to `UpdatesExecutor`.

### Deprecated
- All lists in api classes will be replaced with tuples in the next major version.
