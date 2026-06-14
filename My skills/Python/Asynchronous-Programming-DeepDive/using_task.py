import asyncio
from using_coroutines import coro_generator

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


# and now we can create a task from the coroutine
# while coroutines are just functions that can be paused and resumed, tasks are coroutines that are scheduled to run on the event loop
#  this means that to make use of tasks, we need an event loop to be running

async def main():
    # this line just shedules our coro generator on the event loop and then never awaits it, instead it just move on
    loop.create_task(coro_generator(delay=4, break_after_execution=True))

if __name__ == "__main__":
    loop.run_until_complete(main())

    # closing a loop like this without a proper cleanup will result in some tasks that are still on the event loop to get cancelled
    # without gracefully exiting thus going to result in an message being printed on the screen about the task
    # loop.close()

    # a more graceful way to clean up is to get all of the pending tasks that are on the event loop and end them
    pending_tasks = asyncio.all_tasks(loop=loop)
    for task in pending_tasks: task.cancel()

    # making sure all tasks finish running
    pending_group = asyncio.gather(*pending_tasks, return_exceptions=True)
    loop.run_until_complete(pending_group)
