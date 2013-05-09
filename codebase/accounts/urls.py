from django.conf.urls import patterns, url
from django.contrib.auth.views import login, password_reset, password_change
from accounts import views


urlpatterns = patterns('',

    url(r'^cropPicture/(?P<image_id>\d+)/$', views.cropPicture, name='cropPicture'),
    url(r'^cropPicture/$', views.cropPicture, name='cropPicture'),
    url(r'thumb', views.thumbnail_options, name='thumbnail_options'),
    # (r'login/$',  login),
    # (r'^accounts/logout/$', logout),
    # (r'^accounts/profile/$', test),
    url(r'picture', views.cropPicture, name='cropPicture'),
    (r'^changepassword/$', 'django.contrib.auth.views.password_change'),
    (r'^password_change_done/$', 'django.contrib.auth.views.password_change_done'),
    url(r'login', login, name='login'),#http://localhost:8000/stuntperformers/test

    url(r'logout', views.logout_user, name='logout'),#http://localhost:8000/stuntperformers/test
    # ex: /polls/
    # url(r'^$', views.index, name='index'),
    # # ex: /polls/5/
    url(r'profile', views.profile, name='profile'),
    url(r'register', views.register, name='register'),

    url(r'^user/password/reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    (r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/user/password/done/'}),
    (r'^user/password/done/$', 
        'django.contrib.auth.views.password_reset_complete'),
    #url(r'user_dashboard', views.user_dashboard, name='user_dashboard'),
    #(r'^logout/$', 'django.contrib.auth.views.logout',
     #                     {'next_page': '/successfully_logged_out/'})
    # url(r'changepassword', views.changepassword, name='changepassword'),
    
)