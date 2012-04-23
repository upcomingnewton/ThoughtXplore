# Create your views here.
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import RequestContext , loader
from django.shortcuts import render_to_response, redirect
from ThoughtXplore.txUser.models import User
from ThoughtXplore.txUser.UserFunctions import UserFnx
import datetime
from ThoughtXplore.txMisc.Validation import EmailValidate , StringValidate
from ThoughtXplore.txMisc.enc_dec import Encrypt
from django.core.urlresolvers import reverse
from ThoughtXplore.txCommunications.CommunicationFunctions import send_validation_email
from ThoughtXplore.txMisc import enc_dec


    
def Login_index(HttpRequest):
    errorlist = []
    return render_to_response('txUser/Login.html',{'title':'Login','errorlist':errorlist},context_instance=RequestContext(HttpRequest))


def log_in(HttpRequest):
    msglist = []
    usrfn = UserFnx()
    enc = Encrypt()
    email = HttpRequest.POST['LoginUser_email']
    email_val = EmailValidate(email)
    if( email_val.validate() != 1):
        msglist.append('invalid email adress')
    password = HttpRequest.POST['LoginUser_pass']
    if( len(password) < 1):
        msglist.append('password required')
    try:
        result = usrfn.LoginUser(email, password, 'ADMIN-SITE', HttpRequest.META['REMOTE_ADDR'])
        print 'printing result : ',result
        if( int(result[4]) == 1):
            token = {"userid":result[0],"groupid":result[3],"loginid":enc.encrypt( str(result[2])),}
            print token
            HttpRequest.session["details"] = token
            return HttpResponseRedirect('/user/dashboard/')
        else:
            return HttpResponse( str(result))
    except:
        msglist.append("error")
        return render_to_response('txUser/Login.html',{'title':'Login','errorlist':msglist},context_instance=RequestContext(HttpRequest))
    
    
def log_out(HttpRequest):
    try:
        if "details" in HttpRequest.session:
            token = HttpRequest.session['details']
            print token['loginid']
            logout_user = UserFnx()
            print logout_user.LogoutUser(token['loginid'])
    except:
            print 'except'
    
def AuthenticateUserFromEmail(HttpRequest,token,refs):
    au_user = UserFnx()
    print refs
    try:
        print 'printing from AuthenticateUserFromEmail  '  + token
        result = au_user.AuthenticateUserFromSite(token, HttpRequest.META['REMOTE_ADDR'])
        print result
        if( result[0] >= 1 ):
            encrypt = Encrypt()
            return redirect('/message/' + encrypt.encrypt( str(result[1])) + '/')

    except:
        return HttpResponse("error")
    
        
def LoginUserIndex(request):
    return render_to_response('txUser/Login.html',{},context_instance=RequestContext(request))


def MessageIndex(request,message):
    encrypt = Encrypt()
    return render_to_response("txMisc/Message.html",{'message':encrypt.decrypt(message)},context_instance=RequestContext(request))    


def ListUsers(request):
    return render_to_response("txUser/ListUsers.html",{'title':'list users', 'users':User.objects.all()},context_instance=RequestContext(request))


def CreateUserIndex(request):
    return render_to_response('txUser/CreateUser.html',{'title':'create user page'},context_instance=RequestContext(request))


    

def CreateUserFromSite(HttpRequest):
    #return HttpResponse(str(HttpRequest))
    errorlist = []
    email = HttpRequest.POST['RegisterUser_email']
    email_val = EmailValidate(email)
    if( email_val.validate() != 1):
        errorlist.append('invalid email adress')
    pass1 = HttpRequest.POST['RegisterUser_pass']
    pass2 = HttpRequest.POST['RegisterUser_pass2']
    if( pass1 != pass2):
        errorlist.append('passwords do not match')
    str_val = StringValidate()
    fname = HttpRequest.POST['RegisterUser_fname']
    if(str_val.validate_alphastring(fname) != 1):
            errorlist.append('first name should contain only alphabets')
    mname = HttpRequest.POST['RegisterUser_mname']
    if( len(mname) > 0 ):
        if(str_val.validate_alphastring(mname) != 1):
            errorlist.append('middle name should contain only alphabets')
    lname = HttpRequest.POST['RegisterUser_lname']
    if(str_val.validate_alphastring(lname) != 1):
            errorlist.append('last name should contain only alphabets')
    bday = HttpRequest.POST['RegisterUser_dob']
    bday = bday.split('/')
    try:
        bday = datetime.date(int(bday[2]),int(bday[0]),int(bday[1]))
    except ValueError as err:
        errorlist.append('Invalid Birthdate, '+ err.message)
    gender = HttpRequest.POST['RegisterUser_gender']
    if gender== "-1" :
        errorlist.append('Please select your gender')
        
    if ( len(errorlist) > 0 ):
        return render_to_response('txUser/CreateUser.html',{'title':'create user page','errorlist':errorlist,'POST_DATA':HttpRequest.POST},context_instance=RequestContext(HttpRequest))
    else:
        insfnx = UserFnx()
        result = insfnx.InsertUserFromSite(email, pass2, fname, mname, lname, gender, bday,'system',HttpRequest.META['REMOTE_ADDR'])
    if( result[0] >= 1 ):
        send_validation_email(email, result[1], fname, HttpRequest.META['REMOTE_ADDR'])
        print result[2]
        encrypt = Encrypt()
        return redirect('/message/' + encrypt.encrypt( str(result[2])) + '/')

def view_dashboard(HttpRequest):
    msglist = []
    #print 'i am here, i have come here', HttpRequest.session.keys()
    if "details" in HttpRequest.session:
        #return HttpResponse(str(HttpRequest.session["details"]))
        return render_to_response('txUser/home.html',{"details":str(HttpRequest.session["details"]), 'msglist':msglist},context_instance=RequestContext(HttpRequest))
    else:
        encrypt = Encrypt()
        return redirect('/message/' + encrypt.encrypt("you need to login first") + '/')
