from ThoughtXplore.txUser.models import User
from ThoughtXplore.txMisc.enc_dec import Encrypt
from DatabaseFunctions import *
from ThoughtXplore.txEmails.views import send_mails
from ThoughtXplore.txEmails.models import EmailTemplate, EmailMessageTypes

class UserFnx(User):
    
    def __init__(self):
        self.encrypt = Encrypt()
        
        
    def AuthenticateUserFromSite(self,emailid,ip):

        # 1. call authentication db script
        print"here"
        print emailid
        res = DBAuthenicateUser({'to_email':emailid,'by_email':'AuthenticateUserDaemon@tx.com','ip':ip,'type':'USER_AU'})
        
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
        user_admin=User.objects.filter(UserEmail="sarvpriye98@gmail.com")
        temp=EmailTemplate.objects.filter(TemplateName="Register")
        emailtype=EmailMessageTypes.objects.filter(TypeName="Registration")
        for i in temp:
            temp_id=i.id
        for i in users_:
            user_id= i.id
        for i in user_admin:
            user_id_admin= i.id
        for i in emailtype:
            emailtype_id=i.id
            
        if ( result[0][0] == 601 ):
            
            param={
                   'fromUserID':user_id_admin,
                   'Subject':'Account Creation',
                   'TemplateID':temp_id,
                   'paramList':email,
                   'togroupIDs':[],
                   'touserIDs':[user_id],
                   'EmailTypeID':emailtype_id
                   }
        print "lol"
        print param
        send_mails(param)
        print "done"
        
        return result
    
    def LoginUser(self,email,password,type,ip):
        details = {'email':email,
                       'pass':self.encrypt.encrypt(password),
                       'login_type':type,
                       'ip':ip}
                        
        DBLoginUser(details)