from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',    
    url(r'^par1/$','txUser.test_views.par1_index'),
    url(r'^par2/$','txUser.test_views.par2_index'),
    url(r'^par3/$','txUser.test_views.par3_index'),
    url(r'^par4/$','txUser.test_views.par4_index'),
    
    url(r'^par1/par11/$','txUser.test_views.child11_index'),
    url(r'^par1/par12/$','txUser.test_views.child12_index'),
    url(r'^par1/par13/$','txUser.test_views.child13_index'),
    url(r'^par1/par14/$','txUser.test_views.child14_index'),
    
    url(r'^par2/par21/$','txUser.test_views.child21_index'),
    url(r'^par2/par22/$','txUser.test_views.child22_index'),
    url(r'^par2/par23/$','txUser.test_views.child23_index'),
    url(r'^par2/par24/$','txUser.test_views.child24_index'),
    
    url(r'^par3/par31/$','txUser.test_views.child31_index'),
    url(r'^par3/par32/$','txUser.test_views.child32_index'),
    url(r'^par3/par33/$','txUser.test_views.child33_index'),
    url(r'^par3/par34/$','txUser.test_views.child34_index'),
    
    url(r'^par4/par41/$','txUser.test_views.child41_index'),
    url(r'^par4/par42/$','txUser.test_views.child42_index'),
    url(r'^par4/par43/$','txUser.test_views.child43_index'),
    url(r'^par4/par44/$','txUser.test_views.child44_index'),
    
)