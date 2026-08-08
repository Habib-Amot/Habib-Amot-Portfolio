# in this lesson i learnt about how coroutines works in python and also how they are the building blocks of tasks that run on 
# the event loop

import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def coro_generator(delay, break_after_execution=False):
    print('I am a coroutine')
    try:
        while True:
            print('I am running')
            await asyncio.sleep(delay=delay)  # this will make the asynchronous action to be triggered but not executed due to zero sleep time
            if break_after_execution: break

    except asyncio.CancelledError as err:
        print("stopped gracefully")

if __name__ == "__main__":
    # and now the coroutine above can be put to test
    ''' to communicate with a coroutine, we need to make use of the send method of the coroutine'''
    coro = coro_generator(0)
    coro.send(None)
    coro.send(None)
    try:
        coro.throw(asyncio.CancelledError)  # this will raise a cancelled error and the coroutine will be cancelled
    except asyncio.CancelledError as err:
        pass
    except StopIteration as err:
        print("i have finished")

