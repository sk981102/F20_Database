from django.urls import path
from task import views

urlpatterns = [
    path('', views.ListFunc,name='task'),
    #path('submit', views.SubmitFunc),
    #path('View', views.ViewFunc),
]

