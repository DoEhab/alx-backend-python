#!/usr/bin/env python3
import asyncio

wait_random = __import__('0_basic_async_syntax').wait_random

"""
function task_wait_random
"""


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    :param max_delay: max delay value
    :return: async task
    """

    return asyncio.create_task(wait_random(max_delay))
