from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^admin/$','txUser.views.ListUsers'),
    url(r'^register/$','txUser.views.CreateUserIndex'),
    url(r'^register/new/$','txUser.views.CreateUserFromSite'),
    url(r'^message/(?P<message>\S+)/$','txUser.views.MessageIndex'),
    url(r'^authenticate/email/(?P<token>\S+)/(?P<refs>\d+)/$','txUser.views.AuthenticateUserFromEmail'),    url(r'^test/$','txMisc.views.test'),
          
        
        
)               