from django.conf.urls import url
from django.urls import path
from rater import views

urlpatterns = [
    path('', views.assigned_landing_view, name='rater'),
]