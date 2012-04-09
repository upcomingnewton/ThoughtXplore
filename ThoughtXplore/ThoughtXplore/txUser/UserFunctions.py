from ThoughtXplore.txUser.models import User
from ThoughtXplore.txMisc.enc_dec import Encrypt
from DatabaseFunctions import *
from DBMessages import db_messages,decode

class UserFnx(User):
    
    def __init__(self):
        self.encrypt = Encrypt()
        
        
    def AuthenticateUserFromSite(self,emailid,ip):
        # 1. call authentication db script
        print "here11"
        to_emailid = self.encrypt.decrypt(emailid)
        print to_emailid
        res = DBAuthenicateUser({'to_email':to_emailid,'by_email':'AuthenticateUserDaemon@tx.com','ip':ip,'type':'USER_AU'})
        if ( res[0][0] == 695 ):
            # call here user email system
            print 'hi'
        return res
        
    def InsertUserFromSite(self,email,password,fname,mname,lname,gender,bday,entity,ip):
        user = {'email':email, 
                'pass':self.encrypt.encrypt(password),
                'fname':fname,
                'lname':lname,
                'mname':mname,
                'gender':gender,
                'bday':str(bday),
                'entity':'system',
                'state':'INSERT',
                'group':'created_users',
                'logsdesc':'INSERT;created_users',
                'by_email':2,
                'ip':ip}
        result = DBInsertUser(user)
        return (result[0],decode(int(result[0]), result[1]))
    
    def LoginUser(self,email,password,_type,ip):
        details = {'email':email,
                       'pass':self.encrypt.encrypt(password),
                       'login_type':_type,
                       'ip':ip}
                        
        DBLoginUser(details)