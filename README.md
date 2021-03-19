# Rocketgram

![TEST](https://github.com/rocketgram/rocketgram/workflows/TEST/badge.svg)

Modern and powerful asynchronous telegram bot framework.

Release news available here: [@RocketgramNews](https://t.me/RocketgramNews)

## How to install

#### For development

```bash
pip install rocketgram[aiohttp]
```

#### For production

```bash
pip install rocketgram[aiohttp,ujson]
```

## Dependencies

All dependencies are optional but you should install one of `aiohttp` and `tornado` to use framework.

`ujson` is highly recommended to speedup json parsing.

Also you can use `uvloop` as alternative to standard event loop.

* Python >= 3.7
* aiohttp >= 3.6.2
* ujson >= 1.35
* tornado >= 6.0.2
* uvloop >= 0.12.1

## Example

There is a trivial example below.
[Here](https://github.com/vd2org/rocketgram-template) is useful bot template.

```python
from rocketgram import Bot, Dispatcher, UpdatesExecutor
from rocketgram import context, commonfilters
from rocketgram import SendMessage

token = 'YOUR_BOT_TOKEN'

router = Dispatcher()
bot = Bot(token, router=router)

@router.handler
@commonfilters.command('/start')
async def start_command():
    await SendMessage(context.user.user_id, 'Hello there!').send()
    
@router.handler
@commonfilters.command('/help')
async def start_command():
    await SendMessage(context.user.user_id, 'Some userful help!').send()
    
UpdatesExecutor.run(bot)
```

# Testing

Code tested automatically using `Github Actions`. 
You can see build status **[here](https://github.com/rocketgram/rocketgram/actions)**.

To test code manually install and run `pytest`:

```bash
pip install pytest
python -m pytest
```