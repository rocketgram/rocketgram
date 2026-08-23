# Copyright (C) 2015-2024 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import importlib
import sys
import types
import unittest
from types import SimpleNamespace

from rocketgram import Bot, Connector, DeleteWebhook, Dispatcher, EntityType, MessageEntity, Update
from rocketgram import UpdateType
from rocketgram.context import context
from rocketgram.errors import RocketgramParseError
from rocketgram.executors import UpdatesExecutor, WebhookExecutor
from rocketgram.keyboards import InlineKeyboard, ReplyKeyboard
from rocketgram.keyboards.errors import NotEnoughButtonsError
from rocketgram.routers.dispatcher import commonfilters
from rocketgram.routers.dispatcher import commonwaiters
from rocketgram.routers.dispatcher.base import _call_or_await
from rocketgram.tools.parser import to_html, to_markdown, to_markdown_v2


def make_bot(bot_name="TestBot"):
    bot = Bot(
        "1234567890:AAgLHoRpZxIcND0EqNL15HurLzwwSKomngX",
        router=Dispatcher(),
        connector=Connector(),
    )
    bot.name = bot_name
    return bot


def make_update(text):
    return Update.parse({
        "update_id": 123456789,
        "message": {
            "message_id": 1234567,
            "from": {"id": 123, "is_bot": False, "first_name": "User"},
            "chat": {"id": 123, "type": "private"},
            "date": 1691234567,
            "text": text,
        },
    })


def make_entity(entity_type, length, **kwargs):
    return MessageEntity(
        entity_type,
        0,
        length,
        kwargs.get("url"),
        kwargs.get("user"),
        kwargs.get("language"),
        kwargs.get("custom_emoji_id"),
        None,
        None,
    )


class KeyboardRegressionTests(unittest.TestCase):
    def test_persistent_property_updates_persistent_flag(self):
        keyboard = ReplyKeyboard()
        keyboard.persistent = True

        self.assertTrue(keyboard.persistent)
        self.assertTrue(keyboard.resize)
        self.assertTrue(keyboard.render().is_persistent)

    def test_request_chat_remains_usable_with_legacy_arguments(self):
        keyboard = ReplyKeyboard().request_chat("Choose", 7, True)
        request_chat = keyboard.render().keyboard[0][0].request_chat

        self.assertFalse(request_chat.chat_is_channel)
        self.assertTrue(request_chat.chat_has_username)

    def test_game_button_renders_callback_game_object(self):
        button = InlineKeyboard().game("Play", "legacy-value").render().inline_keyboard[0][0]

        self.assertEqual(type(button.callback_game).__name__, "CallbackGame")

    def test_scheme_without_middle_rows(self):
        keyboard = ReplyKeyboard().text("Head").text("Tail")
        keyboard.arrange_scheme(head=1, middle=None, tail=1)

        self.assertEqual([[b.text for b in row] for row in keyboard.render().keyboard], [["Head"], ["Tail"]])

        with self.assertRaises(NotEnoughButtonsError):
            ReplyKeyboard().text("Head").text("Middle").text("Tail").arrange_scheme(
                head=1, middle=None, tail=1)


class DispatcherRegressionTests(unittest.TestCase):
    def test_failed_executor_setup_does_not_leave_a_registered_bot(self):
        class FailingBot:
            name = "TestBot"
            token = "token"

            def __init__(self):
                self.was_shutdown = False

            async def init(self, executor):
                pass

            async def shutdown(self, executor):
                self.was_shutdown = True

            async def send(self, request):
                raise RuntimeError("setup failed")

        async def run():
            bot = FailingBot()
            updates = UpdatesExecutor()
            with self.assertRaises(RuntimeError):
                await updates.add_bot(bot)
            self.assertEqual(updates.bots, [])
            self.assertTrue(bot.was_shutdown)

            bot = FailingBot()
            webhook = WebhookExecutor("https://example.test/", "/")
            with self.assertRaises(RuntimeError):
                await webhook.add_bot(bot)
            self.assertEqual(webhook.bots, [])
            self.assertTrue(bot.was_shutdown)

        asyncio.run(run())

    def test_slotted_class_handlers_register_once_and_run(self):
        bot = make_bot()
        results = []

        @bot.router.handler
        @commonfilters.catch_all()
        class Handler:
            __slots__ = ()

            async def __call__(self):
                results.append(context.update)

        update = make_update("message")
        asyncio.run(bot.process(None, update))

        self.assertEqual(results, [update])
        with self.assertRaises(AssertionError):
            bot.router.handler(Handler)

    def test_drop_waiter_continues_the_current_generator(self):
        bot = make_bot()
        events = []

        @bot.router.handler
        @commonfilters.catch_all()
        async def handler():
            events.append("started")
            yield commonwaiters.next_message()
            events.append("resumed")
            yield commonwaiters.drop_waiter()
            events.append("continued")

        async def run():
            await bot.process(None, make_update("first"))
            await bot.process(None, make_update("second"))

        asyncio.run(run())
        self.assertEqual(events, ["started", "resumed", "continued"])

    def test_bot_deeplink_payload_uses_the_correct_offset(self):
        bot = make_bot()
        results = []

        @bot.router.handler
        @commonfilters.deeplink("payload")
        async def handler():
            results.append(context.update)

        expected = make_update("/start@TestBot payload")
        unexpected = make_update("/start@TestBot different")

        asyncio.run(bot.process(None, expected))
        with self.assertLogs("rocketgram.dispatcher", level="WARNING"):
            asyncio.run(bot.process(None, unexpected))

        self.assertEqual(results, [expected])

    def test_call_or_await_handles_futures(self):
        async def run():
            future = asyncio.get_running_loop().create_future()
            future.set_result(42)
            return await _call_or_await(lambda: future)

        self.assertEqual(asyncio.run(run()), 42)

    def test_polling_shutdown_accepts_a_task_cancelled_before_start(self):
        async def run():
            task = asyncio.create_task(asyncio.sleep(60))
            await UpdatesExecutor._wait_tasks({task})

        asyncio.run(run())

    def test_allowed_updates_survive_start_after_add(self):
        class CapturingExecutor(UpdatesExecutor):
            async def _runner(self, bot, allowed_updates=None):
                self.seen = allowed_updates
                await asyncio.Future()

        async def run():
            executor = CapturingExecutor()
            bot = object()
            allowed_updates = [UpdateType.callback_query]
            executor._bots[bot] = None
            executor._allowed_updates[bot] = allowed_updates

            await executor.start()
            await asyncio.sleep(0)
            self.assertEqual(executor.seen, allowed_updates)
            await executor.stop()

        asyncio.run(run())


