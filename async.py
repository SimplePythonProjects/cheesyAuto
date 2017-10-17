import asyncio

@asyncio.coroutine
def periodic():
    while True:
        print(l)
        print('periodic')
        yield from asyncio.sleep(1)

def stop():
    task.cancel()
l = 5
task = asyncio.Task(periodic())
loop = asyncio.get_event_loop()
loop.call_later(5, stop)

try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass
