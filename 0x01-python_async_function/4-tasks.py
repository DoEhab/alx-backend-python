#!/usr/bin/env python3
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random

"""
function task_wait_n
"""


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    :param n: number of tasks
    :param max_delay: max delay value
    :return: array of delays
    """
    tasks = [asyncio.create_task(task_wait_random(max_delay))
             for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
