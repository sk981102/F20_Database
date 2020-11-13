from django.conf.urls import url
from accounts import views as core_views
#from fallDB.accounts import view as core_views

urlpatterns = [
    url(r'^signup/$', core_views.signup, name='signup'),
]