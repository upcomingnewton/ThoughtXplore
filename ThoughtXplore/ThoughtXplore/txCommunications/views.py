from ThoughtXplore.txMisc.MiscFunctions import split
from ThoughtXplore.txCommunications.CommunicationFunctions import send_mails
from django.http import HttpResponse
from ThoughtXplore.txUser.models import User
from ThoughtXplore.txCommunications.models import Communication_Type,\
    Communication_Templates
from cPickle import dumps, loads
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from ThoughtXplore.txCommunications.CommunicationFunctions import send_mails

@csrf_exempt
def Indexnotices(request):
    user_= User.objects.all()
    CommType=Communication_Type.objects.filter(type="notice")
    print "here"
    t=0
    for i in CommType:
        t=i.id
    print "here1"
    if(t==0):
        TemplateID=Communication_Templates.objects.all()
    else:
        TemplateID=Communication_Templates.objects.filter(Commtype_id=t)
    
    print "here2"
    param_list_to_send=[]
    for item in Communication_Templates.objects.all():
        temp=[item.TemplateName,loads(item.paramList.decode("base64").decode("zip")) ]
        param_list_to_send.append(temp)   
    print "here3"
    return render_to_response('txCommunications/notice.htm',{'title':'Notices','Users':user_,'CommType' :CommType, 'Template':TemplateID, 'paramlist': param_list_to_send})

@csrf_exempt
def Indexemail(request):
    user_= User.objects.all()
    CommType=Communication_Type.objects.filter(type="email")
    print "here"
    t=0
    for i in CommType:
        t=i.id
    print "here1"
    if(t==0):
        TemplateID=Communication_Templates.objects.all()
    else:
        TemplateID=Communication_Templates.objects.filter(Commtype_id=t)
    
    print "here2"
    param_list_to_send=[]
    for item in Communication_Templates.objects.all():
        temp=[item.TemplateName,loads(item.paramList.decode("base64").decode("zip")) ]
        param_list_to_send.append(temp)   
    print "here3"
    return render_to_response('txCommunications/emailing.htm',{'title':'Email','Users':user_,'CommType' :CommType, 'Template':TemplateID, 'paramlist': param_list_to_send})

@csrf_exempt    
def sendemail(HttpRequest):
    
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
