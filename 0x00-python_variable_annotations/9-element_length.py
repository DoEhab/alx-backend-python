#!/usr/bin/env python3
"""
function 'element_length'
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        loops on the list to get the length
        Args:
            lst: first param

        Return:
            item len
        """
    return [(i, len(i)) for i in lst]
