from django.shortcuts import render

# Create your views here.
from models import Event, Guest
from rest_framework import viewsets
from serializers import EventSerializer, GuestSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


