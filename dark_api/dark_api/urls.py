from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',  # NOQA
    # Examples:
    # url(r'^$', 'dark_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include('dark.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
