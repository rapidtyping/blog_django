from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^post/(\d+)/', 'app.views.post', name='post'),
    url(r'^posts/$', 'app.views.posts', name='posts'),
    url(r'^post/add/$', 'app.views.add', name='add'),

    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
