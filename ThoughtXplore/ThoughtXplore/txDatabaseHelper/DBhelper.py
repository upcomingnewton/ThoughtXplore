'''
Created on Mar 3, 2012

@author: nitin
'''


from django.db import connection,transaction

def CallFunction(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    transaction.commit_unless_managed()
    row = cursor.fetchall()
    print row
    return row
    
if __name__=="__main__":
    CallFunction('SELECT * FROM "txUser_user";')