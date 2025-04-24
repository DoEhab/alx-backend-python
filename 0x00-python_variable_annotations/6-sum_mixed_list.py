#!/usr/bin/env python3
"""
function 'sum_mixed_list'
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums ints and float numbers
    Args:
        mxd_lst (list): first param
    Return:
        (float)
    """
    return sum(mxd_lst)
