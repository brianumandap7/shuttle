from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User



def ticket(request):
	query = {
		
	}
	return render(request, 'ticket/ticket.html', query)


