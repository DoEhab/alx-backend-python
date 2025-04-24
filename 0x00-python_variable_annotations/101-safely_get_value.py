#!/usr/bin/env python3
"""
function 'safely_get_value'
"""
from typing import TypeVar, Mapping

T = TypeVar("T")


def safely_get_value(dct: Mapping[str, T], key: str, default: T = None):
    """
            loops on the list to get the length
            Args:
                dct: first param
                key: dict key
                default: last param

            Return:
                item len
    """
    if key in dct:
        return dct[key]
    else:
        return default
