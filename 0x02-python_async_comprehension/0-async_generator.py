#!/usr/bin/env python3
"""
async_generator module
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields 10
    random float numbers between 0 and 10.

    Yields:
        float: A random float between 0 and 10.
    """
    for i in range(10):
        i: int
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
