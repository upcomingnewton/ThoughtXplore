from django.db import models
from ThoughtXplore.txUser.models import User,Group,SecGroup_Comm
from ThoughtXplore.txMisc.enc_dec import Encrypt
from DatabaseFunctions import *
from DBMessages import db_messages,decode
from cPickle import dumps, loads
from aux_fun import MakeGroupMenu

class UserFnx(models.Model):
    
    def __init__(self):
        self.encrypt = Encrypt()
        
        
    def AuthenticateUserFromSite(self,emailid,ip):
        # 1. call authentication db script
        to_emailid = self.encrypt.decrypt(emailid)
        s = to_emailid.split('___')
        print s
        print to_emailid
        result = DBAuthenicateUser({'to_email':s[0],'by_email':'2','state':'AUTHENTICATED','perm':'USER_AU','ip':ip,'logsdesc':'USER_AU'})
        return( int(result[0]),decode(int(result[0]),result[1],'AuthenticateUserFromSite'))
        
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
        if( int(result[0]) >= 1):
            return (result[0],int(result[1]),decode(int(result[0]), result[1],'InsertUserFromSite'))
        else:
            return (result[0],decode(int(result[0]), result[1],'InsertUserFromSite'))
    
    def LoginUser(self,email,password,_type,ip):
        details = {'email':email,
                       'pass':self.encrypt.encrypt(password),
                       'login_type':_type,
                       'ip':ip}
                        
        result = DBLoginUser(details)
        if( int(result[0]) >= 1):
            MakeGroupMenu(result[1])
            return (result)
        else:
            return (result[0],decode(int(result[0]), result[1],'LoginUser'))
        
        
    def LogoutUser(self,loginid):
        details = {'loginid':self.encrypt.decrypt(loginid),
                   'logout_from':99,
                  }
                        
        result = DBLogoutUser(details)
        print result 
        return result
        #if( int(result[0]) >= 1):
        #    return (result)
        #else:
        #    return (result[0],decode(int(result[0]), result[1],'LoginUser'))
        
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
        return (result[0],decode(int(result[0]), result[1],'CreateNewGroup'))
    
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
        return (result[0],decode(int(result[0]), result[1],'CreateSecGroupForComm'))
    
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
        result = DBAddUsertoSecGroupForCommunications(details)
        return (result[0],decode(int(result[0]), result[1],'AddUserToSecGroupForComm'))
    
    
