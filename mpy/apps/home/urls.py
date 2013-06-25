from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('mpy.apps.home.views',
    url(r'^$', 'index_vista', name = 'vista_principal'),
)
