#author: bugzzy

from django.db import models

from ThoughtXplore.txUser.models import User #,Group
from ThoughtXplore.txMisc.models import Entity, PermissionContentType, StateContentType
from ThoughtXplore.txFileSystem.DatabaseFunctions import DBInsertFolder,\
    DBInsertFile
from django.forms import ModelForm

class FolderTypes(models.Model):
    typeName= models.CharField(max_length=50)
    type_desc=models.TextField()

class FileTypes(models.Model):
    typeName= models.CharField(max_length=50)
    type_desc=models.TextField()

class Folder_Basics(models.Model):
    name= models.CharField(max_length=200, unique=True)
    
    desc=models.TextField()
    #parent_folder=models.IntegerField()  #0-For root
    #content_count= models.IntegerField()
    folder_type=models.ForeignKey(FolderTypes)
    '''timestamp_created= models.DateTimeField()
    timestamp_last_modified=models.DateTimeField()'''
    #creater=models.ForeignKey(User)
    #space_used= models.FloatField()
    #FolderSCI= models.ForeignKey(StateContentType)
    #FolderEntity= models.ForeignKey(Entity)
    Active= models.IntegerField()
    def __unicode__(self):
        return self.name
    
    def folderInsert(self, cuser_, folder_name, folder_desc, folder_type_):
        Folder_Basics= {
                        'cuser': cuser_,
                        'name': folder_name,
                        'desc':folder_desc,
                        'folder_type':folder_type_,
                        
                        }
        return DBInsertFolder(Folder_Basics)
        
    
'''    
class Folder_Permissions(models.Model):
    folder_id= models.ForeignKey(Folder_Basics)
    group_id= models.ForeignKey(Group)
    Folder_PCI=models.ForeignKey(PermissionContentType)
    Active=models.IntegerField()
    ResultingSCI= models.ForeignKey(StateContentType)  
  #  access_mode= models.IntegerField()  # 0-List Files only, 1-Access Only, 2-Create, Access & Delete
  #  files_access_mode= models.IntegerField() #0 All Read only, 1- All Read and Write, 2- File-specific Mode 
    '''
    
 
class Files_Basics(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    url=models.CharField(max_length=200)
    folder=models.ForeignKey(Folder_Basics)
    size=models.IntegerField()
    file_type= models.ForeignKey(FileTypes)
    user_created=models.ForeignKey(User)
#   timestamp_created=models.DateTimeField()
#   timestamp_last_modified=models.DateTimeField()
    ACTIVE=models.IntegerField()
   # FileSCI= models.ForeignKey(StateContentType)
    
    
    def __unicode__(self):
        return self.name
    
    def fileInsert(self, name, desc, url,folder_id, size,file_type_id,user_created_id):
        File_Basics= {
                        'name': name,
                        'desc': desc,
                        'url':url,
                        'size':size,
                        'folder_id': folder_id,
                        'file_type_id':file_type_id,
                        'user_created_id':user_created_id,
                        
                        }
        return DBInsertFile(File_Basics)
'''    
class Files_Permissions(models.Model):
    file_id= models.ForeignKey(Files_Basics)
    group_id=models.ForeignKey(Group)
    #files_access_mode= models.IntegerField() #0 All Read only, 1- All Read and Write
    filePCI= models.ForeignKey(PermissionContentType)
    ACTIVE= models.IntegerField()
    resultingSCI= models.ForeignKey(StateContentType)
   ''' 
class creater_user(models.Model):
    folder_id= models.ForeignKey(Folder_Basics)
    creater_uid=models.ForeignKey(User)
        
  
class fsSCI(models.Model):
    app= models.CharField(max_length=50)     #Files and Folder
    sci= models.ForeignKey(StateContentType)
class FileSystemLogs(models.Model):
    LogsUser = models.ForeignKey(User)
    LogsObject = models.IntegerField()
    LogsPCI = models.ForeignKey(PermissionContentType)
    LogsIP = models.CharField(max_length=20)
    LogsTimeStamp = models.DateTimeField()
    LogsDescription = models.CharField(max_length=200)
    LogsPreviousState = models.CharField(max_length=500)
    
class FileForm(ModelForm):
    class Meta:
        model=Files_Basics
