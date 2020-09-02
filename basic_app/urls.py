from django.conf.urls import url
from django.urls import path
from basic_app import views

app_name = 'basic_appTag'

urlpatterns = [
   url(r'^relative/$', views.relative, name='relative'),
   url(r'^other/$', views.other, name='other'),

   # path('', views.relative, name='relative'),
   #  path('', views.other, name='other'),
]