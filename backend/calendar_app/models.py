from django.db import models
from datetime import datetime

class Event(models.Model):

    default_timestamp = datetime.strptime("01.01.1970 12:00:00", "%d.%m.%Y %H:%M:%S")

    title = models.CharField(max_length=100, default="") # Name of the event
    description = models.CharField(max_length=500, default="")  # Description of the event

    starting_time = models.DateTimeField(
        auto_now = False,
        auto_now_add = False,
        blank = True,
        default = f"{default_timestamp}"
    )
    ending_time = models.DateTimeField(
        auto_now = False,
        auto_now_add = False,
        blank = True,
        default = f"{default_timestamp}"
    )
