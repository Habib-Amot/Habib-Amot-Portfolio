# a coroutine is a python function, that can be paused (suspended) and resumed at a particular point in time
# when a coroutine is paused or suspended, other functions or coroutines are executed and once the coroutine is done
# waiting, it is resumed and operation is returned to the point where it paused it execution
# a coroutine can pass it value to another function which must also be a coroutine also
import random
import asyncio
import time


# say we want to perform a series of operation on a set of data, this can be achieved by passing each data into a
# function, but the caveat with this type of approach is that, each function must wait for the current processing
# function to finish before they can process the remaining data. One way to solve this is to use Coroutines

def numbers_gen():
    numbers = list(range(1, 21))
    count = 0
    while count < len(numbers):
        value = yield
        print(numbers[value])


def index_gen():
    index = random.randint(0, 21)
    yield index


# generator_obj = numbers_gen()
# print(next(generator_obj))
# generator_obj.send(3)

# with this knowledge, we can build an asynchronous like method


@asyncio.coroutine
def get_symbol_info(sym):
    time.sleep(2)
    yield f"{sym} is a good Ticker"


@asyncio.coroutine
def get_symbols():
    symbols = ["GGL", "TSL", "MSFT"]
    for sym in symbols:
        yield from get_symbol_info(sym)


# mimicking the event loop
coro = get_symbols()
while True:
    try:
        symbol = next(coro)
        print(symbol)
    except StopIteration:
        print('breaking')
        break
