from django.db import models
from ThoughtXplore.txUser.models import User, UserGroup 
from ThoughtXplore.txEmails.DatabaseFunctions import DBInsertEmailTemplate, DBInsertmail
    
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
    def dbInsertEmailTemplates(self,EmailType, TemplateName, TemplateFormat, paramList, Author):
        emailtemplate={
                   'EmailType': EmailType,
                   'TemplateName': TemplateName,
                   'TemplateFormat':TemplateFormat,
                   'paramList':paramList,
                   'Author':Author                   
                   }
        return DBInsertEmailTemplate(emailtemplate)
  

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
    
    def mailInsertdb(self,FromUserID, fromuseremail, EmailTypeID,TemplateID,Subject,ParameterDict, togroupIDs, touserIDs, ToUserEmails): 
        print "here1"
        sent_message={
                       'FromUserID': FromUserID,
                       'FromUserEmail': str(fromuseremail), 
                       'EmailTypeID':EmailTypeID,
                       'TemplateID': TemplateID,
                       'Subject':Subject,
                       'ParameterDict': ParameterDict,
                       'ToGroupIDs':togroupIDs,
                       'ToUserIDs':touserIDs,
                       'ToUserEmails':ToUserEmails
                               }
        
        print sent_message
        return DBInsertmail(sent_message)

   