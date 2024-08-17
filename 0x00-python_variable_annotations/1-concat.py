#!/usr/bin/env python3
"""This module contains a function
to concatenate two strings
"""


def concat(str1: str, str2: str) -> str:
    """This function concatenates
    two strings

    Args:
        str1 (str): first arg
        str2 (str): second arg

    Returns:
        str: result string
    """
    result = "{} {}".format(str1, str2)
    return result
