from django.db import models

class Events(models.Model):
    MeetingId = models.CharField(max_length=100)
    MeetingName = models.CharField(max_length=100)
    CreateTime = models.DateTimeField(null=True)
    UserId = models.CharField(max_length=100)
    userName = models.CharField(max_length=100)
    startTime = models.DateTimeField(null=True)
    endTime = models.DateTimeField(null=True)