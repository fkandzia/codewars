from typing import List

import numpy as np


def range_extraction(numbers: List[int]) -> str:
    """Convert a list of increasing numbers into a string in the range format.

    Parameters
    ----------
    numbers: List[int]
        A list of integers in increasing order

    Returns
    -------
    range_format_string: str
        A correctly formatted string in the range format
    """
    range_format_string = ''
    if numbers:
        ranges = []
        start_number = stop_number = numbers[0]

        for number in numbers[1:] + [np.inf]:
            if number != stop_number + 1:
                if stop_number == start_number:
                    ranges.append(f'{stop_number}')
                elif stop_number == start_number + 1:
                    ranges.append(f'{start_number},{stop_number}')
                else:
                    ranges.append(f'{start_number}-{stop_number}')
                start_number = number
            stop_number = number

        range_format_string = ",".join(ranges)
    return range_format_string


def range_extraction_2(numbers: List[int]) -> str:
    """Convert a list of increasing numbers into a string in the range format.

    A format for expressing an ordered list of integers is to use a comma
    separated list of either:
        - individual integers
        - or a range of integers denoted by the starting integer separated from
          the end integer in the range by a dash, '-'.
    The range includes all integers in the interval including both endpoints. It's
    not considered a range unless it spans at least 3 numbers, e.g. "12,13,15-17"

    Parameters
    ----------
    numbers: List[int]
        A list of integers in increasing order

    Returns
    -------
    range_format_string: str
        A correctly formatted string in the range format
    """
    if numbers:
        sorted_numbers = sorted(numbers)
        groups = get_groups(sorted_numbers)
        ranges = create_range_format_strings(groups)
        return ','.join(ranges)


def get_groups(numbers: List[int]) -> List[List[int]]:
    """Take a list of increasing ints and return groups of consecutive numbers.

    Parameters
    ----------
    numbers: List[int]
        A list of integers in increasing order

    Returns
    -------
    groups: List[List[int]]
        A list of groups consisting of consecutive numbers
    """
    groups = []
    tmp = [numbers[0]]
    if len(numbers) > 1:
        for idx, value in enumerate(numbers[1:], start=1):
            if value == numbers[idx - 1] + 1:
                tmp.append(value)
            else:
                groups.append(tmp)
                tmp = [value]
    groups.append(tmp)
    return groups


def create_range_format_strings(groups: List[List[int]]) -> List[str]:
    """Convert a list of groups of consecutive numbers into range format strings

    Parameters
    ----------
    groups: List[List[int]]
        A list of groups consisting of consecutive numbers

    Returns
    -------
    range_format_strings: List[str]
        A list of strings formatted according to the range format
    """
    range_format_strings = []
    for group in groups:
        group_length = len(group)
        if group_length < 3:
            range_format_strings.append(','.join(map(str, group)))
        if group_length >= 3:
            range_format_strings.append('-'.join(map(str, group[::group_length - 1])))
    return range_format_strings
