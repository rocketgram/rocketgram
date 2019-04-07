# rocketgram

Modern and powerful asynchronous telegram bot framework.

## Dependencies

### Required

* Python >= 3.7
* aiohttp 3.5.4

### Optional 

* ujson >= 1.35
* uvloop >= 0.12.1

## Example

There is a trivial example below.
[Here](https://github.com/vd2org/rocketgram-template) is useful bot template.

```python
from rocketgram import Bot, Context, Dispatcher, commonfilters, run_updates

token = 'YOUR_BOT_TOKEN'

router = Dispatcher()
bot = Bot(token, router=router)

@router.handler
@commonfilters.command('/start')
async def start_command(ctx: Context):
    await ctx.send_message('Hello there!')
    
@router.handler
@commonfilters.command('/help')
async def start_command(ctx: Context):
    await ctx.send_message('Some userful help!')
    
run_updates(bot)
```