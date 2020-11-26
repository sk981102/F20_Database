from django.conf.urls import url
from my_admin import views
 
urlpatterns = [
    url(r'^taskcreate', views.create, name='taskcreate'),
]
