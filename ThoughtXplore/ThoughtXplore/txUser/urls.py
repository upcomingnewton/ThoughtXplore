from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
                       
    url(r'^user/register/$','txUser.views.CreateUserIndex'),
    url(r'^user/register/new/$','txUser.views.CreateUserFromSite'),
    url(r'^user/admin/$','txUser.views.ListUsers'),
    url(r'^user/login/$','txUser.views.Login_index'),
    url(r'^user/login/log_in/$','txUser.views.log_in'),
    url(r'^user/login/log_out/$','txUser.views.log_out'),
    url(r'^user/forgetpassword/$','txUser.views.Forget_Pass_index'),
    url(r'^user/forget_pass/$','txUser.views.forget_pass'),
    url(r'^user/dashboard/$','txUser.views.view_dashboard'),
    url(r'^user/menu/create/$','txMenu.views.index_create'),
    url(r'^user/menu/create/new/$','txMenu.views.CreateMenuFromSite'),
    url(r'^user/menu/(?P<menuid>\d+)/edit/$','txMenu.views.index_edit'),
    url(r'^user/menu/(?P<menuid>\d+)/edit/update/$','txMenu.views.EditMenuFromSite'),
    url(r'^user/menu/list/(?P<req_type>\S+)/$','txMenu.views.ListMenu'),
    
    url(r'^user/group/create/$','txUser.views2.CreateGroup_Index'),
    url(r'^user/group/create/new/$','txUser.views2.CreateGroup'),
    url(r'^user/group/list/(?P<req_type>\S+)/$','txUser.views2.ListGroups'),
    
    url(r'^user/group/(?P<gid>\d+)/users/add/$','txUser.views2.AddUsers_Index'),
    url(r'^user/group/(?P<gid>\d+)/users/add/new/$','txUser.views2.AddUsersToGroup'),
    url(r'^user/group/(?P<gid>\d+)/users/edit/$','txUser.views2.EditUsers_Index'),
    
    url(r'^user/group/(?P<gid>\d+)/menu/edit/$','txUser.views2.EditMenu_Index'),
    url(r'^user/group/(?P<gid>\d+)/menu/edit/$','txUser.views2.AddMenu_Index'),
    
    url(r'^user/authenticate/email/(?P<token>\S+)/(?P<refs>\d+)/$','txUser.views.AuthenticateUserFromEmail'),
)               