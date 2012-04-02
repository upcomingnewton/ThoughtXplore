from django.db import models
from django.contrib.contenttypes.models import ContentType


# Create your models here.

class MiscState(models.Model):
    StateName  = models.CharField(max_length=50)
    StateDescription = models.CharField(max_length=500)
    
class StateContentType(models.Model):
    """
    This class defines the various states in which a current 
    object can be. EG, when a user is created, he / she may 
    have a state CREATED, which may change to ACTIVE or DELETE 
    some time after. 
    StateName = Name of the state
    StateDescription = Description of the state
    StateContentType = How this state related to various content types
    StateActive > 0 => active
    StateActive < 0 => inactive
    """
    State = models.ForeignKey(MiscState)
    StateContentType = models.ForeignKey(ContentType)
    StateActive = models.IntegerField()


class MiscPermission(models.Model):
    PermissionName = models.CharField(max_length=50)
    PermissionDescription = models.CharField(max_length=500)


class PermissionContentType(models.Model):
    """
        This class defines various permissions which are available for various 
        content types. A user or group users can change the state of a content 
        type if that corresponding permission is granted to them.
        it is used closely with users / group system.
        This class is also used for keeping logs.
        PermissionName = name of the permission
        PermissionDescription = description of the permission
        PermissionContentType = type of permission
        PermissionActive > 0 => active
        PermissionActive < 0 => inactive
    """
    Permission = models.ForeignKey(MiscPermission)
    PermissionContentType = models.ForeignKey(ContentType)
    PermissionActive = models.IntegerField()
    
class Entity(models.Model):
    """
        Entity represents all institutes / companies etc associated with the system.
        Like colleges col-1, col-2  etc  
        it also uses to classify users of a particular institute 
        like col1-student, col1-coordinator, col1-tpo etc etc
        EntityName = name of the entity
        EntityDescription = description 
        EntityState = Current state of the entity
    """
    EntityName = models.CharField(max_length=50)
    EntityDescription = models.CharField(max_length=500)
    SCI = models.ForeignKey(StateContentType)