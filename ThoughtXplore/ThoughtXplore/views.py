from django.http import HttpResponse, HttpRequest
from django.template import RequestContext , loader
from django.shortcuts import render_to_response

def Index(request):
    return render_to_response('main/index.html',context_instance=RequestContext(request))
def NoteVCIndex(request):
    return render_to_response('main/VC-Message.html',context_instance=RequestContext(request))
def NotetpoIndex(request):
    return render_to_response('main/TPO-Message.html',context_instance=RequestContext(request))
def NoteDirIndex(request):
    return render_to_response('main/Director-Message.html',context_instance=RequestContext(request))
