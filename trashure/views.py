from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from trashure.models import JunkPollItem, TrashChoice
from django.template import RequestContext, Context, loader


#def index(response):
#	return HttpResponse("Hello, world. You're at the poll index.")
#	try:
#		p = JunkPollItem.objects.get(pk=junkpollitem_id)
#	except JunkPollItem.DoesNotExist:
#		raise Http404
#	return render_to_response(
#		'trashure/index.html',
#		{'junkpollitem': p},
#		context_instance=RequestContext(response)
#		)

#def index(request):
#    latest_poll_list = JunkPollItem.objects.all().order_by('-pub_date')[:5]
#    t = loader.get_template('trashure/index.html')
#    c = Context({
#        'latest_poll_list': latest_poll_list,
#    })
#    return HttpResponse(t.render(c))


def index(response):
	return render_to_response(
		'trashure/index.html',
		context_instance=RequestContext(response) 
	)

		
def detail(response, junkpollitem_id):
#	return HttpResponse("Hello. Here's a detail.")
	try:
		p = JunkPollItem.objects.get(pk=junkpollitem_id)
	except JunkPollItem.DoesNotExist:
		raise Http404
	try:
		q = p.get_next_by_the_pub_date()				# get_next_by is built-in. Check it out.
	except JunkPollItem.DoesNotExist:
		q = JunkPollItem.objects.order_by('pk')[0]		# go back to the beginning 
	try:
		r = q.get_next_by_the_pub_date()
	except JunkPollItem.DoesNotExist:
		r = JunkPollItem.objects.order_by('pk')[1]
	try:
		s = r.get_next_by_the_pub_date()
	except JunkPollItem.DoesNotExist:
		s = JunkPollItem.objects.order_by('pk')[2]
	try:
		o = p.get_previous_by_the_pub_date()		# put these in context dictionary so they get passed to ..?
	except JunkPollItem.DoesNotExist:
		o = JunkPollItem.objects.order_by('-pk')[0] # can't use negative indexes in query set, but can use this trick
	try:
		n = o.get_previous_by_the_pub_date()
	except JunkPollItem.DoesNotExist:
		n = JunkPollItem.objects.order_by('-pk')[1]
	try:
		m = n.get_previous_by_the_pub_date()
	except JunkPollItem.DoesNotExist:
		m = JunkPollItem.objects.order_by('-pk')[2]		
		
#	try:
#		top_trash = JunkPollItem.objects.order_by('TrashChoice.votes()') # figure out how to write this
#	except
#		
	return render_to_response(
		'trashure/detail.html',
		dictionary={ # this is the context dictionary
			'previous_3': m,
			'previous_2': n,
			'previous_item': o,
			'junkpollitem': p,
			'next_item': q,			# the thing on the left can be whatevs. thing on the right is name you called it above.
			'next_2': r,
			'next_3': s,

		},								
		context_instance=RequestContext(response)
	)
		
#	top_trash = JunkPollItem.objects.get(pk=junkpollitem_id)
#	top_treasure = JunkPollItem.objects.get(pk=junkpollitem_id)	
		
		
#		polls = JunkPollItem.objects.filter(pk__lte=p.pk)[:5]
#		polls += JunkPollItem.objects.filter(pk__gte.p.pk)[:5]
#		add to ...  {'junkpollitem': p,'poll_list': polls}		
# this is where you want to determine which images will show & return them		




# pk means primary key, (in this case passed to views.py by urlconf, which is set in urls.py)
		