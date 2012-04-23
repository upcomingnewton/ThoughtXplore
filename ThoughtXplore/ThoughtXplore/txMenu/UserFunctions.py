from ThoughtXplore.txMenu.models import Menu
from ThoughtXplore.txMisc.enc_dec import Encrypt
from ThoughtXplore.txMenu.DatabaseFunctions import DBInertMenu,DBUpdateMenu,DBUpdateMultiple
from ThoughtXplore.txMenu.DBMessages import decode
from django.db import models
from cPickle import dumps, loads

class MenuFnx(models.Model):
    
    def __init__(self):
        self.encrypt = Encrypt()
    
    def getParentMenus(self):
        try:
            return Menu.objects.filter(MenuPid__exact=-1)
        except:
            return []
        
    def getSingleMenuItemById(self,menuid):
        try:
            return Menu.objects.filter(id__exact=menuid)
        except:
            return []
        
    def getAllMenu(self):
        try:
            return Menu.objects.all()
        except:
            return []
        
    def CreateMenuFromSite(self,name,desc,murl,pid,micon,by,ip):   
            details = {'name':name,
                       'desc':desc,
                       'murl':murl,
                       'pid':pid,
                       'micon':micon,
                       'by':by,
                       'ip':ip,
                       }
            result = DBInertMenu(details)
            if( int(result[0]) >= 1):
                return (result[0],int(result[1]),decode(int(result[0]), result[1],'CreateMenuFromSite'))
            else:
                return (result[0],decode(int(result[0]), result[1],'CreateMenuFromSite'))
            
    
    def UpdateMenuFromSite(self,mid,name,desc,murl,pid,micon,by,ip):
            tempm = Menu.objects.get(id=mid)
            details = {'mid':mid,
                       'name':name,
                       'desc':desc,
                       'murl':murl,
                       'pid':pid,
                       'micon':micon,
                       'maction':'UPDATE',
                       'logsdesc': tempm.encode("zip").encode("base64").strip(),
                       'prev':'prev',
                       'by':by,
                       'ip':ip,
                       }
            result = DBInertMenu(details)
            return (result[0],decode(int(result[0]), result[1],'UpdateMenuFromSite'))


    def UpdateMultipleMenuFromSite(self,csv_mid,permission,mpid,by,ip):
            details = {'csv_mid':csv_mid,
                       'mpid':mpid,
                       'permission':permission,
                       'logsdesc':csv_mid + '-' + permission,
                       'by':by,
                       'ip':ip,
                       }
            result = DBInertMenu(details)
            return (result[0],decode(int(result[0]), result[1],'UpdateMultipleMenuFromSite'))
    