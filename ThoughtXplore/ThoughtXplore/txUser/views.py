# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.template import RequestContext , loader
from django.shortcuts import render_to_response
from ThoughtXplore.txUser.models import User
from ThoughtXplore.txUser.UserFunctions import UserFnx
import datetime
from ThoughtXplore.txMisc.enc_dec import Encrypt

def Index(request):
    #return HttpResponse("you are at the page for registering users")
    #t = loader.get_template()
    #c = RequestContext({'title':'create user page'})
    #return HttpResponse(t.render(c))
    return render_to_response('txUser/CreateUser.html',{'title':'create user page'},context_instance=RequestContext(request))

def RegisterUser(HttpRequest):

    newuser = UserFnx()
    print HttpRequest.POST.keys()
    entered_date = HttpRequest.POST['RegisterUser_dob']
    bday = entered_date.split('/')
    try:
        bday = datetime.date(int(bday[2]),int(bday[0]),int(bday[1]))
        print bday
        result = ""
        result = newuser.InsertUserFromSite(HttpRequest.POST['RegisterUser_email'], HttpRequest.POST['RegisterUser_pass'], HttpRequest.POST['RegisterUser_fname'], HttpRequest.POST['RegisterUser_mname'],HttpRequest.POST['RegisterUser_lname'], HttpRequest.POST['RegisterUser_gender'],bday, 'system', HttpRequest.META['REMOTE_ADDR'])
        #newuser.InsertUserFromSite(HttpRequest.POST['RegisterUser_email'], HttpRequest.POST['RegisterUser_pass'], HttpRequest.POST['RegisterUser_fname'], HttpRequest.POST['RegisterUser_mname'],HttpRequest.POST['RegisterUser_lname'], HttpRequest.POST['RegisterUser_gender'],bday, 'system', 'system', HttpRequest.META['REMOTE_ADDR'])
        
        return HttpResponse("after user creation page" +  str(result))
    except:
        return HttpResponse("error")
    
    
    #print HttpRequest.POST
    #print HttpRequest
    
    
    
def AuthenticateUserFromEmail(HttpRequest,token):
    au_user = UserFnx()
    try:
        print 'printing from view  '  + token
        e= Encrypt()
        token1=e.decrypt(token)
        
        token1=str(token1)
        print token1
        res = au_user.AuthenticateUserFromSite(token1, HttpRequest.META['REMOTE_ADDR'])
        print "here11"
        print str(res)
        return HttpResponse("you are viewing status of user registeration "  + str(res))
    except:
        return HttpResponse("error")
    
        
def LoginUserIndex(request):
    return render_to_response('txUser/Login.html',{},context_instance=RequestContext(request))
    


def LoginUser(HttpRequest): 
    emailid = HttpRequest.POST['emailid']
    password = HttpRequest.POST['password']
    user = UserFnx()
    user.LoginUser(emailid, password, 'testsite', HttpRequest.META['REMOTE_ADDR'])
    # password_disp1=encdec.safe_unicode(password)
    return HttpResponse("login details are : emailid : %s"%(emailid))
