#!/usr/bin/env python3
import asyncio
import random

"""
wait_random function
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    coroutine function
    :param max_delay: max delay time
    :return: return the delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