class ContextRegressionTests(unittest.TestCase):
    def test_new_update_kinds_populate_common_context(self):
        bot = object()
        chat = SimpleNamespace(id=1)
        user = SimpleNamespace(id=2)
        message = SimpleNamespace(chat=chat, user=user)

        context.assign(None, bot, SimpleNamespace(
            type=UpdateType.business_message,
            business_message=message,
        ))
        self.assertIs(context.message, message)
        self.assertIs(context.chat, chat)
        self.assertIs(context.user, user)

        answer = SimpleNamespace(voter_chat=chat, user=None)
        context.assign(None, bot, SimpleNamespace(type=UpdateType.poll_answer, poll_answer=answer))
        self.assertIs(context.answer, answer)
        self.assertIs(context.chat, chat)
        self.assertIsNone(context.user)


class ConnectorRegressionTests(unittest.TestCase):
    def test_aiohttp_session_is_lazy_reusable_and_reports_parse_errors(self):
        payloads = [
            b'{"ok": true, "result": true}',
            b'not-json',
            b'{"ok": true, "result": true}',
        ]
        sessions = []

        class FakeResponse:
            def __init__(self, payload):
                self.payload = payload

            async def read(self):
                return self.payload

        class FakeSession:
            def __init__(self):
                self.closed = False
                sessions.append(self)

            async def post(self, *args, **kwargs):
                return FakeResponse(payloads.pop(0))

            async def close(self):
                self.closed = True

        fake_aiohttp = types.ModuleType("aiohttp")
        fake_aiohttp.ClientSession = FakeSession
        fake_aiohttp.FormData = object

        module_name = "rocketgram.connectors.aiohttp"
        previous_aiohttp = sys.modules.get("aiohttp")
        previous_connector = sys.modules.pop(module_name, None)
        sys.modules["aiohttp"] = fake_aiohttp

        try:
            aiohttp_connector = importlib.import_module(module_name)

            async def run():
                connector = aiohttp_connector.AioHttpConnector()
                self.assertEqual(sessions, [])

                response = await connector.send("token", DeleteWebhook())
                self.assertTrue(response.ok)
                self.assertEqual(len(sessions), 1)

                with self.assertRaises(RocketgramParseError):
                    await connector.send("token", DeleteWebhook())

                await connector.shutdown()
                self.assertTrue(sessions[0].closed)

                response = await connector.send("token", DeleteWebhook())
                self.assertTrue(response.ok)
                self.assertEqual(len(sessions), 2)
                await connector.shutdown()

            asyncio.run(run())
        finally:
            sys.modules.pop(module_name, None)
            if previous_connector is not None:
                sys.modules[module_name] = previous_connector
            if previous_aiohttp is None:
                sys.modules.pop("aiohttp", None)
            else:
                sys.modules["aiohttp"] = previous_aiohttp


class ParserRegressionTests(unittest.TestCase):
    def test_html_escapes_entity_attributes(self):
        text = "link"
        entity = make_entity(EntityType.text_link, len(text), url='https://example.test/?a=1&b="2"')

        self.assertEqual(
            to_html(text, [entity]),
            '<a href="https://example.test/?a=1&amp;b=&quot;2&quot;">link</a>',
        )

    def test_markdown_code_and_link_render_valid_delimiters(self):
        code = make_entity(EntityType.code, 1)
        link = make_entity(EntityType.text_link, 4, url="https://example.test/a)b")

        self.assertEqual(to_markdown("x", [code]), "`x`")
        self.assertEqual(to_markdown_v2("link", [link]), "[link](https://example.test/a\\)b)")

    def test_expandable_blockquotes_are_preserved(self):
        text = "first\nsecond"
        entity = make_entity(EntityType.expandable_blockquote, len(text))

        self.assertEqual(to_html(text, [entity]), "<blockquote expandable>first\nsecond</blockquote>")
        self.assertEqual(to_markdown_v2(text, [entity]), "**>first\n>second||")


if __name__ == "__main__":
    unittest.main()
