# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from smartswitch.api.models import Device, UserDevice

# Register your models here.
admin.site.register(Device, admin.ModelAdmin)
admin.site.register(UserDevice, admin.ModelAdmin)