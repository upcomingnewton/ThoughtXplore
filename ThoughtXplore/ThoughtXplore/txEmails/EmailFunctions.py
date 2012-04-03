from ThoughtXplore.txEmails.models import Emails, EmailMessageTypes, EmailTemplate
from ThoughtXplore.txEmails.DatabaseFunctions import DBInsertmail, DBInsertEmailTemplate
class EmailFunx(Emails, EmailMessageTypes,EmailTemplate):
    

    def dbInsertEmailTemplates(self,EmailType, TemplateName, TemplateFormat, paramList, Author, ip):
        emailtemplate={
                   'EmailType': EmailType,
                   'TemplateName': TemplateName,
                   'TemplateFormat':TemplateFormat,
                   'paramList':paramList,
                   'Author':Author,    
                   'ip':ip               
                   }
        return DBInsertEmailTemplate(emailtemplate)
    def mailInsertDB(self,FromUserID, fromuseremail, EmailTypeID,TemplateID,Subject,ParameterDict, togroupIDs, touserIDs, ToUserEmails, ip): 
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
                       'ToUserEmails':ToUserEmails,
                       'ip':ip
                               } 
        print sent_message    
        return DBInsertmail(sent_message)
