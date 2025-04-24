#!/usr/bin/env python3
"""
function 'element_length'
"""
from typing import Union, List, Tuple, Sequence


def element_length(lst: Union[str, List[str]]) -> List[Tuple[str, int]]:
    """
        loops on the list to get the length
        Args:
            lst: first param

        Return:
            item len
        """
    return [(i, len(i)) for i in lst]
