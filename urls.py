
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from trashure.models import JunkPollItem

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^trashure/$', 'trashure.views.index', name='index'),

	url(r'^trashure/(?P<junkpollitem_id>\d+)/((?P<vote>\w+)/)?$', 'trashure.views.detail', name='detail'),
	
		
	url(r'^(?P<junkpollitem_id>\d+)/results/$', 'django.views.generic.list_detail.object_detail', name="results"),
	
	url(r'^admin/', include(admin.site.urls)),
)


from mystuff.settings import DEBUG
if DEBUG:
	urlpatterns += patterns('', (
		r'^static/(?P<path>.*)$',
		'django.views.static.serve',
		{'document_root': 'static'}
	))
	
	
if settings.DEBUG:
	urlpatterns += patterns('', url(
		r'^media/(?P<path>.*)$', 
		'django.views.static.serve', 
		{'document_root': settings.MEDIA_ROOT, }
	))