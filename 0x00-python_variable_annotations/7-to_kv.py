#!/usr/bin/env python3
"""
function 'to_kv'
"""
from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """
    square of tuple
    Args:
        k: first param
        v: second param
    Return:
        tuple
    """
    return k, float(v ** 2)
