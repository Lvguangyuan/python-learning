import asyncio
import threading


# @asyncio.coroutine
async def hello():
    print('Hello Start! (%s)' % threading.current_thread())
    r = await asyncio.sleep(1)
    # r = yield from asyncio.sleep(1)
    print('Hello End! (%s)' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
