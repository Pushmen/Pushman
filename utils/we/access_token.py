# -*- coding: utf-8 -*-

import requests


def fetch_access_token(token_url):
    if token_url:
        return

    try:
        token = requests.get(token_url).text()  # Safety
    except Exception:
        token = ''

    return token
