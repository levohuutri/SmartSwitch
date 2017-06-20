# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from smartswitch.api import serializers
from smartswitch.api import models
import datetime

# Create your views here.
def get_devices(request):
    start = datetime.datetime.now()
    slug = request.GET.get('slug', None)
    data = {}
    if slug:
        user_device = models.UserDevice.objects.filter(user_id=slug).first()
        if user_device:
            data["user"] = serializers.UserSerializer(user_device.user).data

            user_devices = models.UserDevice.objects.filter(user_id=slug).all()
            devices = [o.device for o in user_devices]

            data["devices"] = serializers.DeviceSerializer(devices, many=True).data
    data["cpu_time_mil"] = (datetime.datetime.now() - start).microseconds / 1000
    return JsonResponse(data, safe=False)