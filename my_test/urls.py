from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_test.views.home', name='home'),
    # url(r'^my_test/', include('my_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_note/', 'notes.views.add_note'),
    url(r'^random_note/', 'notes.views.random_note'),
    url(r'^count/', 'notes.views.count'),
    url(r'^$', 'notes.views.index'),
    url(r'^emb_widg/', 'notes.views.test_embeddable_widget'),
)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
