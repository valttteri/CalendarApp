from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.core.exceptions import ObjectDoesNotExist
from .serializers import EventSerializer
from .models import Event

class EventView(viewsets.ModelViewSet):

    serializer_class = EventSerializer
    queryset = Event.objects.all()