# urls.py
from django.conf.urls import patterns, include, url
from dl_collections.models import Collection, Campus

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# from ajax_select import urls as ajax_select_urls
from django.contrib.sitemaps import GenericSitemap
# http://stackoverflow.com/questions/11428427/no-module-named-simple-error-in-django
# from django.views.generic.simple import redirect_to
admin.autodiscover()

collection_dict = {
    'queryset': Collection.objects.all(),
}

campus_dict = {
    'queryset': Campus.objects.all(),
}

sitemaps = {
    "UC": GenericSitemap(campus_dict),
    "collection_registry": GenericSitemap(collection_dict),
}

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^', include('dl_collections.urls')),
)
