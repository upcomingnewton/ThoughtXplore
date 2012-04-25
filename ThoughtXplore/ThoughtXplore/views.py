from django.http import HttpResponse, HttpRequest
from django.template import RequestContext , loader
from django.shortcuts import render_to_response

def Index(request):
    return render_to_response('main/index.html',{'title':'Home'},context_instance=RequestContext(request))
def NoteVCIndex(request):
    return render_to_response('main/VC-Message.html',{'title':'Vice Chancellor'},context_instance=RequestContext(request))
def NotetpoIndex(request):
    return render_to_response('main/TPO-Message.html',{'title':'TPO UIET'},context_instance=RequestContext(request))
def NoteDirIndex(request):
    return render_to_response('main/Director-Message.html',{'title':'Director UIET'},context_instance=RequestContext(request))
def IndexContacts(request):
    return render_to_response('main/contacts.html',{'title':'Contact Us'},context_instance=RequestContext(request))
def IndexLogin(request):
    return render_to_response('main/login.html',{'title':'User Login'},context_instance=RequestContext(request))
