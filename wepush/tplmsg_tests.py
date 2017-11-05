# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import urllib

import requests
from django.conf import settings
from pywe_sign import fill_signature

from wepush.models import WeChatTemplateInfo


def send_tplmsg(push_id):
    tpl = WeChatTemplateInfo.objects.get(wepush_id=push_id)

    data = {
        'push_id': push_id,
        'title': u'提现故障',
        'ip': '127.0.0.1',
        'type': u'微信提现',
        'descr': u'余额发放失败',
        'detail': u'余额不足，错误码: NOTENOUGH',
        'time': '',
        'remark': u'请尽快充值！',
        'color': '#173177',
    }

    data = fill_signature(data, tpl.wepush_secret)

    requrl = '{}/api/send/tplmsg?text={}'.format(settings.DOMAIN, urllib.quote_plus(json.dumps(data)))
    print requrl

    print requests.get(requrl).json()
