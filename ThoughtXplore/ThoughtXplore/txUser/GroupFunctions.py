from django.db import models
from ThoughtXplore.txUser.models import User,Group,SecGroup_Comm
from ThoughtXplore.txMisc.enc_dec import Encrypt
from DatabaseFunctions import *
from DBMessages import db_messages,decode



class GroupFnx(models.Model):
    
        def __init__(self):
            self.encrypt = Encrypt()
            
        def CreateGroup(self,gname,gdesc,gtype,entity,by,ip):
            # 1. call authentication db script
            details = {
                       'ip':ip,
                       'by':by,
                       'request':'INSERT',
                       'entity':entity,
                       'group_type_id':gtype,
                       'groupname':gname,
                       'groupdesc':gdesc,
                       }
            result = DBCreateGroup(details)
            if( result[0] == 1):
                return result
            else:
                return( int(result[0]),decode(int(result[0]),result[1],'CreateGroup'))
        
        def AddMenuToGroup(self,gid,mlist,by,ip,len_mlist):
            details = {
                       'ip':ip,
                       'by':by,
                       'menulist':mlist,
                       'groupid':gid,
                       'menuid_len':len_mlist,
                       'logsdesc':'logsdesc',
                       }
            result = DBAddMenuToGroup(details)
            print result
            return result
            #if( result[0] == 1):
            #    return result
            #else:
            #    return( int(result[0]),decode(int(result[0]),result[1],'CreateGroup'))
        
        def CreateGroupWithMenu(self,gname,gdesc,gtype,entity,by,ip,mlist):
            res = self.CreateGroup(gname,gdesc,gtype,entity,by,ip)
            print 'printing value of res', res
            if( res[0] == 1):
                print mlist
                str_selected_menu = ''
                count  = 0
                for x in mlist:
                    str_selected_menu = str_selected_menu + x + ','
                    count = count + 1
                str_selected_menu = str_selected_menu[:-1]
                print str_selected_menu, count
                print 'string version is ', str(str_selected_menu)
                res2 = self.AddMenuToGroup(res[1],str(str_selected_menu),by,ip,count)
                print "printing result of adding the menu's to group", res2
            
            
        def ListAllGroups(self):
            return Group.objects.all()
        
        
        def AddUserToGroup(self,groupid,userid,by_user,ip):
                str_userid = ''
                logsdesc = ""
                print userid
                for x in userid:
                    str_userid = str_userid + x + ','
                str_userid = str_userid[:-1]
                print str_userid
                details = {
                            'groupid':groupid,
                            'userid':str_userid,
                            'logsdesc':logsdesc,
                            'by_user':by_user,
                            'ip':ip,
                           }
                result = DBAddUserToGroup(details)
                print result
                return result