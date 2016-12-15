from django.conf.urls import url

from . import views
app_name = 'crawl'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<sitename>.+)/$', views.list, name='image_list'),
    url(r'^(?P<sitename>.+)/(?P<sort>[vasm])$', views.list, name='image_list'),
    url(r'^(?P<sitename>.+)/(?P<page>[0-9]+)$', views.list, name='image_list'),
    url(r'^(?P<sitename>.+)/(?P<sort>[vasm])/(?P<page>[0-9]+)$', views.list, name='image_list'),
]
