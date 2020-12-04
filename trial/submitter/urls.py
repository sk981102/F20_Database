from django.urls import path
from django.conf.urls import url
from submitter import views

urlpatterns = [
	path('', views.submitter_landing_view, name='submitter'),
	url(r'^detail/(?P<pk>\d+)/$', views.list_uploaded_file, name='detail'),
	url(r'^detail/(?P<pk>\d+)/upload$', views.upload_new_file, name='upload'),
	url(r'^detail/(?P<pk>\d+)/submitted$', views.submitted, name='submitted'),
]
