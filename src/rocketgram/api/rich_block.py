# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field
from typing import Any, List, Optional

from .animation import Animation
from .audio import Audio
from .location import Location
from .photo_size import PhotoSize
from .rich_block_caption import RichBlockCaption
from .rich_block_list_item import RichBlockListItem
from .rich_block_table_cell import RichBlockTableCell
from .rich_text import RichText
from .video import Video
from .voice import Voice


@dataclass(frozen=True)
class RichBlock:
    """\
    Represents RichBlock and its supported object variants:
    https://core.telegram.org/bots/api#richblock
    """

    @classmethod
    def parse(cls, data: dict) -> Optional['RichBlock']:
        if data is None:
            return None

        rich_block_class = _RICH_BLOCK_CLASSES.get(data.get('type'))
        if rich_block_class is None:
            return None
        return rich_block_class.parse(data)


@dataclass(frozen=True)
class RichBlockParagraph(RichBlock):
    text: Any
    type: str = field(init=False, default='paragraph')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockParagraph':
        return cls(RichText.parse(data['text']))


@dataclass(frozen=True)
class RichBlockSectionHeading(RichBlock):
    text: Any
    size: int
    type: str = field(init=False, default='heading')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockSectionHeading':
        return cls(RichText.parse(data['text']), data['size'])


@dataclass(frozen=True)
class RichBlockPreformatted(RichBlock):
    text: Any
    language: Optional[str] = None
    type: str = field(init=False, default='pre')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockPreformatted':
        return cls(RichText.parse(data['text']), data.get('language'))


@dataclass(frozen=True)
class RichBlockFooter(RichBlock):
    text: Any
    type: str = field(init=False, default='footer')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockFooter':
        return cls(RichText.parse(data['text']))


@dataclass(frozen=True)
class RichBlockDivider(RichBlock):
    type: str = field(init=False, default='divider')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockDivider':  # noqa
        return cls()


@dataclass(frozen=True)
class RichBlockMathematicalExpression(RichBlock):
    expression: str
    type: str = field(init=False, default='mathematical_expression')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockMathematicalExpression':
        return cls(data['expression'])


@dataclass(frozen=True)
class RichBlockAnchor(RichBlock):
    name: str
    type: str = field(init=False, default='anchor')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockAnchor':
        return cls(data['name'])


@dataclass(frozen=True)
class RichBlockList(RichBlock):
    items: List[RichBlockListItem]
    type: str = field(init=False, default='list')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockList':
        return cls([RichBlockListItem.parse(d) for d in data['items']])


@dataclass(frozen=True)
class RichBlockBlockQuotation(RichBlock):
    blocks: List[RichBlock]
    credit: Optional[Any] = None
    type: str = field(init=False, default='blockquote')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockBlockQuotation':
        return cls(
            [RichBlock.parse(d) for d in data['blocks']],
            RichText.parse(data.get('credit')),
        )


@dataclass(frozen=True)
class RichBlockPullQuotation(RichBlock):
    text: Any
    credit: Optional[Any] = None
    type: str = field(init=False, default='pullquote')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockPullQuotation':
        return cls(RichText.parse(data['text']), RichText.parse(data.get('credit')))


@dataclass(frozen=True)
class _RichBlockCollection(RichBlock):
    blocks: List[RichBlock]
    caption: Optional[RichBlockCaption] = None

    @classmethod
    def parse(cls, data: dict):
        return cls(
            [RichBlock.parse(d) for d in data['blocks']],
            RichBlockCaption.parse(data.get('caption')),
        )


@dataclass(frozen=True)
class RichBlockCollage(_RichBlockCollection):
    type: str = field(init=False, default='collage')


@dataclass(frozen=True)
class RichBlockSlideshow(_RichBlockCollection):
    type: str = field(init=False, default='slideshow')


@dataclass(frozen=True)
class RichBlockTable(RichBlock):
    cells: List[List[RichBlockTableCell]]
    is_bordered: Optional[bool] = None
    is_striped: Optional[bool] = None
    caption: Optional[Any] = None
    type: str = field(init=False, default='table')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockTable':
        return cls(
            [[RichBlockTableCell.parse(cell) for cell in row] for row in data['cells']],
            data.get('is_bordered'),
            data.get('is_striped'),
            RichText.parse(data.get('caption')),
        )


