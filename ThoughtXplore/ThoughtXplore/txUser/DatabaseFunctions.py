'''
Created on Mar 3, 2012

@author: nitin
'''
from ThoughtXplore.txDatabaseHelper import DBhelper
from datetime import datetime
#SELECT * FROM txUser_user_insert('testuser@test.com','testpass','fname_test','mname_test','lname_test','f',current_date,'system','INSERT','created_users','state=;group=;',1,'test');

def DBInsertUser(userdetails):
    query = "SELECT * FROM txUser_user_insert('" + userdetails['email'] + "','" + userdetails['pass'] + "','" + userdetails['fname'] + "','" + userdetails['mname'] + "','" + userdetails['lname'] + "','" + userdetails['gender'] + "','" + userdetails['bday'] + "','" + userdetails['entity'] + "','" + userdetails['state'] + "','" + userdetails['group'] + "','" + userdetails['logsdesc'] + "','" + str(userdetails['by_email']) + "','" + userdetails['ip'] +"'); "
    print query
    result =  DBhelper.CallFunction(query)
    print result
    return result[0]
    
def DBLoginUser(logindetails):
    query = "SELECT * FROM user_login('" + logindetails['email'] + "','" + logindetails['pass'] + "','" + logindetails['login_type'] + "','" + logindetails['ip'] + "','" + str(datetime.now()) + "');"
    print query
    result =  DBhelper.CallFunction(query)
    print result
    return result[0]
    
def DBLogoutUser(details):
    query = "SELECT * FROM user_logout(" + str(details['loginid']) + "," +  str(details['logout_from']) + ",'" + str(datetime.now()) + "');"
    print query
    result =  DBhelper.CallFunction(query)
    print result
    return result[0]
    
def DBAuthenicateUser(auth_details):
    #"SELECT * FROM txUser_user_statechange('" + auth_details['to_email'] + "','" + auth_details['by_email'] + "','" + auth_details['state'] + "','" + auth_details['perm'] + "','" + auth_details['ip'] + "','" + auth_details['logsdesc'] + "');"
    query = "SELECT * FROM txUser_user_statechange('" + auth_details['to_email'] + "','" + auth_details['by_email'] + "','" + auth_details['state'] + "','" + auth_details['perm'] + "','" + auth_details['ip'] + "','" + auth_details['logsdesc'] + "');"
    print query
    result =  DBhelper.CallFunction(query)
    print result
    return result[0]


def DBCreateSecGroupForCommunications(details):
    query = "SELECT * FROM  SecGroup_Comm_insert('" + details['groupid'] + "','" + details['permission'] + "','" + details['params'] + "','[-1]','" + details['logdesc'] + "'," + details['by'] + ",'" + details['ip'] + "');"
    print query
    #result =  DBhelper.CallFunction(query)
    #return result

def DBAddUsertoSecGroupForCommunications(details):
    query= "SELECT * FROM SecGroup_Comm_appned(" + str(details['groupid']) + ",'" + details['userid'] + "','" + details['params'] + "','" + details['permission'] + "','" + str(details['by']) + "');"
    print query
    result =  DBhelper.CallFunction(query)
    return result[0]

def DBCreateGroup(details):
    query=  "SELECT * FROM txUser_group_insert('" + details['groupname']  + "','" + details['groupdesc'] + "'," + str(details['group_type_id']) + ",'" + details['entity']  + "','" + details['request'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
    print query
    result =  DBhelper.CallFunction(query)
    print result
    return result[0]


def DBAddMenuToGroup(details):
    query=  "SELECT * FROM txUser_group_insert(" + str(details['groupid']) + ",'" + details['menulist'] + "'," + str(details['menuid_len']) + ",'" + details['logsdesc'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
    print query
    result =  DBhelper.CallFunction(query)
    print result
    return result[0]


def DBAddUserToGroup(details):
    query =  "SELECT * FROM txUser_usergroup_insert("  + str(details['groupid']) + ",'" + details['userid'] + "','" + details['logsdesc'] + "'," + str(details['by_user']) + ",'" + details['ip'] + "');"
    print query
    result =  DBhelper.CallFunction(query)
    print result
    return result[0]

def GetActiveMenusByGroupid(groupid):
    query =  'SELECT * FROM "txMenu_menu" WHERE id IN ( SELECT "Menu_id" FROM "txMenu_groupmenu" WHERE "Group_id"=' + str(groupid) + ' and "Active"=1);'
    print query
    result =  DBhelper.CallFunction(query)
    print result
    return result


