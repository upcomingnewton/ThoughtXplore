from django.db import models
from ThoughtXplore.txMisc.models import PermissionContentType
from ThoughtXplore.txUser.models import User


class MiscLogs(models.Model):
    """
        Log class for misc apps
    """
    LogsUser = models.ForeignKey(User)
    LogsObject = models.IntegerField()
    LogsPCI = models.ForeignKey(PermissionContentType)
    LogsIP = models.CharField(max_length=20)
    LogsTimeStamp = models.DateTimeField()
    LogsDescription = models.CharField(max_length=200)
    LogsPreviousState = models.CharField(max_length=500)