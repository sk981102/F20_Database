from django.urls import path
from django.conf.urls import url
from task import views

urlpatterns = [
    path('', views.ListFunc,name='task'),
    url(r'^(?P<pk>\d+)/$', views.TaskDetailView, name='task_detail'),
    #path('submit', views.SubmitFunc),
    #path('View', views.ViewFunc),
]

