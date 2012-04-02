from django.http import HttpResponse, HttpRequest
from django.template import RequestContext , loader
from django.shortcuts import render_to_response

def test(request):
    return render_to_response('test/test.html',{'title':'test page'},context_instance=RequestContext(request))