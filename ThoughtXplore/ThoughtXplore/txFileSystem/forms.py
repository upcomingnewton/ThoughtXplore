from django import forms
from ThoughtXplore.txFileSystem.models import Folder_Basics,Files_Basics
from django.http import HttpResponse
from ThoughtXplore.txDatabaseHelper import DBhelper
from ThoughtXplore.txFileSystem.DatabaseFunctions import DBInsertFile


def checkperm(form, applabel, modelreq,operation_requested ):

    
    by_user=form.cleaned_data['cuser']
    #applabel="txFileSystem"
    #modelreq="folder_basics"
    #operation_requested="CREATE_ACCESS_DELETE"
    query= "SELECT checkuserforpermission('"+by_user+"','"+applabel+"','"+modelreq+"','"+ operation_requested+"')"
    return DBhelper.CallFunction(query)[0]
    
class UploadFileForm(forms.Form):

    cuser= forms.CharField(max_length=50)
    filename= forms.CharField(max_length=50)
    file= forms.FileField
    folder_=forms.CharField(max_length=50)
    desc= forms.CharField(max_length=500)
    filetype=forms.CharField(max_length=50)
    
            
    
    def handle_uploaded_file(self, f):
        dest='/home/sarvpriye/git/ThoughtXplore/ThoughtXplore/ThoughtXplore/txFileSystem/uploadedcontent/'
        if(self.cleaned_data['filename']!= ""):
            dest+=self.cleaned_data['filename']
        else:
            dest+=f.name

        status= checkperm(self,'txFileSystem', 'folder_basics', 'CREATE_ACCESS_DELETE')
        status='+'
        if(status=='-'):
            return HttpResponse("This operation is not supported by system for this user")
        else:
            size= f.size
            size=str(size)
            url=dest
            
            destination = open(dest, 'wb+')
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
          
            message="File Uploaded in Folder: "+self.cleaned_data['folder_']+" by User:"+self.cleaned_data['cuser']

            name=self.cleaned_data['filename']
            desc= self.cleaned_data['desc']
            folder_id=self.cleaned_data['folder_']
            file_type_id=self.cleaned_data['filetype']
            user_created_id=self.cleaned_data['cuser']
            FileBasic= Files_Basics()
            FileBasic.fileInsert(name, desc, url, folder_id, size, file_type_id, user_created_id)
               
           
        
                
        return message
        
       
        

class CreateFolder(forms.Form):
    cuser= forms.CharField(max_length=50)
    Folder_Name=forms.CharField(max_length=50)
    Folder_Desc= forms.CharField(max_length=500)
    Folder_Type= forms.CharField(max_length=50)
    
    
        
            
            
    def process(self):
    
        cuser= self.cleaned_data['cuser']
        folder_name= self.cleaned_data['Folder_Name']
        desc= self.cleaned_data['Folder_Desc']
        folder_type= self.cleaned_data['Folder_Type']
        newFolder= Folder_Basics()
        newFolder.folderInsert(cuser, folder_name, desc, folder_type)
        # FolderCreater.creater_insert(HttpRequest.POST['folder_id_, creater_uid_)
        

