from django.conf.urls import patterns, include, url
from journal.views import IndexView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chapters/', include('chapters.urls', namespace = 'chapters')),
    url(r'^discussions/', include('discussions.urls', namespace = 'discussions')),
    url(r'^accounts/', include('userprofiles.urls', namespace='userprofile')),

    #User Authentication URLs
    url(r'^accounts/auth/$', 'views.auth_view'),
    url(r'^accounts/login/$', 'views.login'),
    url(r'^accounts/logout/$', 'views.logout'),
    url(r'^accounts/invalid/$', 'views.invalid_login'),
    url(r'^accounts/register/$', 'views.register_user'),
    url(r'^accounts/register_success/$', 'views.register_success'),
)
