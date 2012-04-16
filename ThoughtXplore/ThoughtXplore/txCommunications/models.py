from django.db import models
from ThoughtXplore.txMisc.models import StateContentType, PermissionContentType
from ThoughtXplore.txUser.models import User, Group
class Communication_Type(models.Model):
    type= models.CharField(max_length=100)
    SCI= models.ForeignKey(StateContentType)
  
class Communication_Templates(models.Model):
    Commtype_id=models.ForeignKey(Communication_Type)
    TemplateName=models.CharField(max_length=100)
    TemplateFormat=models.TextField()
    paramList=models.TextField()
    Author=models.ForeignKey(User)
    SCI= models.ForeignKey(StateContentType)

class Communications(models.Model):
    Commtype_id=models.ForeignKey(Communication_Type)
    FromUserID=models.ForeignKey(User)
    TemplateID=models.ForeignKey(Communication_Templates)
    Subject=models.TextField()
    ParameterDict=models.TextField()
    DateTimeSent=models.TextField()
    Message=models.TextField()
    SCI= models.ForeignKey(StateContentType)

class Communication_Groups(models.Model):
    Commtype_id=models.ForeignKey(Communication_Type)
    comm_id=models.ForeignKey(Communications)
    Groups= models.TextField()

class Message_Replies(models.Model):
    Commtype_id=models.ForeignKey(Communication_Type)
    FromUserID=models.ForeignKey(User)
    reply= models.TextField()
    SCI= models.ForeignKey(StateContentType)

class CommunicationLogs(models.Model):
    
    # user making changes
    LogsUser = models.ForeignKey(User)
    # row id being changed
    LogsObject = models.IntegerField()
    LogsPCI = models.ForeignKey(PermissionContentType)
    LogsIP = models.CharField(max_length=20)
    LogsTimeStamp = models.DateTimeField()
    LogsDescription = models.CharField(max_length=200)
    LogsPreviousState = models.CharField(max_length=5000)