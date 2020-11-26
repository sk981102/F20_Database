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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from pages import views
#from my_admin import views as adminviews
from accounts.views import signup, signin, viewusers, myaccount, changepw, changeinfo, deleteaccount


urlpatterns = [
    path('', views.home_view, name='home'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('submitter/', views.submitter_landing_view, name='submitter'),
    path('task/', include('task.urls'),name='task'),
    path('rater/', views.rater_landing_view, name='rater'),
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
	path('submitter/upload', views.submitter_file_upload, name='upload'),
	path('submitter/apply', views.apply, name='apply'),
]
