"""Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.
"""
import re
from typing import List


def solution(raw: str, markers: List[str]) -> str:
    """Remove all comments from raw string as indicated by markers."""
    return '\n'.join(
        [re.split(r'|'.join(map(re.escape, markers)), line)[0].strip() for line in raw.split('\n')]) if markers else raw


def solution_detailed(raw: str, markers: List[str]) -> str:
    """Remove all comments from raw string as indicated by markers."""
    if markers:
        cleaned_lines = []
        escaped_markers = r'|'.join(map(re.escape, markers))
        for line in raw.split('\n'):
            cleaned_lines.append(re.split(escaped_markers, line)[0].strip())
        cleaned = '\n'.join(cleaned_lines)
        return cleaned
    return raw