'''
Created on Mar 3, 2012

@author: nitin
'''
from ThoughtXplore.txDatabaseHelper import DBhelper

def DBInsertUser(userdetails):
    query = "SELECT * FROM txUser_user_insert('" + userdetails['email'] + "','" + userdetails['pass'] + "','" + userdetails['fname'] + "','" + userdetails['mname'] + "','" + userdetails['lname'] + "','" + userdetails['gender'] + "','" + userdetails['bday'] + "','" + userdetails['entity'] + "','" + userdetails['by_email'] + "','" + userdetails['ip'] +"'); "
    print query
    result =  DBhelper.CallFunction(query)
    print result
    return result
    
def DBLoginUser(logindetails):
    query = "SELECT * FROM user_login('" + logindetails['email'] + "','" + logindetails['pass'] + "','" + logindetails['login_type'] + "','" + logindetails['ip'] + "');"
    print DBhelper.CallFunction(query)
    
def DBAuthenicateUser(auth_details):
    query = "SELECT * FROM txUser_user_authenicate('" + auth_details['to_email'] + "','" + auth_details['by_email'] + "','" + auth_details['ip'] + "','" + auth_details['type'] + "');"
    result =  DBhelper.CallFunction(query)
    return result