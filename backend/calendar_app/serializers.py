from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    '''Serializer for the calendar events'''

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'starting_time', 'ending_time')
