from django.db import models
from ThoughtXplore.txUser.models import User, UserGroup 
from ThoughtXplore.txMessaging.txEmails.DatabaseFunctions import DBInsertmail
'''

A database class for storing the email logs



'''

class sent_messages(models.Model):

    FromUserEmail= models.EmailField()    #email id thru which the mail was sent  
    FromUserid=models.ForeignKey(User)    #user-id of the user doing the process
    FromUserGroup=models.ForeignKey(UserGroup)    #group id of this user
    Subject=models.TextField()
    Message=models.TextField()
    DateTimeSent=models.DateTimeField()
    Attachment= models.CharField(max_length=100)
    ToGroupIDs=models.TextField()
    ToUserIDs=models.TextField()
    
    def mailInsertdb(self, fromuseremail, fromuserid, fromusergroup,subject, message, attachment, togroupIDs, touserIDs): 
        
        if(self.isgroupinvolved):
            sent_messages={
                       'FromUserEmail': fromuseremail, 
                       'FromUserid': fromuserid, 
                       'FromUserGroup':fromusergroup,
                       'Subject': subject,
                       'Message': message,
                       'Attachment':attachment,
                       'ToGroupIDs':togroupIDs,
                       'ToUserIDs':touserIDs
                               }
        return DBInsertmail(sent_messages)

    
