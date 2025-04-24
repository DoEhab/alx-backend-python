#!/usr/bin/env python3
"""
function 'to_kv'
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    square of tuple
    Args:
        k: first param
        v: second param
    Return:
        tuple
    """
    return k, float(v ** 2)
