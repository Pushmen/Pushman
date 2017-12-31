# -*- coding: utf-8 -*-

from djadmin import AdvancedExportExcelModelAdmin, ReadonlyModelAdmin, ReadOnlyModelAdmin
from django.contrib import admin
from pysnippets.strsnippets import strip

from wepush.models import (WeChatTemplateInfo, WeChatTemplateMessageRequestLogInfo, WeChatTemplateMessageSendLogInfo,
                           WeChatTemplateReceiverInfo)


class WeChatTemplateInfoAdmin(ReadonlyModelAdmin, admin.ModelAdmin):
    list_display = ('wepush_id', 'wepush_secret', 'wepush_remark', 'app_id', 'app_secret', 'template_id', 'token_url', 'token_key', 'status', 'created_at', 'updated_at')
    list_filter = ('template_id', 'status')
    search_fields = ('wepush_id', 'wepush_secret', 'wepush_remark', 'app_id', 'app_secret', 'template_id', 'token_url', 'token_key')
    readonly_fields_exclude = ('wepush_remark', 'app_id', 'app_secret', 'template_id', 'token_url', 'token_key', 'status')

    def save_model(self, request, obj, form, change):
        obj.app_id = strip(obj.app_id)
        obj.app_secret = strip(obj.app_secret)
        obj.template_id = strip(obj.template_id)
        obj.token_url = strip(obj.token_url)
        obj.save()


class WeChatTemplateReceiverInfoAdmin(admin.ModelAdmin):
    list_display = ('receiver_id', 'receiver_remark', 'wepush_id', 'openid', 'status', 'created_at', 'updated_at')
    list_filter = ('wepush_id', 'status')
    search_fields = ('receiver_id', 'receiver_remark', 'wepush_id', 'openid')

    def save_model(self, request, obj, form, change):
        obj.wepush_id = strip(obj.wepush_id)
        obj.openid = strip(obj.openid)
        obj.save()


class WeChatTemplateMessageRequestLogInfoAdmin(AdvancedExportExcelModelAdmin, ReadOnlyModelAdmin, admin.ModelAdmin):
    list_display = ('request_id', 'wepush_id', 'request_ip', 'request_text', 'request_sign_status', 'status', 'created_at', 'updated_at')
    list_filter = ('wepush_id', 'request_sign_status', 'status')
    search_fields = ('request_id', 'wepush_id', 'request_ip', 'request_text')


class WeChatTemplateMessageSendLogInfoAdmin(AdvancedExportExcelModelAdmin, ReadOnlyModelAdmin, admin.ModelAdmin):
    list_display = ('send_id', 'wepush_id', 'openid', 'send_msgres', 'send_status', 'status', 'created_at', 'updated_at')
    list_filter = ('wepush_id', 'send_status', 'status')
    search_fields = ('send_id', 'wepush_id', 'openid', 'send_msgres')


admin.site.register(WeChatTemplateInfo, WeChatTemplateInfoAdmin)
admin.site.register(WeChatTemplateReceiverInfo, WeChatTemplateReceiverInfoAdmin)
admin.site.register(WeChatTemplateMessageRequestLogInfo, WeChatTemplateMessageRequestLogInfoAdmin)
admin.site.register(WeChatTemplateMessageSendLogInfo, WeChatTemplateMessageSendLogInfoAdmin)
