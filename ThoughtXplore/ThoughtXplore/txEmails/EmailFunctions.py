from ThoughtXplore.txEmails.models import Emails, EmailMessageTypes, EmailTemplate

class EmailFunx(Emails, EmailMessageTypes,EmailTemplate):
    

    def DBInsertEmailTemplates(self, EmailType, TemplateName, TemplateFormat_, paramList_, authorID):
        return EmailTemplate.dbInsertEmailTemplates(self, EmailType, TemplateName, TemplateFormat_, paramList_, authorID)
        
        
      
    def DBmailInsert(self, fromUserID,from_, EmailTypeID,TemplateID,Subject,paramList,to_group_list, to_id_list_, to_email_list_):
    
        message= Emails()
        message.mailInsertdb( fromUserID,from_, EmailTypeID,TemplateID,Subject,paramList,to_group_list, to_id_list_, to_email_list_)
        