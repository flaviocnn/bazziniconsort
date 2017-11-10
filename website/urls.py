from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^events/$', views.events, name='events'),
    url(r'^events/(?P<event_id>[0-9]+)/$', views.event, name='event'),
    url(r'^about/$', views.about, name='about'),
    url(r'^about/(?P<user_id>[0-9]+)/$', views.curriculum, name='curriculum'),
]