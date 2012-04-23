from django.conf.urls.defaults import patterns, include, url
from ThoughtXplore import txCommunications, txUser
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'ThoughtXplore.views.Index', name='home'),  
     url(r'^contacts/$', 'ThoughtXplore.views.IndexContacts', name='Contact Us'),
     url(r'^comm/', include('txCommunications.urls')),
     url(r'^usertest/',include('txUser.urls_group_testing')),
     url(r'^user/',include('txUser.urls')),
     url(r'^folders/',include('txFileSystem.urls')),
     url(r'^note/vice-chancellor/$','ThoughtXplore.views.NoteVCIndex'),
     url(r'^note/director/$','ThoughtXplore.views.NoteDirIndex'),
     url(r'^note/tpo/$','ThoughtXplore.views.NotetpoIndex'),    
)