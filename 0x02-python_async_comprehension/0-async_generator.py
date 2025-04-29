#!/usr/bin/env python3
import asyncio
import random

"""
async_generator function
"""


async def async_generator() -> int:
    """
    coroutine function
    that returns a random number async
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
