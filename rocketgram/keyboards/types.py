from dataclasses import dataclass
from typing import Optional, List


@dataclass(frozen=True)
class KeyboardButton:
    """\
    Represents KeyboardButton keyboard object:
    https://core.telegram.org/bots/api#keyboardbutton
    """

    text: str
    request_contact: Optional[bool] = None
    request_location: Optional[bool] = None


@dataclass(frozen=True)
class InlineKeyboardButton:
    """\
    Represents InlineKeyboardButton keyboard object:
    https://core.telegram.org/bots/api#inlinekeyboardbutton
    """

    text: str
    url: Optional[str] = None
    callback_data: Optional[str] = None
    switch_inline_query: Optional[str] = None
    switch_inline_query_current_chat: Optional[str] = None
    callback_game: Optional[dict] = None  # TODO: CallbackGame
    pay: Optional[bool] = None


@dataclass(frozen=True)
class ReplyKeyboardMarkup:
    """\
    Represents ReplyKeyboardMarkup keyboard object:
    https://core.telegram.org/bots/api#replykeyboardmarkup
    """

    keyboard: List[List[KeyboardButton]]
    resize_keyboard: Optional[bool] = None
    one_time_keyboard: Optional[bool] = None
    selective: Optional[bool] = None


@dataclass(frozen=True)
class InlineKeyboardMarkup:
    """\
    Represents InlineKeyboardMarkup keyboard object:
    https://core.telegram.org/bots/api#inlinekeyboardmarkup
    """

    inline_keyboard: List[List[InlineKeyboardButton]]


@dataclass(frozen=True)
class ReplyKeyboardRemove:
    """\
    Represents ReplyKeyboardRemove keyboard object:
    https://core.telegram.org/bots/api#replykeyboardremove
    """

    selective: bool = False
    remove_keyboard: bool = True


@dataclass(frozen=True)
class ForceReply:
    """\
    Represents ForceReply keyboard object:
    https://core.telegram.org/bots/api#forcereply
    """

    selective: bool = False
    force_reply: bool = True
