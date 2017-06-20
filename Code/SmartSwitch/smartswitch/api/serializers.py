from smartswitch.api.models import UserDevice, Device
from django.contrib.auth.models import User
from rest_framework import serializers

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', ]


class UserDeviceSerializer(serializers.ModelSerializer):
    device = DeviceSerializer()
    class Meta:
        model = UserDevice
        fields = '__all__'