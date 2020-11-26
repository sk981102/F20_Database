from django.urls import path
from task import views

urlpatterns = [
    path('', views.ListFunc,name='task'),
    path('upload', views.ApprovedTasks),
    #path('View', views.ViewFunc),
]

