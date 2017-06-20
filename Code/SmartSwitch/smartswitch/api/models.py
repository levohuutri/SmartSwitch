# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Device(models.Model):
    id = models.AutoField(primary_key=True)
    address_mac = models.CharField(max_length=100)
    address_ipv4 = models.CharField(max_length=100)

    def __unicode__(self):
        return self.address_mac


class UserDevice(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    device = models.ForeignKey(Device)

    def __unicode__(self):
        return "{0} - {1}".format(self.user.username, self.device.address_mac)