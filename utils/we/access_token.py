# -*- coding: utf-8 -*-

import requests


def fetch_access_token(token_url, token_key=None):
    if token_url:
        return

    try:
        token = requests.get(token_url).json().get(token_key or 'access_token', '')  # Safety
    except Exception:
        token = ''

    return token
