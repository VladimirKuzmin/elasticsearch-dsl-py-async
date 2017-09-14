import asyncio


def execute_queries(*queries):
    future = asyncio.gather(*(q.execute_async() for q in queries))
    loop = future._loop
    return loop.run_until_complete(future)
