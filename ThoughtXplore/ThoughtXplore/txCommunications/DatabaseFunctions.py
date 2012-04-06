from ThoughtXplore.txDatabaseHelper import DBhelper


def DBInsertComm(message_details):

    print message_details

    query="SELECT CommunicationInsert("+message_details['FromUserID']+","+message_details['CommTypeID']+","+message_details['TemplateID']+",'"+message_details['Subject']+"','"+message_details['ParameterDict']+"','"+str(message_details['TimeStamp'])+"','"+str(message_details['Message'])+"','"+message_details['ToGroupIDs']+"','"+ message_details['ip']  +"');"
    print query
    return DBhelper.CallFunction(query)  
 
def DBInsertCommTemplate(details):
    
    CommTypeID=details['CommType']
    TemplateName=details['TemplateName']
    TemplateFormat=details['TemplateFormat']
    paramList=details['paramList']
    Author=details['Author']
    query="SELECT txInsertCommunicationTemplate("+str(CommTypeID)+",'"+TemplateName+"','"+TemplateFormat+"','"+ paramList+"',"+ str(Author)+",'"+ details['ip']  +"');"
    
    print query
    return DBhelper.CallFunction(query)

    