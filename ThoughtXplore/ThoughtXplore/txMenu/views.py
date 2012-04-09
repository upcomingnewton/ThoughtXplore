# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.template import RequestContext , loader
from django.shortcuts import render_to_response
import datetime
from ThoughtXplore.txMisc.enc_dec import Encrypt


def IndexAdd(request):
    return render_to_response('txadmin/CreateMenu.html',{'title':'create menu'},context_instance=RequestContext(request))


def IndexView(request):
    return HttpResponse("view page")

def IndexEdit(request):
    return HttpResponse("edit page")