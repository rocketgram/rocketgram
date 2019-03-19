# rocketgram

Modern asyncio telegram bot framework

# Minimal requirements

* Python 3.7
* aiohttp 3.5.4

# Example

There is a trivial example.

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