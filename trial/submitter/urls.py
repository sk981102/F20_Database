from django.urls import path
from django.conf.urls import url
from submitter import views

urlpatterns = [
	path('', views.submitter_landing_view, name='submitter'),
	url(r'^upload/(?P<pk>\d+)/$', views.submitter_file_upload, name='upload'),
	url(r'^upload/(?P<pk>\d+)/submitted$', views.submitted, name='submitted'),
]