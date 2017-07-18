# -*- coding: utf-8 -*-

"""
    pyguest.serializers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Author: Y.Z.Y
    
"""

from models import Event, Guest
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'name', 'address', 'start_time', 'limit', 'status')


class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest
        fields = ('url', 'realname', 'phone', 'email', 'sign', 'event')
