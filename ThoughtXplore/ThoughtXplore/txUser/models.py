from django.db import models
from ThoughtXplore.txMisc.models import Entity, StateContentType,\
    PermissionContentType
from DatabaseFunctions import DBInsertUser,DBLoginUser

# Create your models here.
class User(models.Model):
    UserEmail = models.CharField(max_length=500)
    UserPassword = models.CharField(max_length=500)
    UserBirthDate = models.DateField()
    UserFirstName = models.CharField(max_length=100)
    UserMiddleName = models.CharField(max_length=100)
    UserLastName = models.CharField(max_length=100)
    UserEntity = models.ForeignKey(Entity)
    SCI = models.ForeignKey(StateContentType)
    UserGender = models.CharField(max_length=1)
    
    def __unicode__(self):
        return self.UserEmail
    
class GroupType(models.Model):
    GroupTypeName = models.CharField(max_length=50)
    GroupTypeDescription = models.CharField(max_length=500)
    
class Group(models.Model):
    GroupName = models.CharField(max_length=50)
    GroupDescription = models.CharField(max_length=500)
    GroupType = models.ForeignKey(GroupType)
    SCI = models.ForeignKey(StateContentType)
    GroupEntity = models.ForeignKey(Entity)
    
class GroupPCI(models.Model):
    Group = models.ForeignKey(Group)
    PCI = models.ForeignKey(PermissionContentType)
    Active = models.IntegerField()
    ResultingSCI = models.ForeignKey(StateContentType)

class UserGroup(models.Model):
    User = models.ForeignKey(User)
    Group = models.ForeignKey(Group)
    SCI = models.ForeignKey(StateContentType)
    
class SecGroup_Comm(models.Model):
    Group = models.ForeignKey(Group)
    SCI = models.ForeignKey(StateContentType)
    User = models.TextField()
    LastUpdate = models.DateTimeField()
    UserParams = models.CharField(max_length=500)
    
class UserLogs(models.Model):
    # user making changes
    LogsUser = models.ForeignKey(User)
    # row id being changed
    LogsObject = models.IntegerField()
    LogsPCI = models.ForeignKey(PermissionContentType)
    LogsIP = models.CharField(max_length=20)
    LogsTimeStamp = models.DateTimeField()
    LogsDescription = models.CharField(max_length=200)
    LogsPreviousState = models.CharField(max_length=5000)
    
class LoginType(models.Model):
    SCI = models.ForeignKey(StateContentType)
    LoginTypeName = models.CharField(max_length=100)
    
class UserLoginLog(models.Model):
    user = models.ForeignKey(User)
    LoginTime = models.DateTimeField()
    Login_From = models.ForeignKey(LoginType)
    LogoutTime = models.DateTimeField()
    LoginIP = models.CharField(max_length=20)
    Logout_From = models.IntegerField()