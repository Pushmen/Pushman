# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import urllib

import requests
from django.conf import settings
from pywe_sign import fill_signature

from wepush.models import WeChatTemplateInfo


def send_tplmsg(push_id, openid=None):
    tpl = WeChatTemplateInfo.objects.get(wepush_id=push_id)

    data = {
        'push_id': push_id,
        'first': u'提现故障',
        'keyword1': '127.0.0.1',
        'keyword2': u'微信提现',
        'keyword3': u'余额发放失败',
        'keyword4': u'余额不足，错误码: NOTENOUGH',
        'keyword5': '',
        'remark': u'请尽快充值！',
        'color': '#173177',
        'openids': json.dumps([openid] if openid else []),
    }

    data = fill_signature(data, tpl.wepush_secret)

    requrl = '{0}/api/send/tplmsg?text={1}'.format(settings.DOMAIN, urllib.quote_plus(json.dumps(data)))
    print requrl

    print requests.get(requrl).json()
