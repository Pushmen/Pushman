# -*- coding: utf-8 -*-

from django.conf.urls import url

from wepush import tplmsg_views


urlpatterns = [
    url(r'^send/tplmsg$', tplmsg_views.send_tplmsg, name='send_tplmsg'),
]
