# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import os
from dataclasses import asdict
from datetime import datetime
from enum import Enum
from logging import getLogger
from typing import Sequence, Union

import pytest
import yaml

from rocketgram import Update, UpdateType, MessageType, ChatType

logger = getLogger(__name__)


class ParsingTest:
    @staticmethod
    def collect(path: str) -> Sequence[str]:
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith('.yaml'):
                    yield os.path.relpath(os.path.join(root, file), start=path)

    def __init__(self, file_name: str):
        self._name = file_name

        with open(os.path.join(os.path.dirname(__file__), file_name), 'r') as f:
            data = yaml.safe_load(f.read())

        self._description = data['description']
        self._input = data['input']
        exp = data['expected']

        self._e_update_type = UpdateType(exp.get('update_type')) if exp.get('update_type') else None
        self._e_message_type = MessageType(exp.get('message_type')) if exp.get('message_type') else None
        self._e_chat_type = ChatType(exp.get('chat_type')) if exp.get('chat_type') else None

        self._e_output = exp['output']

    @property
    def name(self) -> str:
        return self._name

    @property
    def input(self) -> dict:
        return self._input

    def compare(self, update: Update):
        if self._e_update_type:
            assert update.type == self._e_update_type, f"Update type mismatch"
        if self._e_message_type:
            assert update.message.type == self._e_message_type, f"Message type mismatch"
        if self._e_chat_type:
            assert update.message.chat.type == self._e_chat_type, f"Chat type mismatch"

        update_dict = asdict(update)
        assert update_dict['raw'] == self._input, f"`raw` field is not equal to `input`"
        del update_dict['raw']

        self._check_extra_fields(update_dict, self._e_output)

    @classmethod
    def _check_extra_fields(cls, element: Union[dict, list, tuple], expected: Union[dict, list, tuple], path: str = ''):
        if isinstance(element, (list, tuple)):
            for i in range(len(expected)):
                cls._check_extra_fields(element[i], expected[i], f"{path}{i}.")
            return

        # Check extra fields
        for k in set(element.keys()) - set(expected.keys()):
            assert element[k] is None, f"Field `{path}{k}` is none"

        # Check expected fields
        for k, ev in expected.items():
            v = element.get(k)

            if isinstance(v, dict):
                cls._check_extra_fields(element[k], expected[k], f"{path}{k}.")
                continue

            if isinstance(v, Enum):
                v = v.value
            elif isinstance(v, datetime):
                v = v.isoformat()

            if isinstance(ev, list):
                for i in range(len(ev)):
                    cls._check_extra_fields(element[k][i], expected[k][i], f"{path}{k}.{i}.")
                continue

            assert ev == v, f"Field `{path}{k}`: expected `{ev}`, got `{v}`"


@pytest.fixture(scope="module", params=ParsingTest.collect(os.path.dirname(__file__)))
def parsing_test(request):
    return ParsingTest(request.param)


@pytest.mark.api
def test_parsing(parsing_test: ParsingTest):
    logger.debug("Parsing test: %s", parsing_test.name)
    parsing_test.compare(Update.parse(parsing_test.input))
