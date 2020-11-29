from django.conf.urls import url
from my_admin import views 

app_name='MyAdmin'
urlpatterns = [
    url(r'^taskcreate', views.create, name='taskcreate'),
    url(r'^taskmanage/$', views.manage, name='taskmanage'),
    url(r'^taskmanage/(?P<pk>\d+)/$', views.task_submitters, name='submitters'),
    url(r'^taskmanage/(?P<task_id>\d+)/standard$', views.task_pass_standard, name='standard'),
    url(r'^taskmanage/(?P<task_id>\d+)/(?P<user_id>\w+)/$', views.sub_approve, name='approve'),
]
