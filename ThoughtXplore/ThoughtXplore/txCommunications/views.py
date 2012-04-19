from ThoughtXplore.txMisc.MiscFunctions import split
from ThoughtXplore.txCommunications.CommunicationFunctions import send_mails, send_notice
from django.http import HttpRequest,HttpResponse
from ThoughtXplore.txUser.models import User
from ThoughtXplore.txCommunications.models import Communication_Type,\
    Communication_Templates, Communications
from cPickle import dumps, loads
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext , loader
from ThoughtXplore.txCommunications.CommunicationFunctions import send_mails
from django.contrib import sessions
from ThoughtXplore.txMisc.enc_dec import Encrypt
import time
from time import mktime
from datetime import datetime
from ThoughtXplore.txMisc.MiscFunctions import decode_month 
from ThoughtXplore.txCommunications.DatabaseFunctions import DBInsertCommTemplate
def iframeNotice(request,ref):
    
    c=Communications.objects.filter(id=ref)
    for i in c:
        subject= i.Subject
        
        message= i.Message
        time=i.DateTimeSent
        
    message=loads(message.decode("base64").decode("zip"))
    
    subject=loads(subject.decode("base64").decode("zip"))

    return render_to_response('main/txCommunications/notice_iframe.html',{'Subject':subject,'message':message, 'time':time},context_instance=RequestContext(request))

def Index_viewnotices(request, token, ref):
    
    
    try:
        if token=="4089":
            admin=1
        else:
            admin=0
        
            
        for i in Communication_Type.objects.filter(type="notice"):
            ct_id=i.id
        print ct_id
        Comm= Communications.objects.filter(Commtype_id=ct_id)
        
        print "here"
        for i in Comm:
            a=i.DateTimeSent
            d2 = time.strptime(a,'%Y-%m-%d %H:%M:%S.%f')

            d3={'day':d2.tm_mday,
                'month':decode_month(d2.tm_mon),
                'year':d2.tm_year
                }       
            print d2
            dt = datetime.fromtimestamp(mktime(d2))
            print dt
            
                        
            #time_string=d2
            #d3= time.strftime(d2, "%Y %B %d %H %M %S")
            #print d2
            i.DateTimeSent=d3
            #i.ParameterDict=d2.tm_mday
            #i.TemplateID_id=decode_month(d2.tm_mon)
            i.Message=loads(i.Message.decode("base64").decode("zip"))
            i.Subject=loads(i.Subject.decode("base64").decode("zip"))
            print i.ParameterDict
        Com=[]
        for i in reversed(Comm):
            Com.append(i)
        Comm=Com
        
        print "done"
        return render_to_response('main/txCommunications/View_Notices.html',{'title':'Notices','admin':admin, 'Notices':Comm },context_instance=RequestContext(request))
    except:
        return HttpResponse("error")
    
def Indexnotices(request, token):
    
    try:
        if token=="4089":
            return render_to_response('main/txCommunications/Admin_Notices.html',{'title':'Admin Notices','fromUserID':3 },context_instance=RequestContext(request))
        
        else:
            return HttpResponse("UNAUTHORIZED ACCESS")
    except:
        return HttpResponse("error")
    
    t=0
    try:
        user_= User.objects.all()
        CommType=Communication_Type.objects.filter(type="notice")
        #print "here"
        
        for i in CommType:
            t=i.id
        #print "here1"
        if(t==0):
            TemplateID=Communication_Templates.objects.all()
        else:
            TemplateID=Communication_Templates.objects.filter(Commtype_id=t)
        
        #print "here2"
        param_list_to_send=[]
        for item in Communication_Templates.objects.all():
            temp=[item.TemplateName,loads(item.paramList.decode("base64").decode("zip")) ]
            param_list_to_send.append(temp)   
        #print "here3"
        return render_to_response('txCommunications/notice.htm',{'title':'Notices','Users':user_,'CommType' :CommType, 'Template':TemplateID, 'paramlist': param_list_to_send},context_instance=RequestContext(request))
    except:
        return HttpResponse("error")

def sendnotice(HttpRequest):
    
    details={
                'fromUserID': 1,
                'ip':HttpRequest.META['REMOTE_ADDR'],
                'subject':HttpRequest.POST['AdminNotices_subject'],
                'message':HttpRequest.POST['AdminNotices_message']                
             }
    
    print details 
    result= send_notice(details)
    print result
    result=result[1:-1]
    a= split(result)
    b=int(a[0])
    print b
    if b==500:
        message="The Notice has been successfully Posted."
    else:
        message="The Notice was not posted due to an error"
    encrypt = Encrypt()
    a= '/user/message/' + encrypt.encrypt( message) + '/'
    return redirect(str(a))
    


def Indexemail(request): 
    t=0
    try:
        user_= User.objects.all()
        CommType=Communication_Type.objects.filter(type="email")
        #print "here"
        #t=0
        for i in CommType:
            t=i.id
        print "here1"
        if(t==0):
            TemplateID=Communication_Templates.objects.all()
        else:
            TemplateID=Communication_Templates.objects.filter(Commtype_id=t)
        
        #print "here2"
        param_list_to_send=[]
        for item in Communication_Templates.objects.all():
            temp=[item.TemplateName,loads(item.paramList.decode("base64").decode("zip")) ]
            param_list_to_send.append(temp)   
        #print "here3"
        return render_to_response('txCommunications/emailing.htm',{'title':'Email','Users':user_,'CommType' :CommType, 'Template':TemplateID, 'paramlist': param_list_to_send},context_instance=RequestContext(request))
    except:
        return HttpResponse("error")
    
    
def addtemplate(HttpRequest):
    authorID= int(HttpRequest.POST["authorID"])
    CommType=Communication_Type.objects.filter(type="email")
    for i in CommType:
        CommTypeID=i.id
    print CommTypeID
    TemplateName= HttpRequest.POST["TemplateName"]
    paramList= HttpRequest.POST["paramList"]
    TemplateFormat= HttpRequest.POST["TemplateFormat"]
    paramList_=  dumps(paramList).encode("zip").encode("base64").strip()
    TemplateFormat_=dumps(TemplateFormat).encode("zip").encode("base64").strip()
    template= Communication_Templates()
    ip=HttpRequest.META['REMOTE_ADDR']
    print "test"
    details={
             'CommType':CommTypeID,
             'TemplateName':TemplateName,
             'paramList':paramList_,
             'TemplateFormat':TemplateFormat_,
             'Author':authorID,
             'ip':HttpRequest.META['REMOTE_ADDR'],
             }
    DBInsertCommTemplate(details)
    
    return HttpResponse("Done")

def sendemail(HttpRequest):
    try:
        fromUserID= HttpRequest.POST["fromUserID_"]
        for i in Communication_Type.objects.filter(type="email"):
            CommTypeID=i.id
        subject= HttpRequest.POST["Subject_"]
        togroupIDs= HttpRequest.POST["ToGroupIDs_"]
        paramList= HttpRequest.POST["paramList_"]
        TemplateID= HttpRequest.POST["TemplateID_"]
        if(togroupIDs!=""):
            a=split(togroupIDs)
            togroupIDs_=[int(i) for i in a]
        param = {
               'fromUserID':fromUserID,
               'Subject':subject,
               'CommTypeID':CommTypeID,
               'TemplateID':TemplateID,
               'paramList':paramList,
               'togroupIDs':togroupIDs_,
               'ip':HttpRequest.META['REMOTE_ADDR'],
               'comm_code_name': 'General Template Email'
                }
        print param
        send_mails(param)
        
        HttpResponse("Done")
    except:
        return HttpResponse("error")