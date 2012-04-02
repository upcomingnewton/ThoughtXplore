from ThoughtXplore.txUser.models import User
from ThoughtXplore.txMisc.enc_dec import Encrypt
from DatabaseFunctions import *


class UserFnx(User):
    
    def __init__(self):
        self.encrypt = Encrypt()
        
        
    def AuthenticateUserFromSite(self,emailid,ip):
        # 1. call authentication db script
        to_emailid = self.encrypt.decrypt(emailid)
        res = DBAuthenicateUser({'to_email':to_emailid,'by_email':'AuthenticateUserDaemon@tx.com','ip':ip,'type':'USER_AU'})
        return res
        
    def InsertUserFromSite(self,email,password,fname,mname,lname,gender,bday,entity,ip):
        user = {'email':email, 
                'pass':self.encrypt.encrypt(password),
                'fname':fname,
                'lname':lname,
                'mname':mname,
                'gender':gender,
                'bday':str(bday),
                'entity':entity,
                'by_email':'CreateUserDeamon@tx.com',
                'ip':ip}
        result = DBInsertUser(user)
        return result
    
    def LoginUser(self,email,password,type,ip):
        details = {'email':email,
                       'pass':self.encrypt.encrypt(password),
                       'login_type':type,
                       'ip':ip}
                        
        DBLoginUser(details)