from ThoughtXplore.txUser.models import User
from ThoughtXplore.txMisc.enc_dec import Encrypt
from DatabaseFunctions import *
from ThoughtXplore.txCommunications.models import Communication_Templates, Communication_Type
from ThoughtXplore.txCommunications.CommunicationFunctions import send_mails

class UserFnx(User):
    
    def __init__(self):
        self.encrypt = Encrypt()
        
        
    def AuthenticateUserFromSite(self,emailid,ip):

        # 1. call authentication db script
        print"here"
        print emailid
        res = DBAuthenicateUser({'to_email':emailid,'by_email':'AuthenticateUserDaemon@tx.com','ip':ip,'type':'USER_AU'})
        
        if ( res[0][0] == 695 ):
            # call here user email system
            print 'hi'
        return res
        
    def InsertUserFromSite(self,email,password,fname,mname,lname,gender,bday,entity,ip):
        
        print "here"       

        print "break"
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
        
        print "clear0"
        result = DBInsertUser(user)
        print "clear1"
        users_= User.objects.filter(UserEmail=email)
        user_admin=User.objects.filter(UserEmail="CreateUserDeamon@tx.com")
        temp=Communication_Templates.objects.filter(TemplateName="Register")
        commtype=Communication_Type.objects.filter(type="email")
        for i in temp:
            temp_id=i.id
        for i in users_:
            user_id= i.id
        for i in user_admin:
            user_id_admin= i.id
        for i in commtype:
            commtype_id=i.id
        print "here1"
        print user_id_admin
        print temp_id
        print email
        print user_id
        print commtype_id
        if ( result[0][0] == 601 ):
            
            param={
                   'fromUserID':user_id_admin,
                   'Subject':'Account Creation',
                   'TemplateID':temp_id,
                   'paramList':email,
                   'togroupIDs':[],
                   'touserIDs':[user_id],
                   'CommTypeID':commtype_id,
                    'ip':ip,
                    'email_code_name':'Auth_Email'

                   }
        print "lol"
        print param
        r= send_mails(param)
        print "done"
        
        return result
    
    def LoginUser(self,email,password,type,ip):
        details = {'email':email,
                       'pass':self.encrypt.encrypt(password),
                       'login_type':type,
                       'ip':ip}
                        
        DBLoginUser(details)
