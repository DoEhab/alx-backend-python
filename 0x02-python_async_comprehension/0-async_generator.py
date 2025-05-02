#!/usr/bin/env python3
"""
async_generator module
"""

import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:

    """
    Asynchronous generator that yields 10
    random float numbers between 0 and 10.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        yield random.uniform(0, 10)
