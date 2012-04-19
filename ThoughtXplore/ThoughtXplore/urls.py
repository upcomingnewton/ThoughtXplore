from django.conf.urls.defaults import patterns, include, url
from ThoughtXplore import txCommunications

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'ThoughtXplore.views.Index', name='home'),  
     url(r'^contacts/$', 'ThoughtXplore.views.IndexContacts', name='Contact Us'),

    # url(r'^ThoughtXplore/', include('ThoughtXplore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^comm/', include('txCommunications.urls')),
    
    
    #url(r'^comm/admin/addnotices/(?P<token>\S+)/$','txCommunications.views.Indexnotices'),
    url(r'^user/',include('txUser.urls')),
    url(r'^note/vice-chancellor/$','ThoughtXplore.views.NoteVCIndex'),
    url(r'^note/director/$','ThoughtXplore.views.NoteDirIndex'),
    url(r'^note/tpo/$','ThoughtXplore.views.NotetpoIndex'),
    #url(r'^user/register/$','txUser.views.Index'),
    #url(r'^user/fb/register/$','txUserfb.views.Index'),
    #url(r'^user/fb/register/register$','txUserfb.views.RegisterUser'),
    #url(r'^user/register/register/$','txUser.views.RegisterUser'),
    #url(r'^user/register/status/$','txUser.views.RegisterUserStatus'),
    #url(r'^user/login/$','txUser.views.LoginUserIndex'),
    #url(r'^user/login/login/$','txUser.views.LoginUser'),
    url(r'^folders/',include('txFileSystem.urls')),
    
   
   # url(r'^messaging/email/$','txEmails.views.Indexaddtemplate'),
   # url(r'^messaging/email/addtemplate/$','txEmails.views.addtemplate'),
   
    #url(r'^messaging/email/send/$','txEmails.views.sendmail'),

    
)