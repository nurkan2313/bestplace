"""urlconf for the base application"""

from django.conf.urls import url
from profiles import views

urlpatterns = [
    url(r'^profile_detail_public/(?P<username>\S+)/$', views.profile_detail_public, name='profile_detail_public'),
    url(r'^profile_detail_private/$', views.profile_detail_private, name='profile_detail_private'),
    url(r'^profile_edit/$', views.profile_edit),
    url(r'^bookmarks/add/$', views.add_favorite, name='profiles_bookmark_add'),
    url(r'^bookmarks/remove/$', views.remove_favorite, name='profiles_bookmark_remove'),

    url(r'^bookmarks/$', views.profiles_bookmark_list, name='profiles_bookmark_list'),


]
