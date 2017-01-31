# coding: utf-8
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from place import views as place_views
from profiles import views as profiles_views

admin.autodiscover()


urlpatterns = [
    url(r'^accounts/', include('accounts.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^$', place_views.show_list, name='home'),
    url(r'^search/$', place_views.search, name='search'),
    url(r'^detail/(?P<place_slug>\S+)/$', place_views.place_detail, name='detail'),
    url(r'^category/(?P<category_slug>\S+)/$', place_views.category_list, name='category'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^profile/add_favorite/(?P<place_id>\d+)$', profiles_views.add_favorite, name='add_favorite'),
    url(r'^comments/', include('django_comments.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +\
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
