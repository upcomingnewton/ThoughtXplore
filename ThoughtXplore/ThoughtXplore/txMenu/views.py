# Create your views here.
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import RequestContext , loader
from django.shortcuts import render_to_response, redirect
import datetime
from ThoughtXplore.txMisc.Validation import EmailValidate , StringValidate
from ThoughtXplore.txMisc.enc_dec import Encrypt
from ThoughtXplore.txMenu.UserFunctions import MenuFnx



def index_create(request):
    menuobj = MenuFnx()
    errorlist = []
    parentmenu = menuobj.getParentMenus()
    if ( len(parentmenu) == 0 ):
        errorlist.append('There are no parent menu items yet')
    return render_to_response('txadmin/CreateMenu.html',{'title':'create menu','par_menu':parentmenu,'errorlist':errorlist},context_instance=RequestContext(request))

def CreateMenuFromSite(HttpRequest):
    errorlist = []
    menuobj = MenuFnx()
    encrypt = Encrypt()
    parentmenu = menuobj.getParentMenus()
    try:
        strval = StringValidate()
        menuname = HttpRequest.POST['CreateMenu_name']
        if( strval.validate_alphanumstring( menuname) != 1 ):
            errorlist.append('Error in menuname')
        menudesc = HttpRequest.POST['CreateMenu_desc']
        if( strval.validate_alphanumstring( menudesc) != 1 ):
            errorlist.append('Error in menudesc')
        menuurl = HttpRequest.POST['CreateMenu_url']
        if( strval.validate_alphanumstring( menuurl) != 1 ):
            errorlist.append('Error in menuurl')
        #menuicon = HttpRequest.POST['CreateMenu_micon']
        #if( strval.validate_alphastring( menuicon) != 1 ):
        #    errorlist.append('Error in menuicon')
        menuicon = 'NULL'
        menupid = -1
        if( len(parentmenu) == 0 ):
            menupid = -1
        else:
            menupid  = HttpRequest.POST['CreateMenu_parmenu']
        result = menuobj.CreateMenuFromSite(menuname, menudesc, menuurl, menupid, menuicon,1,HttpRequest.META['REMOTE_ADDR'])
        print result[0]
        if( int(result[0]) >= 1):
            print 'it is 1'
            return HttpResponseRedirect('/user/menu/create/')
        else:
            return redirect('/message/' + encrypt.encrypt( str(result[1])) + '/')
    except KeyError as msg:
        errorlist.append(str(msg))
        print 'yes i am here'
        return render_to_response('txadmin/CreateMenu.html',{'title':'create menu','par_menu':parentmenu,'errorlist':errorlist},context_instance=RequestContext(HttpRequest))
    except:
        print 'lolwa'
        errorlist.append('There are no parent menu items yet')
        return render_to_response('txadmin/CreateMenu.html',{'title':'create menu','par_menu':parentmenu,'errorlist':errorlist},context_instance=RequestContext(HttpRequest))

def index_edit(request,menuid):
    menuobj = MenuFnx()
    errorlist = []
    p = menuobj.getSingleMenuItemById(menuid)
    if( len(p) == 0 ):
        errorlist.append('could not fetch menu details. Please try after sometime')
    parentmenu = menuobj.getParentMenus()
    if ( len(parentmenu) == 0 ):
        errorlist.append('There are no parent menu items yet')
    return render_to_response('txadmin/CreateMenu.html',{'title':'create menu','par':parentmenu,'errorlist':errorlist},context_instance=RequestContext(request))


def EditMenuFromSite(request):
    return HttpResponse("view page")

def ListMenu(HttpRequest,req_type):
    errorlist = []
    menuobj = MenuFnx()
    menu = menuobj.getAllMenu()
    if len(menu) == 0 :
        errorlist.append('No Menu items exist in the system')
    return render_to_response('txadmin/ListMenu.html',{'title':'list menu','menulist':menu,'errorlist':errorlist},context_instance=RequestContext(HttpRequest))