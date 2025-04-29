#!/usr/bin/env python3

async_generator = __import__('0-async_generator').async_generator

"""
async_comprehension function
"""


async def async_comprehension():
    """
    coroutine function
    that returns a random number async
    """
    return [i async for i in async_generator()]
