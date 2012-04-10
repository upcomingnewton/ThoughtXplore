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

    
    
    
def AuthenticateUserFromEmail(HttpRequest,token):
    au_user = UserFnx()
    try:
        print 'printing from view  '  + token
        res = au_user.AuthenticateUserFromSite(token, HttpRequest.META['REMOTE_ADDR'])
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
    print "here"
    print result
    
    if( result[0] == 1 ):
        send_validation_email(email, result[1], fname, HttpRequest.META['REMOTE_ADDR'])
        
        encrypt = Encrypt()
        return redirect('/message/' + encrypt.encrypt( str(result[1])) + '/')


