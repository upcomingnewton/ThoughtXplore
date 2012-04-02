from django.http import HttpResponse
from django.shortcuts import render_to_response
from ThoughtXplore.txFileSystem.models import Folder_Basics,FolderTypes,FileTypes
from ThoughtXplore.txFileSystem.forms import CreateFolder, UploadFileForm,checkperm
from django.views.decorators.csrf import csrf_exempt
from ThoughtXplore.txUser.models import User

@csrf_exempt
def upload_File(request):
    if request.method== 'POST':
        form1= UploadFileForm(request.POST, request.FILES)
        if form1.is_valid():
            m=form1.handle_uploaded_file(request.FILES['file'])
            return HttpResponse('Success, '+m)
    else:
        form1= UploadFileForm()
        
    Folders= Folder_Basics.objects.all()
    users_=User.objects.all()    
    FileType= FileTypes.objects.all()
    return render_to_response('txFileSystem/uploadfiles.htm', {'title':'Upload File', 'form': form1, 'Folders':Folders,'Users':users_,'FileType':FileType})
    #return render_to_response('txFileSystem/uploadfiles.htm')
@csrf_exempt 
def createFolder(request):
    
    if request.method== 'POST' :
        form= CreateFolder(request.POST)
        if form.is_valid():
            status= checkperm(form, 'txFileSystem','folder_basics','CREATE_ACCESS_DELETE')[0][10]
            status='+'
            if(status=='-'):
                return HttpResponse("This operation is not supported by system for this user")
            else:
                form.process()
      
            return show_folders(request)
    else:
        return HttpResponse("Failed")
        #form= CreateFolder()
@csrf_exempt   
def show_folders(request):
    Folders= Folder_Basics.objects.all()
    users_= User.objects.all()
    foldertype= FolderTypes.objects.all()
    return render_to_response('txFileSystem/create_directory.htm',{'title':'Create New Directory','Folders': Folders, 'Users':users_, 'FolderType':foldertype})


    
