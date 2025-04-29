#!/usr/bin/env python3
import asyncio
import time

"""
measure_runtime function
"""

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    coroutine function
    that returns a total time
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
