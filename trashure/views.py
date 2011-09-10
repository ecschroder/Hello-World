from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, Context, loader
from django.core.urlresolvers import reverse
from trashure.models import JunkPollItem



def index(response):
	
	toptrash = JunkPollItem.objects.order_by('rating_score')[:4]
	toptreasure = JunkPollItem.objects.order_by('-rating_score')[:2]
	mostcontroversial = JunkPollItem.objects.order_by('-controversy_score')[:3]
	

	return render_to_response(
		'trashure/index.html',
		dictionary={
			'toptrash': toptrash,
			'toptreasure': toptreasure,
			'mostcontroversial': mostcontroversial,
		},
		context_instance=RequestContext(response) 
	)


def detail(request, junkpollitem_id, vote):

	p = get_object_or_404(JunkPollItem, pk=junkpollitem_id)

	relatedtrash = JunkPollItem.objects.order_by('?')[:6]	# see QuerySet API reference
		
	if vote == 'treasure':
		p.treasure_counter += 1
		p.save()
	
	if vote == 'trash':
		p.trash_counter += 1
		p.save()

	return render_to_response(
		'trashure/detail.html',
		dictionary={ # this is the context dictionary
			'junkpollitem': p,
			'relatedtrash': relatedtrash,
		},								
		context_instance=RequestContext(request)
	)
