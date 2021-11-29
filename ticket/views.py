from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Tickets, Status, Stations, shuttle, destination, current_loc
from login.models import Roles, Author



def ticket(request):
	query = {
		'role': Author.objects.filter(user = request.user)
	}
	return render(request, 'ticket/dash.html', query)

def file(request):
	query = {
		
	}
	if request.method == "POST" and 'sb' in request.POST:
		db = Tickets()
		db.start_date = request.POST.get('dt')
		db.start_time = request.POST.get('tt')
		db.description = request.POST.get('dn')
		db.email = request.POST.get('ea')
		db.status_id = 1
		
		db.user = request.user
		db.save()

		return HttpResponseRedirect('/ticket/')
	return render(request, 'ticket/file.html', query)

def record(request):
	query = {
		'list': Tickets.objects.filter(user = request.user)
	}
	return render(request, 'ticket/record.html', query)

def track(request):
	query = {

	}
	return render(request, 'ticket/track.html', query)


def dashtrack(request):
	query = {

	}
	return render(request, 'ticket/dashtrack.html', query)