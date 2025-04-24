#!/usr/bin/env python3
"""
function 'make_multiplier'
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    multiple param
    Args:
        multiplier: first param

    Return:
        function
    """
    def multiply_by(value: float) -> float:
        return value * multiplier
    return multiply_by
