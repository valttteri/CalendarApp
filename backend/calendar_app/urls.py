from django.urls import path
from .views import *

urlpatterns = [
    path("events/create/", CreateNewEventView.as_view())
]