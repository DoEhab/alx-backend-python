#!/usr/bin/env python3
"""
This function return string rep of float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    input_list: first param
    """
    result: float = 0
    for i in input_list:
        result = result + i
    return result
