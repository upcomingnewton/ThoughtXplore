from ThoughtXplore.txDatabaseHelper import DBhelper
from datetime import datetime


def DBInsertEmailTemplate(details):
    
    EmailType=details['EmailType']
    TemplateName=details['TemplateName']
    TemplateFormat=details['TemplateFormat']
    paramList=details['paramList']
    Author=details['Author']
    
    query="SELECT txInsertEmailTemplate("+str(EmailType)+",'"+TemplateName+"','"+TemplateFormat+"','"+ paramList+"','"+ str(Author)+"','"+ details['ip']  +"');"
    print query
    return DBhelper.CallFunction(query)
def DBInsertmail(message_details):
    

    timestamp=datetime.now()
    print message_details
    print "h"
    query="SELECT txEmails_db_entry("+message_details['FromUserID']+",'"+message_details['FromUserEmail']+"',"+message_details['EmailTypeID']+","+message_details['TemplateID']+",'"+message_details['Subject']+"','"+message_details['ParameterDict']+"','"+str(timestamp)+"','"+message_details['ToGroupIDs']+"','"+message_details['ToUserIDs']+"','"+message_details['ToUserEmails']+"','"+ message_details['ip']  +"');"
    print query
    return DBhelper.CallFunction(query)   

    