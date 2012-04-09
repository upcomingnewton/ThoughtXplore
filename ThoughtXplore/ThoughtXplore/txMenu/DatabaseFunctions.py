from ThoughtXplore.txDatabaseHelper import DBhelper

def DBInsertUser(userdetails):
    query = "SELECT * FROM txUser_user_insert('" + userdetails['email'] + "','" + userdetails['pass'] + "','" + userdetails['fname'] + "','" + userdetails['mname'] + "','" + userdetails['lname'] + "','" + userdetails['gender'] + "','" + userdetails['bday'] + "','" + userdetails['entity'] + "','" + userdetails['by_email'] + "','" + userdetails['ip'] +"'); "
    print query
    result =  DBhelper.CallFunction(query)
    print result
    return result