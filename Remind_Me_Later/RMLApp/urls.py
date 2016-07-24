from django.conf.urls import url

from RMLApp import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^remindmelists/$', views.remindme_list),
    url(r'^remindmedetail/(?P<pk>[0-9]+)/$', views.remindme_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)