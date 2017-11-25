# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from shortuuidfield import ShortUUIDField

from pushman.basemodels import CreateUpdateMixin


class WeChatTemplateInfo(CreateUpdateMixin):
    wepush_id = ShortUUIDField(_(u'wepush_id'), max_length=32, help_text=u'模板唯一标识', db_index=True, unique=True)
    wepush_secret = ShortUUIDField(_(u'wepush_secret'), max_length=32, help_text=u'模板消息密钥', db_index=True)
    wepush_remark = models.CharField(_(u'wepush_remark'), max_length=32, blank=True, null=True, help_text=u'模板消息备注')
    app_id = models.CharField(_(u'app_id'), max_length=255, help_text=u'开发者ID', db_index=True)
    app_secret = models.CharField(_(u'app_secret'), max_length=255, help_text=u'开发者密钥', db_index=True)
    template_id = models.CharField(_(u'template_id'), max_length=255, help_text=u'模板ID', db_index=True)
    token_url = models.URLField(_(u'token_url'), blank=True, null=True, help_text=u'获取access_token链接')
    token_key = models.CharField(_(u'token_key'), max_length=255, blank=True, null=True, help_text=u'access_token key')

    class Meta:
        verbose_name = _(u'wechattemplateinfo')
        verbose_name_plural = _(u'wechattemplateinfo')

    def __unicode__(self):
        return unicode(self.wepush_id)


class WeChatTemplateReceiverInfo(CreateUpdateMixin):
    receiver_id = ShortUUIDField(_(u'receiver_id'), max_length=32, help_text=u'接收人唯一标识', db_index=True, unique=True)
    receiver_remark = models.CharField(_(u'receiver_remark'), max_length=32, blank=True, null=True, help_text=u'接收人备注')
    wepush_id = models.CharField(_(u'wepush_id'), max_length=32, help_text=u'模板唯一标识', db_index=True)
    openid = models.CharField(_(u'openid'), max_length=255, blank=True, null=True, help_text=u'接受者Openid', db_index=True)

    class Meta:
        verbose_name = _(u'wechattemplatereceiverinfo')
        verbose_name_plural = _(u'wechattemplatereceiverinfo')

    def __unicode__(self):
        return unicode(self.pk)


class WeChatTemplateMessageRequestLogInfo(CreateUpdateMixin):
    request_id = ShortUUIDField(_(u'request_id'), max_length=32, help_text=u'请求唯一标识', db_index=True, unique=True)
    wepush_id = models.CharField(_(u'wepush_id'), max_length=32, help_text=u'模板唯一标识', db_index=True)
    request_ip = models.GenericIPAddressField(_(u'request_ip'), blank=True, null=True, help_text=u'请求IP')
    request_text = models.TextField(_(u'request_text'), blank=True, null=True, help_text=u'请求文本')
    request_sign_status = models.BooleanField(_(u'request_sign_status'), default=True, help_text=u'请求签名状态')

    class Meta:
        verbose_name = _(u'wechattemplatemessagerequestloginfo')
        verbose_name_plural = _(u'wechattemplatemessagerequestloginfo')

    def __unicode__(self):
        return unicode(self.pk)


class WeChatTemplateMessageSendLogInfo(CreateUpdateMixin):
    send_id = ShortUUIDField(_(u'send_id'), max_length=32, help_text=u'发送唯一标识', db_index=True, unique=True)
    wepush_id = models.CharField(_(u'wepush_id'), max_length=32, help_text=u'模板唯一标识', db_index=True)
    openid = models.CharField(_(u'openid'), max_length=255, blank=True, null=True, help_text=u'接受者Openid', db_index=True)
    send_msgres = models.TextField(_(u'send_msgres'), blank=True, null=True, help_text=u'发送回执')
    send_status = models.BooleanField(_(u'send_status'), default=True, help_text=u'发送状态')

    class Meta:
        verbose_name = _(u'wechattemplatemessagesendloginfo')
        verbose_name_plural = _(u'wechattemplatemessagesendloginfo')

    def __unicode__(self):
        return unicode(self.pk)
