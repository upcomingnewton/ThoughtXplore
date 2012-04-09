from django.shortcuts import render_to_response
from django.template import RequestContext , loader
from django.http import HttpRequest, HttpResponse

def Index(request):
    #return HttpResponse("you are at the page for registering users")
    #t = loader.get_template()
    #c = RequestContext({'title':'create user page'})
    #return HttpResponse(t.render(c))
    return render_to_response('txUserfb/register.htm',{'title':'create user page using fb plugin'},context_instance=RequestContext(request))

def RegisterUser(HttpRequest):
    
    return HttpResponse("here :)")