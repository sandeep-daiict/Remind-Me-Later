from django.conf.urls import url

from RMLApp import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^remindmelists/$', views.remindme_list)
]
urlpatterns = format_suffix_patterns(urlpatterns)