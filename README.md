# Rocketgram

![TEST](https://github.com/rocketgram/rocketgram/workflows/TEST/badge.svg)

Modern and powerful asynchronous telegram bot framework.

Release news available here: [@RocketgramNews](https://t.me/RocketgramNews)

## Dependencies

All dependencies are optional, but you should install `aiohttp` to use the framework.

`orjson` or `ujson` is highly recommended to speed up json parsing.

Also, you can use `uvloop` as alternative to standard event loop.

## How to install

#### For development

```bash
pip install rocketgram[aiohttp]
```

#### For production

```bash
pip install uvloop rocketgram[aiohttp,orjson]
```

## Example

There is a trivial example below.
[Here](https://github.com/vd2org/rocketgram-template) is useful bot template.

```python
from rocketgram import Bot, Dispatcher, UpdatesExecutor
from rocketgram import context, commonfilters
from rocketgram import SendMessage

try:
    import uvloop

    uvloop.install()
except ImportError:
    pass

token = f'YOUR_BOT_TOKEN'

router = Dispatcher()
bot = Bot(token, router=router)

@router.handler
@commonfilters.command('/start')
async def start_command():
    await SendMessage(context.user.id, f'Hello there!').send()
    
@router.handler
@commonfilters.command('/help')
async def start_command():
    await SendMessage(context.user.id, f'Some userful help!').send()
    
UpdatesExecutor.run(bot)
```

# Testing

Code tested automatically using `Github Actions`. 
You can see the build status **[here](https://github.com/rocketgram/rocketgram/actions)**.

To test code manually run `pytest`:

```bash
pytest
```