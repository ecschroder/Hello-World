
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^trashure/$', 'trashure.views.index', name='the_index_view'),

	url(r'^trashure/(?P<junkpollitem_id>\d+)/$', 'trashure.views.detail', name='the_detail_view'),
	
	url(r'^admin/', include(admin.site.urls)),
)


	
	
	
# urlpatterns = patterns('',
    # (r'^polls/$', 'polls.views.index'),

    # (r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
#	matches http://127.0.0.1:8000/polls/34/
	
    # (r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
#	matches http://127.0.0.1:8000/polls/34/results/
	
    # (r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
#	matches http://127.0.0.1:8000/polls/34/vote/
    
	# url(r'^admin/', include(admin.site.urls)),
# )




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