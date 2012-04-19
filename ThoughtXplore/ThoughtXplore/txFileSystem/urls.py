from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
     
    url(r'^create/$','txFileSystem.views.show_folders'),
    url(r'^create/status/$','txFileSystem.views.createFolder'),
    url(r'^show/$','txFileSystem.views.show_folders'),
    url(r'^upload/$','txFileSystem.views.upload_File'),
    url(r'^upload/status/$','txFileSystem.views.upload_File'), 


)