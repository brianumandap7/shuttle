from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from ticket.models import Tickets, Status



def fts(request):
	query = {
		
	}
	return render(request, 'fts/fts.html', query)

def head(request):
	query = {
		
	}
	return render(request, 'fts/head.html', query)

def exec(request):
	query = {
		
	}
	return render(request, 'fts/exec.html', query)






