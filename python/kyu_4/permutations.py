"""In this kata you have to create all permutations of an input string and
remove duplicates, if present. This means, you have to shuffle all letters
from the input in all possible orders."""
import itertools
from typing import List


def permutations(raw: str) -> List[str]:
    """Return a list of all unique permutations of a given input string.

    In case of an empty string (`''`) a list with an empty string will be returned (`['']`).

    Parameters
    ----------
    raw: str
        Input string from which the permutations are being generated

    Returns
    -------
    permutations: List[str]
        A list of permutation strings based on the input string
    """
    return [*set(''.join(tup) for tup in itertools.permutations(raw))]
