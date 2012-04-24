from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
                         
    # USER REGISTRATION , LOGIN AND RELATED STUFF
    url(r'^register/$','txUser.views.CreateUserIndex'),
    url(r'^register/new/$','txUser.views.CreateUserFromSite'),
    url(r'^login/$','txUser.views.Login_index'),
    url(r'^login/log_in/$','txUser.views.log_in'),
    url(r'^login/log_out/$','txUser.views.log_out'),
    url(r'^forgetpassword/$','txUser.views.Forget_Pass_index'),
    url(r'^forget_pass/$','txUser.views.forget_pass'),
    url(r'^authenticate/email/(?P<token>\S+)/(?P<refs>\d+)/$','txUser.views.AuthenticateUserFromEmail'),
    url(r'^dashboard/$','txUser.views.view_dashboard'),
    
    # USER GROUP MENU STUFF
    url(r'^menu/create/$','txMenu.views.index_create'),
    url(r'^menu/create/new/$','txMenu.views.CreateMenuFromSite'),
    url(r'^menu/(?P<menuid>\d+)/edit/$','txMenu.views.index_edit'),
    url(r'^menu/(?P<menuid>\d+)/edit/update/$','txMenu.views.EditMenuFromSite'),
    url(r'^menu/list/(?P<req_type>\S+)/$','txMenu.views.ListMenu'),
    
    
    # GROUP 

    url(r'^group/create/$','txUser.views2.CreateGroup_Index'),
    url(r'^group/create/new/$','txUser.views2.CreateGroup'),
    url(r'^group/list/(?P<req_type>\S+)/$','txUser.views2.ListGroups'),
    
    url(r'^group/(?P<gid>\d+)/users/add/$','txUser.views2.AddUsers_Index'),
    url(r'^group/(?P<gid>\d+)/users/add/new/$','txUser.views2.AddUsersToGroup'),
    url(r'^group/(?P<gid>\d+)/users/edit/$','txUser.views2.EditUsers_Index'),
    
    url(r'^group/(?P<gid>\d+)/menu/edit/$','txUser.views2.EditMenu_Index'),
    url(r'^group/(?P<gid>\d+)/menu/edit/$','txUser.views2.AddMenu_Index'),
    
    
    # admin
    url(r'^admin/$','txUser.views.ListUsers'),
)               