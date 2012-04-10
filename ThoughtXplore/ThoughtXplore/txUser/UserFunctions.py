from django.db import models
from ThoughtXplore.txUser.models import User,Group,SecGroup_Comm
from ThoughtXplore.txMisc.enc_dec import Encrypt
from DatabaseFunctions import *
from DBMessages import db_messages,decode
from cPickle import dumps, loads

class UserFnx(models.Model):
    
    def __init__(self):
        self.encrypt = Encrypt()
        
        
    def AuthenticateUserFromSite(self,emailid,ip):
        # 1. call authentication db script
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
        
        if( int(result[0]) == 1 ):
         return (result[0],int(result[1]))
        else:
         return (result[0],decode(int(result[0]), result[1]))
        
    
    def LoginUser(self,email,password,_type,ip):
        details = {'email':email,
                       'pass':self.encrypt.encrypt(password),
                       'login_type':_type,
                       'ip':ip}
                        
        DBLoginUser(details)
        
    def CreateNewGroup(self,name,desc,type,entity,by,ip):
        details = {
                        'name':name,
                        'desc':desc,
                        'type':type,
                        'entity':entity,
                        'permission':'INSERT',
                        'by':by,
                        'ip':ip
                   }
        result = DBCreateGroup(details)
        return (result[0],decode(int(result[0]), result[1]))
    
    def CreateSecGroupForComm(self,groupid,params,logsdec,by,ip):
        details = {
                    'groupid':groupid,
                    'permission':'INSERT',
                    'params':params,
                    'logdesc':logsdec,
                    'by':by,
                    'ip':ip
                   }
        result = DBCreateSecGroupForCommunications(details)
        return (result[0],decode(int(result[0]), result[1]))
    
    def AddUserToSecGroupForComm(self,groupid,userlist,by,ip):
        d = SecGroup_Comm.objects.all()
        #print d[0]
        t = []
        prev = ''
        params = ''
        for x in d:
            #print x.id
          if ( x.Group.id == groupid):


                params = x.UserParams


                prev = dumps(x.User).encode("zip").encode("base64").strip()


                t = x.User + ',' + userlist + '-1'


        details = {
                   'groupid':groupid,
                    'userid':str(t),
                    'permission':'UPDATE',
                    'params':params,
                    'logdesc':'AddUserToSecGroupForComm',
                    'prevstate':prev,
                    'by':by,
                    'ip':ip
                   }
        print 
        result = DBAddUsertoSecGroupForCommunications(details)
        return (result[0],decode(int(result[0]), result[1]))