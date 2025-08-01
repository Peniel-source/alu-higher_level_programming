#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

import requests
from requests import Session

if __name__ == "__main__":
    session = Session()
    requ = session.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(requ.text))
    print("\t- content:", requ.text)
