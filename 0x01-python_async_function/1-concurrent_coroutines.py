#!/usr/bin/env python3
from basic_async_syntax import wait_random
import asyncio

"""
function wait_n
"""


async def wait_n(n, max_delay):
    """
    :param n: number of tasks
    :param max_delay: max delay value
    :return: array of delays
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
