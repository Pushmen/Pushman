# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

import requests
from django.conf import settings
from pywe_sign import fill_signature

from wepush.models import WeChatTemplateInfo


def send_tplmsg(key):
    tpl = WeChatTemplateInfo.objects.get(wepush_id=key)

    data = {
        'key': key,
        'title': u'提现故障',
        'ip': '127.0.0.1',
        'type': u'微信提现',
        'descr': u'余额发放失败',
        'detail': u'余额不足，错误码: NOTENOUGH',
        'remark': u'请尽快充值！'
    }

    data = fill_signature(data, tpl.wepush_secret)

    requrl = '{}/api/send/tplmsg?text={}'.format(settings.DOMAIN, json.dumps(data))
    print requrl

    requests.get(requrl)
