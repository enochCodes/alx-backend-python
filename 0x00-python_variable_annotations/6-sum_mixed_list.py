#!/usr/bin/env python3
'''
6-sum_mixed_list.py
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list

    Calculates the sum of a list
    containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]):
        A list of integers and floats.

    Returns:
        float: The sum of all elements in
        the list as a float.
    """
    return sum(mxd_lst)
