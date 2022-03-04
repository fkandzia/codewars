"""Write a function that when given a URL as a string, parses out just the
domain name and returns it as a string.
"""
import re
from typing import Optional


def domain_name(url: str) -> Optional[str]:
    """Parse the domain name from a given URL.

    Parameters
    ----------
    url: str
        A string containing a valid url

    Returns
    -------
    domain_name: str or None
        If a valid URL was given, then return the
        domain name as a string otherwise return None.
    """
    full_url = '(?:.+)://(?:www\.)?(?P<domain_name>.*?)\..*'
    implicit_url = '(?:www\.)?(?P<domain_name>.*?)\..*'
    short_url = '(?P<domain_name>.*?)\..*'

    if '://' in url:
        pattern = full_url
    elif url.startswith('www.'):
        pattern = implicit_url
    else:
        pattern = short_url

    matcher = re.match(pattern, url)
    if matcher:
        return matcher['domain_name']

def domain_name_2(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]