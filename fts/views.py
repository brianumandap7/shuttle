from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from ticket.models import Tickets, Status



def fts(request):
	query = {
		'list': Tickets.objects.all(),
	}
	return render(request, 'fts/fts.html', query)

def head(request):
	query = {
		'list': Tickets.objects.all(),
	}
	return render(request, 'fts/head.html', query)

def exec(request):
	query = {
		
	}
	return render(request, 'fts/exec.html', query)

def headu(request, tag = 0):
	query = {
		'tag':tag,
		'upd':Tickets.objects.filter(ticket_id = tag).update(status_id = 2),
	}
	return render(request, 'fts/headu.html', query)






