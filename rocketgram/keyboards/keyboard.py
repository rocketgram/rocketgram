# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from itertools import accumulate, chain, cycle, repeat
from typing import List, Tuple, Union

from . import errors

MIN_BUTTONS = 1
MAX_BUTTONS = 8


def _check_scheme_values(*args):
    for l in args:
        for i in l:
            if i < MIN_BUTTONS or i > MAX_BUTTONS:
                return False
    return True


def _check_scheme_types(*args):
    for i in args:
        if not isinstance(i, (list, tuple)):
            return False
    return True


class Keyboard:
    __slots__ = ('_buttons',)

    def __init__(self):
        self._buttons = list()

    def __assing_buttons(self, keyboard):
        btns = chain.from_iterable([p + q for p, q in zip(keyboard, repeat([None]))])
        self._buttons = list(btns)[:-1]

    def arrange_scheme(self, head: Union[None, int, List, Tuple] = None,
                       middle: Union[None, int, List, Tuple] = 1,
                       tail: Union[None, int, List, Tuple] = None):

        head = [] if head is None else head
        middle = [] if middle is None else middle
        tail = [] if tail is None else tail

        head = [head] if isinstance(head, int) else head
        middle = [middle] if isinstance(middle, int) else middle
        tail = [tail] if isinstance(tail, int) else tail

        if not _check_scheme_types(head, middle, tail):
            raise TypeError('Scheme values must be list or tuple')

        if not _check_scheme_values(head, middle, tail):
            raise errors.TooManyButtonsError('Too many buttons in a row. Must be from 1 to 8')

        btns = [b for b in self._buttons if b]

        if sum(head) + sum(tail) > len(btns):
            raise errors.NotEnoughButtonsError('Not egnought buttons to render scheme')

        head_btns = btns[:sum(head)]
        middle_btns = btns[sum(head):-sum(tail) if sum(tail) > 0 else None]
        tail_btns = btns[-sum(tail):]

        head_part = [head_btns[p:q] for p, q in zip(accumulate(chain([0], head)), accumulate(head))]

        middle_part = list()
        m = zip(accumulate(chain([0], cycle(middle))), accumulate(cycle(middle)))
        while True:
            p, q = next(m)
            part = middle_btns[p:q]
            if len(part):
                middle_part.append(part)
            else:
                break

        tail_part = [tail_btns[p:q] for p, q in zip(accumulate(chain([0], tail)), accumulate(tail))]

        self.__assing_buttons(chain(head_part + middle_part + tail_part))

        return self

    def arrange_simple(self, row: int = 8):
        if row < MIN_BUTTONS or row > MAX_BUTTONS:
            raise errors.TooManyButtonsError('Too many buttons in a row')

        btns = [b for b in self._buttons if b]
        l = len(btns) if len(btns) < row else row
        keyboard = [btns[i:i + row] for i in range(0, len(btns), row)]

        self.__assing_buttons(keyboard)

        return self

    def row(self):
        if len(self._buttons) and self._buttons[-1]:
            self._buttons.append(None)
        return self

    def render(self) -> List[List]:
        keyboard = list(list())
        cnt = 0
        for b in self._buttons:
            if b:
                if len(keyboard) < cnt + 1:
                    keyboard.append(list())
                keyboard[cnt].append(b)

                if len(keyboard[cnt]) > MAX_BUTTONS:
                    raise errors.TooManyButtonsError('Too many buttons in a row')
            else:
                cnt += 1

        return keyboard

    def add(self, button):
        self._buttons.append(button)
