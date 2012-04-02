from django.db import models
from ThoughtXplore.txUser.models import User 
from ThoughtXplore.txMisc.models import PermissionContentType
    
class EmailMessageTypes(models.Model):
    
    TypeName = models.CharField(max_length=100)
    url =models.CharField(max_length=200)
    addninfo = models.CharField(max_length=100)
    
        
class EmailTemplate(models.Model):
    
    EmailType=models.ForeignKey(EmailMessageTypes)
    TemplateName= models.CharField(max_length=100)
    TemplateFormat=models.TextField()
    paramList=models.TextField()
    Author=models.ForeignKey(User)
    


class Emails(models.Model):

    FromUserID=models.ForeignKey(User)
    FromUserEmail=models.CharField(max_length=100)
    EmailTypeID= models.ForeignKey(EmailMessageTypes)
    TemplateID=models.ForeignKey(EmailTemplate)
    Subject=models.TextField()
    ParameterDict=models.TextField()
    DateTimeSent=models.TextField()
    ToGroupIDs=models.TextField()
    ToUserIDs=models.TextField()
    ToUserEmails= models.TextField()
    
    

class EmailLogs(models.Model):
    
    # user making changes
    LogsUser = models.ForeignKey(User)
    # row id being changed
    LogsObject = models.IntegerField()
    LogsPCI = models.ForeignKey(PermissionContentType)
    LogsIP = models.CharField(max_length=20)
    LogsTimeStamp = models.DateTimeField()
    LogsDescription = models.CharField(max_length=200)
    LogsPreviousState = models.CharField(max_length=5000)