from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Tickets, Status, Stations, shuttle, destination, current_loc, imhere, answers, questions, hdf, reserve
from login.models import Roles, Author



def ticket(request):
	query = {
		'role': Author.objects.filter(user = request.user),
		'tik': Tickets.objects.filter(user = request.user)
	}
	return render(request, 'ticket/dash.html', query)

def admindash(request):
	query = {
		'uc': Author.objects.all().count(),
		'tc': Tickets.objects.all().count(),
		'sc': shuttle.objects.all().count(),
		'cc': hdf.objects.all().count(),
	}
	return render(request, 'ticket/admindash.html', query)

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
	'sh': Stations.objects.all(),
	}
	return render(request, 'ticket/dashtrack.html', query)

def shuttle_track(request, tag=0):
	query = {
		'tag':tag,
		'curr': current_loc.objects.all(),
		'stat': Stations.objects.filter(station_id = tag),
		'res': reserve.objects.filter(user = request.user),
	}

	if request.method == "POST":
			db = reserve()
			db.user = request.user
			db.save()
	return render(request, 'ticket/shuttle_track.html', query)

def df(request):
	query = {
		'hd': hdf.objects.all()[:1],
		'ans': answers.objects.all(),
	}

	if request.method == "POST":
		db = hdf()
		db.q1_id = 1
		db.q2_id = 2
		db.q3_id = 3
		db.q4_id = 4
		db.q5_id = 5
		db.a1_id = request.POST.get('a1')
		db.a2_id = request.POST.get('a2')
		db.a3_id = request.POST.get('a3')
		db.a4_id = request.POST.get('a4')
		db.a5_id = request.POST.get('a5')
		db.email = request.POST.get('eadd')
		db.save()

		return HttpResponseRedirect('/ticket/conf')

	return render(request, 'ticket/hdf.html', query)

def conf(request):
	query = {
		'lat': hdf.objects.all().order_by('-id')[:1]
	}

	return render(request, 'ticket/conf.html', query)