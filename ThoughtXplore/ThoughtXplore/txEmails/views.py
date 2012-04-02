from ThoughtXplore.txEmails.models import Emails, EmailMessageTypes, EmailTemplate
from django.core.mail import send_mass_mail, send_mail
from ThoughtXplore.txUser.models import User, UserGroup
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import re
from cPickle import dumps, loads
import string
from ThoughtXplore.txEmails.EmailFunctions import EmailFunx
pattern = re.compile(r'\s*("[^"]*"|.*?)\s*,')
def split(line):
    return [x[1:-1] if x[:1] == x[-1:] == '"' else x
            for x in pattern.findall(line.rstrip(',') + ',')]

@csrf_exempt
def addtemplate(HttpRequest):
    authorID= int(HttpRequest.POST["authorID"])
    EmailType= int(HttpRequest.POST["EmailType"])
    TemplateName= HttpRequest.POST["TemplateName"]
    paramList= HttpRequest.POST["paramList"]
    TemplateFormat= HttpRequest.POST["TemplateFormat"]
    
    paramList_=  dumps(paramList).encode("zip").encode("base64").strip()
    TemplateFormat_=dumps(TemplateFormat).encode("zip").encode("base64").strip()
    template= EmailTemplate()
    emailfunc= EmailFunx()
    
    emailfunc.dbInsertEmailTemplates(EmailType, TemplateName, TemplateFormat_, paramList_, authorID)

@csrf_exempt
def sendmail(HttpRequest):
    
    print "hi"
    
    fromUserID= HttpRequest.POST["fromUserID_"]
    subject= HttpRequest.POST["Subject_"]
    togroupIDs= HttpRequest.POST["ToGroupIDs_"]
    touserIDs= HttpRequest.POST["ToUserIDs_"] 
    paramList= HttpRequest.POST["paramList_"]
    TemplateID= HttpRequest.POST["TemplateID_"]
    EmailTypeID= HttpRequest.POST["EmailTypeID_"]
    print "hi"

    touserIDs_=[]
    togroupIDs_=[]
    if(touserIDs!=""):
        a= split(touserIDs)
        touserIDs_=[int(i) for i in a]
    
    if(togroupIDs!=""):
        a=split(togroupIDs)
        togroupIDs_=[int(i) for i in a]
    param = {
           'fromUserID':fromUserID,
           'Subject':subject,
           'TemplateID':TemplateID,
           'paramList':paramList,
           'togroupIDs':togroupIDs,
           'touserIDs':touserIDs,
           'EmailTypeID':EmailTypeID
            }
    print "lol"
    print param
    send_mails(param)
    
    HttpResponse("Done")
@csrf_exempt
def Indexaddtemplate(request):

    users_= User.objects.all()
    EmailTypes=EmailMessageTypes.objects.all()
    EmailTemplates=EmailTemplate.objects.all()
    i=0
    param_list_to_send=[]
    for item in EmailTemplate.objects.all():
        temp=[item.TemplateName,loads(item.paramList.decode("base64").decode("zip")) ]
        param_list_to_send.append(temp)
    
    return render_to_response('txEmailMessaging/emailing.htm',{'title':'Email','Users':users_,'EmailTypes' :EmailTypes, 'EmailTemplate':EmailTemplates, 'paramlist': param_list_to_send})

@csrf_exempt
def send_mails(param):
    
  
    
    to_id_list=[]
    for a in param['togroupIDs']:
            for b in UserGroup.objects.filter(Group=a):
                to_id_list.append(b.User_id)
    for a in param['touserIDs']:   
                to_id_list.append(a)
       
    to_email_list=[]
    for e in to_id_list:
        for f in User.objects.filter(id=e):
            to_email_list.append(f.UserEmail)
    
    for e in User.objects.filter(id=param['fromUserID']):
        from_=e.UserEmail
    
    for e in EmailTemplate.objects.filter(id=param['TemplateID']):
        Template=loads(e.TemplateFormat.decode("base64").decode("zip"))
        reqparam=loads(e.paramList.decode("base64").decode("zip"))
    paramList=param['paramList']
    param_list_=[]
   
    param_list_=string.split(paramList,',')
    
    
    reqparam_=string.split(reqparam,',')
    
    
        
    Template=str(Template)

    for i,v in zip(reqparam_,param_list_):    
        Template=Template.replace(i, v)
    message=Template
    
    datatuple=[param['Subject'], message,from_,to_email_list]
    
    #auth_user_="auth_user"
    #auth_password_="auth_password"
    send_mail(param['Subject'], message,from_, to_email_list, fail_silently=True)
    #send_mass_mail(datatuple, fail_silently=True)    
    #db entry
    to_id_list_=""
    to_group_list=""
    
    to_email_list_=""
    
    for a in to_email_list:
        to_email_list_+= a+", "
    if(param['togroupIDs']!=""):
        for a in param['togroupIDs']:
            to_group_list+=","+a
    for a in to_id_list:
        if(to_id_list_==""): to_id_list_=str(a)
        else:
            to_id_list_=","+str(a)
    if(to_id_list_==""):
        to_id_list_="Null"
    else:
        to_group_list="Null"
        
    paramList=dumps(paramList).encode("zip").encode("base64").strip()
    emailfunc= EmailFunx()
    emailfunc.mailInsertDB(param['fromUserID'],from_,  param['EmailTypeID'],param['TemplateID'], param['Subject'],paramList,to_group_list, to_id_list_, to_email_list_)
    
     
        