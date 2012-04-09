from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ThoughtXplore.views.home', name='home'),
    # url(r'^ThoughtXplore/', include('ThoughtXplore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
   
    url(r'^user/admin/$','txUser.views.ListUsers'),
    url(r'^user/register/$','txUser.views.CreateUserIndex'),
    url(r'^user/register/new/$','txUser.views.CreateUserFromSite'),
    url(r'^message/(?P<message>\S+)/$','txUser.views.MessageIndex'),
    #url(r'^user/register/$','txUser.views.Index'),
    #url(r'^user/fb/register/$','txUserfb.views.Index'),
    #url(r'^user/fb/register/register$','txUserfb.views.RegisterUser'),
    #url(r'^user/register/register/$','txUser.views.RegisterUser'),
    #url(r'^user/register/status/$','txUser.views.RegisterUserStatus'),
    #url(r'^user/login/$','txUser.views.LoginUserIndex'),
    #url(r'^user/login/login/$','txUser.views.LoginUser'),
    url(r'^user/authenticate/email/(?P<token>\S+)','txUser.views.AuthenticateUserFromEmail'),
    url(r'^test/$','txMisc.views.test'),
    url(r'^folders/create/$','txFileSystem.views.show_folders'),
    url(r'^folders/create/status/$','txFileSystem.views.createFolder'),
    url(r'^folders/show/$','txFileSystem.views.show_folders'),
    url(r'^files/upload/$','txFileSystem.views.upload_File'),
    url(r'^files/upload/status/$','txFileSystem.views.upload_File'),
    url(r'^messaging/email/$','txEmails.views.Indexaddtemplate'),
    url(r'^messaging/email/addtemplate/$','txEmails.views.addtemplate'),
    url(r'^comm/email/$','txCommunications.views.Indexemail'),   
    url(r'^comm/notice/$','txCommunications.views.Indexnotices'),   
    url(r'^comm/notice/send/$','txCommunications.CommunicationFunctions.send_notice'),   
    url(r'^comm/addtemplate/$','txCommunications.CommunicationFunctions.addtemplate'),   
    url(r'^comm/email/send/$','txCommunications.views.sendemail'),   
    url(r'^messaging/email/send/$','txEmails.views.sendmail'),

    
)