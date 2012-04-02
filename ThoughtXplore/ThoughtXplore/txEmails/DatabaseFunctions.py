from ThoughtXplore.txDatabaseHelper import DBhelper
from datetime import datetime

'''

FUNCTION insert_sent_user_mail(FromUserEmail text, FromUserid text, FromUserGroup text, 
       Subject text, 
       Message text,timestamp_ text, Attachment text,ToUserEmail text, 
       ToUserid text, ToUserGroup text )
  


FUNCTION insert_sent_group_mail(FromUserEmail text, FromUserid text, FromUserGroup text,
       Subject text, Message text,timestamp_ text, 
       Attachment text, ToGroupid text )
 
'''

def DBInsertmail(message_details):
    
  
   
        query="SELECT email_db_entry('"+message_details['FromUserEmail']+"','"+message_details['FromUserid']+"','"+message_details['FromUserGroup']+"','"+message_details['Subject']+"','"+message_details['Message']+"','"+message_details['timestamp_']+"','"+message_details['Attachment']+"','"+message_details['togroupIDs']+"','"+message_details['ToUserIDs']+"');"
    
        return DBhelper.CallFunction(query)   

    