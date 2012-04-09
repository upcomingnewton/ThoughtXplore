'''
Created on Mar 3, 2012

@author: nitin
'''
from ThoughtXplore.txDatabaseHelper import DBhelper

#SELECT * FROM txUser_user_insert('testuser@test.com','testpass','fname_test','mname_test','lname_test','f',current_date,'system','INSERT','created_users','state=;group=;',1,'test');

def DBInsertUser(userdetails):
    query = "SELECT * FROM txUser_user_insert('" + userdetails['email'] + "','" + userdetails['pass'] + "','" + userdetails['fname'] + "','" + userdetails['mname'] + "','" + userdetails['lname'] + "','" + userdetails['gender'] + "','" + userdetails['bday'] + "','" + userdetails['entity'] + "','" + userdetails['state'] + "','" + userdetails['group'] + "','" + userdetails['logsdesc'] + "','" + str(userdetails['by_email']) + "','" + userdetails['ip'] +"'); "
    print query
    result =  DBhelper.CallFunction(query)
    print result
    return result[0]
    
def DBLoginUser(logindetails):
    query = "SELECT * FROM user_login('" + logindetails['email'] + "','" + logindetails['pass'] + "','" + logindetails['login_type'] + "','" + logindetails['ip'] + "');"
    print DBhelper.CallFunction(query)
    
def DBAuthenicateUser(auth_details):
    query = "SELECT * FROM txUser_user_authenicate('" + auth_details['to_email'] + "','" + auth_details['by_email'] + "','" + auth_details['ip'] + "','" + auth_details['type'] + "');"
    print query
    result =  DBhelper.CallFunction(query)
    return result