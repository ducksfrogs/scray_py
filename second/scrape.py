import csv
from typing import List

import requests
import lxml.html


def main():
    """
    Main
    """

    url = 'https://gihyo.jp/dp'
    html = fetch(url)
    books = scrape


def fetch(url: str) -> str:
    """
    ddd
    """
    r = requests.get(url)
    return r.text


def scrape(html: str, base_url, str) -> List[dict]:
    books = []
    html = lxml.html.fromstring(html)
    
