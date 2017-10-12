# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from ipaddr import client_ip
from pywe_sign import check_signature
from pywe_storage import RedisStorage
from pywe_template_message import TemplateMessage
from TimeConvert import TimeConvert as tc

from utils.error.errno_utils import SignatureStatusCode, WeChatTemplateStatusCode
from utils.error.response_utils import response
from utils.redis.connect import r
from wepush.models import (WeChatTemplateInfo, WeChatTemplateMessageRequestLogInfo, WeChatTemplateMessageSendLogInfo,
                           WeChatTemplateReceiverInfo)


def send_tplmsg(request):
    """ key + title/ip/type/descr/detail/remark + sign """
    text = request.POST.get('text', '') or request.GET.get('text', '')

    if not text:
        return response()

    data = json.loads(text)

    wepush_id = data.get('key', '')

    reqlog = WeChatTemplateMessageRequestLogInfo.objects.create(
        wepush_id=wepush_id,
        request_ip=client_ip(request),
        request_text=text,
    )

    try:
        tpl = WeChatTemplateInfo.objects.get(wepush_id=wepush_id, status=True)
    except WeChatTemplateInfo.DoesNotExist:
        return response(WeChatTemplateStatusCode.TEMPLATE_NOT_FOUND)

    if not check_signature(data, api_key=tpl.wepush_secret):
        reqlog.request_sign_status = False
        reqlog.save()
        return response(SignatureStatusCode.SIGNATURE_ERROR)

    receivers = WeChatTemplateReceiverInfo.objects.filter(wepush_id=tpl.wepush_id)
    if not receivers.exists():
        return response(WeChatTemplateStatusCode.RECEIVER_NOT_FOUND)

    tpl_data = {
        'first': {
            'value': data.get('title', u'服务器故障'),
            'color': data.get('color', u'#173177'),
        },
        'ip': {
            'value': data.get('ip', '127.0.0.1'),
            'color': data.get('color', u'#173177'),
        },
        'type': {
            'value': data.get('type', u'服务器故障'),
            'color': data.get('color', u'#173177'),
        },
        'descr': {
            'value': data.get('descr', u'服务器故障'),
            'color': data.get('color', u'#173177'),
        },
        'detail': {
            'value': data.get('detail', u'服务器故障'),
            'color': data.get('color', u'#173177'),
        },
        'time': {
            'value': data.get('time', tc.local_string()),
            'color': data.get('color', u'#173177'),
        },
        'remark': {
            'value': data.get('remark', u'请尽快处理！'),
            'color': data.get('color', u'#173177'),
        },
    }
    tplmsg = TemplateMessage(appid=tpl.app_id, secret=tpl.app_secret, storage=RedisStorage(r))
    for receiver in receivers:
        msgres = tplmsg.send_template_message(user_id=receiver.openid, template_id=tpl.template_id, data=tpl_data, url=data.get('url', None))
        WeChatTemplateMessageSendLogInfo.objects.create(
            wepush_id=wepush_id,
            openid=receiver.openid,
            send_status=msgres['errcode'] == 0,
        )

    return response()
