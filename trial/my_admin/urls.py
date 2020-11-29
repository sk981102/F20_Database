from django.conf.urls import url
from my_admin import views 

urlpatterns = [
    url(r'^taskcreate', views.create, name='taskcreate'),
    url(r'^taskmanage/$', views.manage, name='taskmanage'),
    url(r'^taskmanage/(?P<pk>\d+)/$', views.task_submitters, name='submitters'),
]
