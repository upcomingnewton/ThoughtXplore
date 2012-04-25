from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    
    url(r'^admin/addnotices/(?P<token>\S+)/$','txCommunications.views.Indexnotices'),
    url(r'^admin/addnews/(?P<token>\S+)/$','txCommunications.views.IndexNews'),
    url(r'^email/$','txCommunications.views.Indexemail'),   
    url(r'^notice/view/(?P<ref>\S+)/$','txCommunications.views.Index_viewnotices'),   
    url(r'^news/view/(?P<ref>\S+)/$','txCommunications.views.Index_viewnews'),   
    url(r'^notice/iframe/(?P<ref>\S+)/$','txCommunications.views.iframeNotice'),   
    url(r'^notice/send/$','txCommunications.views.sendnotice'),   
    url(r'^addtemplate/$','txCommunications.CommunicationFunctions.addtemplate'),   
    url(r'^email/send/$','txCommunications.views.sendemail'),   


)