from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import RequestContext , loader
from django.shortcuts import render_to_response, redirect
from ThoughtXplore.txUser.models import User, Group
from ThoughtXplore.txUser.UserFunctions import UserFnx
import datetime
from ThoughtXplore.txMisc.Validation import EmailValidate , StringValidate
from ThoughtXplore.txMisc.enc_dec import Encrypt
from django.core.urlresolvers import reverse
from ThoughtXplore.txCommunications.CommunicationFunctions import send_validation_email
from ThoughtXplore.txMisc import enc_dec
from ThoughtXplore.txMenu.UserFunctions import MenuFnx
from ThoughtXplore.txUser.GroupFunctions import GroupFnx




def ListGroups(HttpRequest, req_type):
    msglist = []
    if req_type == "all":
        group = GroupFnx()
        grouplist = group.ListAllGroups()
        if ( len(grouplist) == 0):
                msglist.append("THERE NO GROUPS IN THE SYSTEM, YET")
        return render_to_response('txUser/ListGroup.html',{'grouplist':grouplist,'msglist':msglist },context_instance=RequestContext(HttpRequest))

def CreateGroup_Index(HttpRequest):
    msglist = []
    menuobj = MenuFnx()
    menulist = menuobj.getAllMenu()
    if ( len(menulist) == 0 ):
        msglist.append('There are no parent menu items yet')
    try:
       return render_to_response('txadmin/user_system/CreateGroup.html',{'msglist':msglist,'menulist':menulist},context_instance=RequestContext(HttpRequest))
    except:
       return HttpResponse("error")
   
def CreateGroup(HttpRequest):
    selected_menu = HttpRequest.POST.getlist('Group_MenuOptions')
    msglist = []
    gname = HttpRequest.POST['Group_Name']
    if gname is None:
        msglist.append("ERROR : group name is required")
    gdesc = HttpRequest.POST['Group_Desc']
    if gdesc is None:
            msglist.append("ERROR: group desc is required")
    menuobj = MenuFnx()
    menulist = menuobj.getAllMenu()
    if ( len(menulist) == 0 ):
        msglist.append('There are no parent menu items yet')
    if len(msglist) > 0:
        return render_to_response('txadmin/user_system/CreateGroup.html',{'msglist':msglist,'menulist':menulist},context_instance=RequestContext(HttpRequest))
    else:
        group = GroupFnx()
        group.CreateGroupWithMenu(gname, gdesc, 1, 'system', 1, 'test', selected_menu)
    return HttpResponse("thanks")

def AddUsers_Index(HttpRequest,gid):
    msglist = []
    #userobj = User()
    userlist = User.objects.all()
    if len(userlist) == 0:
        msglist.append("ERROR !!! there are no users in the system yet.")
    return render_to_response('txadmin/EditGroupUsers_AddUsers.html',{'msglist':msglist,'userlist':userlist, 'groupid':gid},context_instance=RequestContext(HttpRequest))

def EditUsers_Index(HttpRequest,gid):
    return HttpResponseRedirect("/user/group/" + str(gid) + "/users/add/")
    
    
def AddUsersToGroup(HttpRequest,gid):
    userlist = HttpRequest.POST.getlist('Group_Userid')
    group = GroupFnx()
    group.AddUserToGroup(gid, userlist, 1, 'test')