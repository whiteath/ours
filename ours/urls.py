from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ours.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',"ours.views.home"),
    url(r'^m/', include('message.urls')),
    url(r'^accounts/login/$',"ours.views.user_login"),
    url(r'^accounts/logout/$',"ours.views.user_logout"),
)
