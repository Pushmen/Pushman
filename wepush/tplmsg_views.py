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
from utils.we.access_token import fetch_access_token
from wepush.models import (WeChatTemplateInfo, WeChatTemplateMessageRequestLogInfo, WeChatTemplateMessageSendLogInfo,
                           WeChatTemplateReceiverInfo)


def send_tplmsg(request):
    """ push_id + title/ip/type/descr/detail/time/remark/color + sign """
    text = request.POST.get('text', '') or request.GET.get('text', '')

    if not text:
        return response()

    data = json.loads(text)

    # Key for back compatibility
    wepush_id = data.get('push_id', '') or data.get('key', '')

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

    color = data.get('color', u'#173177')
    tpl_data = {
        'first': {
            'value': data.get('title', u'服务器故障'),
            'color': color,
        },
        'ip': {
            'value': data.get('ip', '127.0.0.1'),
            'color': color,
        },
        'type': {
            'value': data.get('type', u'服务器故障'),
            'color': color,
        },
        'descr': {
            'value': data.get('descr', u'服务器故障'),
            'color': color,
        },
        'detail': {
            'value': data.get('detail', u'服务器故障'),
            'color': color,
        },
        'time': {
            'value': data.get('time', tc.local_string()) or tc.local_string(),
            'color': color,
        },
        'remark': {
            'value': data.get('remark', u'请尽快处理！'),
            'color': color,
        },
    }

    tplmsg = TemplateMessage(appid=tpl.app_id, secret=tpl.app_secret, token=fetch_access_token(tpl.token_url, tpl.token_key), storage=RedisStorage(r))

    success = failure = 0
    for receiver in receivers:
        msgres = tplmsg.send_template_message(user_id=receiver.openid, template_id=tpl.template_id, data=tpl_data, url=data.get('url', None))
        # Success Or Not
        send_status = msgres['errcode'] == 0
        # TPL Send Log
        WeChatTemplateMessageSendLogInfo.objects.create(
            wepush_id=wepush_id,
            openid=receiver.openid,
            send_msgres=msgres,
            send_status=send_status,
        )
        # Success/Failure Num Incr
        if send_status:
            success += 1
        else:
            failure += 1

    return response(200, data={
        'success': success,
        'failure': failure,
    })
