from django.conf.urls import patterns, url

from stuntperformers import views


urlpatterns = patterns('',
    url(r'test', views.test, name='test'),#http://localhost:8000/stuntperformers/test

    url(r'reg', views.register, name='reg'),#http://localhost:8000/stuntperformers/test
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    

    url(r'changepassword', views.changepassword, name='changepassword'),
    
)