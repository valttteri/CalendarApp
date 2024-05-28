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

class CreateNewEventView(APIView):
    '''Create a new event'''

    #permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = EventSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)