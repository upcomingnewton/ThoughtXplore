from ThoughtXplore.txDatabaseHelper import DBhelper


def DBInsertmail(message_details):

    print message_details
    query="SELECT txEmails_db_entry("+message_details['FromUserID']+","+message_details['Commtype_id']+","+message_details['TemplateID']+",'"+message_details['Subject']+"','"+message_details['ParameterDict']+"','"+str(message_details['TimeStamp'])+"','"+str(message_details['Message'])+"','"+message_details['ToGroupID']+"','"+ message_details['ip']  +"');"
    print query
    return DBhelper.CallFunction(query)   