@dataclass(frozen=True)
class RichBlockDetails(RichBlock):
    summary: Any
    blocks: List[RichBlock]
    is_open: Optional[bool] = None
    type: str = field(init=False, default='details')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockDetails':
        return cls(
            RichText.parse(data['summary']),
            [RichBlock.parse(d) for d in data['blocks']],
            data.get('is_open'),
        )


@dataclass(frozen=True)
class RichBlockMap(RichBlock):
    location: Location
    zoom: int
    width: int
    height: int
    caption: Optional[RichBlockCaption] = None
    type: str = field(init=False, default='map')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockMap':
        return cls(
            Location.parse(data['location']),
            data['zoom'],
            data['width'],
            data['height'],
            RichBlockCaption.parse(data.get('caption')),
        )


@dataclass(frozen=True)
class RichBlockAnimation(RichBlock):
    animation: Animation
    has_spoiler: Optional[bool] = None
    caption: Optional[RichBlockCaption] = None
    type: str = field(init=False, default='animation')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockAnimation':
        return cls(
            Animation.parse(data['animation']),
            data.get('has_spoiler'),
            RichBlockCaption.parse(data.get('caption')),
        )


@dataclass(frozen=True)
class RichBlockAudio(RichBlock):
    audio: Audio
    caption: Optional[RichBlockCaption] = None
    type: str = field(init=False, default='audio')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockAudio':
        return cls(Audio.parse(data['audio']), RichBlockCaption.parse(data.get('caption')))


@dataclass(frozen=True)
class RichBlockPhoto(RichBlock):
    photo: List[PhotoSize]
    has_spoiler: Optional[bool] = None
    caption: Optional[RichBlockCaption] = None
    type: str = field(init=False, default='photo')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockPhoto':
        return cls(
            [PhotoSize.parse(d) for d in data['photo']],
            data.get('has_spoiler'),
            RichBlockCaption.parse(data.get('caption')),
        )


@dataclass(frozen=True)
class RichBlockVideo(RichBlock):
    video: Video
    has_spoiler: Optional[bool] = None
    caption: Optional[RichBlockCaption] = None
    type: str = field(init=False, default='video')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockVideo':
        return cls(
            Video.parse(data['video']),
            data.get('has_spoiler'),
            RichBlockCaption.parse(data.get('caption')),
        )


@dataclass(frozen=True)
class RichBlockVoiceNote(RichBlock):
    voice_note: Voice
    caption: Optional[RichBlockCaption] = None
    type: str = field(init=False, default='voice_note')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockVoiceNote':
        return cls(Voice.parse(data['voice_note']), RichBlockCaption.parse(data.get('caption')))


@dataclass(frozen=True)
class RichBlockThinking(RichBlock):
    text: Any
    type: str = field(init=False, default='thinking')

    @classmethod
    def parse(cls, data: dict) -> 'RichBlockThinking':
        return cls(RichText.parse(data['text']))


_RICH_BLOCK_CLASSES = {
    'paragraph': RichBlockParagraph,
    'heading': RichBlockSectionHeading,
    'pre': RichBlockPreformatted,
    'footer': RichBlockFooter,
    'divider': RichBlockDivider,
    'mathematical_expression': RichBlockMathematicalExpression,
    'anchor': RichBlockAnchor,
    'list': RichBlockList,
    'blockquote': RichBlockBlockQuotation,
    'pullquote': RichBlockPullQuotation,
    'collage': RichBlockCollage,
    'slideshow': RichBlockSlideshow,
    'table': RichBlockTable,
    'details': RichBlockDetails,
    'map': RichBlockMap,
    'animation': RichBlockAnimation,
    'audio': RichBlockAudio,
    'photo': RichBlockPhoto,
    'video': RichBlockVideo,
    'voice_note': RichBlockVoiceNote,
    'thinking': RichBlockThinking,
}
