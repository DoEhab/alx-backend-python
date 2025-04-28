#!/usr/bin/env python3
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

"""
function measure_time
"""


async def measure_time(n: int, max_delay: int) -> float:
    """
    :param n: number of tasks
    :param max_delay: max delay value
    :return: execution time
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
