# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import Any, List, Optional

from .input_media_animation import InputMediaAnimation
from .input_media_audio import InputMediaAudio
from .input_media_photo import InputMediaPhoto
from .input_media_video import InputMediaVideo
from .input_media_voice_note import InputMediaVoiceNote
from .input_rich_block_list_item import InputRichBlockListItem
from .location import Location
from .rich_block_caption import RichBlockCaption
from .rich_block_table_cell import RichBlockTableCell


@dataclass(frozen=True)
class InputRichBlock:
    """\
    Represents InputRichBlock object:
    https://core.telegram.org/bots/api#inputrichblock
    """


@dataclass(frozen=True)
class InputRichBlockParagraph(InputRichBlock):
    text: Any
    type: str = field(init=False, default='paragraph')


@dataclass(frozen=True)
class InputRichBlockSectionHeading(InputRichBlock):
    text: Any
    size: int
    type: str = field(init=False, default='heading')


@dataclass(frozen=True)
class InputRichBlockPreformatted(InputRichBlock):
    text: Any
    language: Optional[str] = None
    type: str = field(init=False, default='pre')


@dataclass(frozen=True)
class InputRichBlockFooter(InputRichBlock):
    text: Any
    type: str = field(init=False, default='footer')


@dataclass(frozen=True)
class InputRichBlockDivider(InputRichBlock):
    type: str = field(init=False, default='divider')


@dataclass(frozen=True)
class InputRichBlockMathematicalExpression(InputRichBlock):
    expression: str
    type: str = field(init=False, default='mathematical_expression')


@dataclass(frozen=True)
class InputRichBlockAnchor(InputRichBlock):
    name: str
    type: str = field(init=False, default='anchor')


@dataclass(frozen=True)
class InputRichBlockList(InputRichBlock):
    items: List[InputRichBlockListItem]
    type: str = field(init=False, default='list')


@dataclass(frozen=True)
class InputRichBlockBlockQuotation(InputRichBlock):
    blocks: List[InputRichBlock]
    credit: Optional[Any] = None
    type: str = field(init=False, default='blockquote')


@dataclass(frozen=True)
class InputRichBlockPullQuotation(InputRichBlock):
    text: Any
    credit: Optional[Any] = None
    type: str = field(init=False, default='pullquote')


@dataclass(frozen=True)
class InputRichBlockCollage(InputRichBlock):
    blocks: List[InputRichBlock]
    caption: Optional[RichBlockCaption] = None
    type: str = field(init=False, default='collage')


@dataclass(frozen=True)
class InputRichBlockSlideshow(InputRichBlock):
    blocks: List[InputRichBlock]
    caption: Optional[RichBlockCaption] = None
    type: str = field(init=False, default='slideshow')


@dataclass(frozen=True)
class InputRichBlockTable(InputRichBlock):
    cells: List[List[RichBlockTableCell]]
    is_bordered: Optional[bool] = None
    is_striped: Optional[bool] = None
    caption: Optional[Any] = None
    type: str = field(init=False, default='table')


@dataclass(frozen=True)
class InputRichBlockDetails(InputRichBlock):
    summary: Any
    blocks: List[InputRichBlock]
    is_open: Optional[bool] = None
    type: str = field(init=False, default='details')


@dataclass(frozen=True)
class InputRichBlockMap(InputRichBlock):
    location: Location
    zoom: int
    width: int
    height: int
    caption: Optional[RichBlockCaption] = None
    type: str = field(init=False, default='map')


@dataclass(frozen=True)
class InputRichBlockAnimation(InputRichBlock):
    animation: InputMediaAnimation
    caption: Optional[RichBlockCaption] = None
    type: str = field(init=False, default='animation')


@dataclass(frozen=True)
class InputRichBlockAudio(InputRichBlock):
    audio: InputMediaAudio
    caption: Optional[RichBlockCaption] = None
    type: str = field(init=False, default='audio')


@dataclass(frozen=True)
class InputRichBlockPhoto(InputRichBlock):
    photo: InputMediaPhoto
    caption: Optional[RichBlockCaption] = None
    type: str = field(init=False, default='photo')


@dataclass(frozen=True)
class InputRichBlockVideo(InputRichBlock):
    video: InputMediaVideo
    caption: Optional[RichBlockCaption] = None
    type: str = field(init=False, default='video')


@dataclass(frozen=True)
class InputRichBlockVoiceNote(InputRichBlock):
    voice_note: InputMediaVoiceNote
    caption: Optional[RichBlockCaption] = None
    type: str = field(init=False, default='voice_note')


@dataclass(frozen=True)
class InputRichBlockThinking(InputRichBlock):
    text: Any
    type: str = field(init=False, default='thinking')
