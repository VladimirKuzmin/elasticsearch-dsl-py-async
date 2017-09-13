import asyncio


def execute_queries(*queries, loop=None):
    loop = loop or asyncio.get_event_loop()
    return loop.run_until_complete(asyncio.gather(*(q.execute_async() for q in queries)))
