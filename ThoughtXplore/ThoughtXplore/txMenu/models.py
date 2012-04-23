from django.db import models
from ThoughtXplore.txMisc.models import Entity, StateContentType,\
    PermissionContentType
from ThoughtXplore.txUser.models import Group
# Create your models here.
class Menu(models.Model):
    MenuName = models.CharField(max_length=100)
    MenuDesc = models.CharField(max_length=500)
    MenuUrl = models.CharField(max_length=500)
    MenuPid = models.IntegerField()
    SCI = models.ForeignKey(StateContentType)
    MenuIcon = models.CharField(max_length=500)
    
    
class GroupMenu(models.Model):
    Menu = models.ForeignKey(Menu)
    Group = models.ForeignKey(Group)
    Active = models.IntegerField()