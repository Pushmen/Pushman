# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class CreateUpdateMixin(models.Model):
    status = models.BooleanField(_(u'status'), default=True, help_text=_(u'状态'), db_index=True)
    created_at = models.DateTimeField(_(u'created_at'), auto_now_add=True, editable=True, help_text=_(u'创建时间'))
    updated_at = models.DateTimeField(_(u'updated_at'), auto_now=True, editable=True, help_text=_(u'更新时间'))

    class Meta:
        abstract = True
