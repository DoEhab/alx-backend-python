#!/usr/bin/env python3
"""
function 'safe_first_element'
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
            loops on the list to get the length
            Args:
                lst: first param

            Return:
                item len
            """
    if lst:
        return lst[0]
    else:
        return None
