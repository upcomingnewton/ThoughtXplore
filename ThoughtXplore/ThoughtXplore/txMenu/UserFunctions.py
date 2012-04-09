from ThoughtXplore.txMenu.models import Menu
from ThoughtXplore.txMisc.enc_dec import Encrypt
from DatabaseFunctions import *

class UserFnx(Menu):
    
    def __init__(self):
        self.encrypt = Encrypt()
    
    def getParentMenus(self):
        try:
            return Menu.objects.filter(MenuPid__exact=-1)
        except:
            return []