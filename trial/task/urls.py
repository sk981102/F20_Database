from django.urls import path
from django.conf.urls import url
from task import views

urlpatterns = [
    path('', views.ListFunc,name='task'),
    url(r'^(?P<pk>\d+)/$', views.TaskDetailView, name='task_detail'),
    url(r'^(?P<pk>\d+)/contract/$', views.ViewContract, name='contract'),
    url(r'^(?P<task_id>\d+)/(?P<submitter_id>\d+)/contract/apply/$', views.Applied, name='applied'),
]

