"""urlconf for the base application"""

from django.conf.urls import url
from place import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^all/$', views.show_list, name='show_list'),
    url(r'^s/$', views.search, name='search'),
    url(r'^category_slug/(?P<category_slug>\S+)/$', views.category_list, name='category'),

]
