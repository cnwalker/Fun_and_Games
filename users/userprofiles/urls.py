from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^profile/$', 'userprofiles.views.user_profile'),
)
