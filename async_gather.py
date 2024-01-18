import asyncio


async def task1():
    print("Hello")
    await asyncio.sleep(3)
    return 'result from 1st task'


async def task2():
    print("world")
    await asyncio.sleep(2)
    return 'result from 2nd task'


async def task3():
    print("!")
    await asyncio.sleep(1)
    return 'result from 3rd task'


async def main():
    results = await asyncio.gather(task1(), task2(), task3())
    for result in results:
        print(result)

asyncio.run(main())
