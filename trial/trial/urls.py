"""trial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from pages import views
#from my_admin import views as adminviews
from raw_data.views import createdatatype, createtypeschema, datatypelist
from accounts.views import signup, signin, viewusers, myaccount, changepw, changeinfo, deleteaccount, search, post_detail, type_detail#, test#, test2#,test

from task.views import taskdatatableschema

urlpatterns = [
    path('', views.home_view, name='home'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('submitter/', include('submitter.urls'), name='submitter'),
    path('task/', include('task.urls'),name='task'),
    path('rater/', include('rater.urls'), name='rater'),
    path('pjadmin/', views.admin_landing_view, name='pjadmin'),
    path('pjadmin/', include(('my_admin.urls','my_admin'), namespace='myadmin')),#mod needed
    path('admin/', admin.site.urls, name='admin'),
    path('signup/', signup, name='signup'),
    path('login/', signin, name='signin'),
    path('viewusers/', viewusers, name='viewusers'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/changepw/', changepw, name='changepw'),
    path('myaccount/changeinfo', changeinfo, name='changeinfo'),
    path('myaccount/deleteaccount', deleteaccount, name='deleteaccount'),
    path('search/', search, name='search'),
    path('createdatatype/', createdatatype, name='createdatatype'),
    path('createtypeschema', createtypeschema, name='createtypeschema'),
    path('datatypelist', datatypelist, name='datatypelist'),
    path('taskcreatesuccess/', taskdatatableschema, name='taskdatatableschema'),
    #path('type_detail/', test, name='type_detail'),
    #path('test2/', test2, name='test2'),
    url(r'^post_detail/(?P<pk>\d+)/', post_detail),
    url(r'^type_detail/(?P<pk>\d+)/', type_detail),
    #url(r'^type_detail/(?P<pk>\d+)/', type_detail),

] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
