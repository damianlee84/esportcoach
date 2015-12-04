"""this file connects all urls to application when being called."""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^findcoach/$', views.findcoach, name='findcoach'),
    url(r'^list_of_coaches/', views.list_of_coaches, name='list_of_coaches'),
    url(r'^tutorselected/(?P<tutor_username>[-\w]+)', views.tutorselected, name='tutorselected'),
    url(r'^reviewcoach/(?P<tutor_username>[-\w]+)', views.reviewcoach, name='reviewcoach'),
    url(r'^paymentpage/(?P<tutor_username>[-\w]+)', views.paymentpage, name='paymentpage'),
    url(r'^streampage/', views.streampage, name='streampage'),
]
