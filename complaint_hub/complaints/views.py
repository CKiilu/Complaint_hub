from django.shortcuts import render, HttpResponse

from .forms import *
from .models import *

import simplejson

# Create your views here.
# Home
def home(request):
	return render(request, 'home.html')

# Academic
def acad(request):
	return render(request, 'acad.html')

def makeup(request):
	form = AcademicComplaintForm(data=request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
	else:
		form = AcademicComplaintForm()
	context = {
	'form': form,
	}
	return render(request, 'make_up_validation.html', context)

def portal(request):
	form = AcademicComplaintForm(data=request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
	else:
		form = AcademicComplaintForm()
	context = {
	'form': form,
	}
	return render(request, 'portal_validation.html', context)

def special(request):
	form = AcademicComplaintForm(data=request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
	else:
		form = AcademicComplaintForm()
	context = {
	'form': form,
	}
	return render(request, 'special_validation.html', context)

def verify(request):
	form = AcademicComplaintForm(data=request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
	else:
		form = AcademicComplaintForm()
	context = {
	'form': form,
	}
	return render(request, 'result_validation.html', context)

# Adminstrative
def administrative(request):
	return render(request, 'admin.html')

def exeat(request):
	form = ExeatForm(data=request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
	else:
		form = ExeatForm()
	context = {
		'form': form, 
	}
	return render(request, 'admin_exeat.html', context)

def work_study(request):
	form = WorkStudyForm(data=request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
	else:
		form = WorkStudyForm()
	context = {
		'form': form, 
	}
	return render(request, 'admin_workstudy.html', context)

def ppd(request):
	form = PPDForm(data=request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
	else:
		form = PPDForm()
	context = {
		'form': form, 
	}
	return render(request, 'admin_ppd.html', context)

def admin_special(request):
	form = SpecialAdmRequestForm(data=request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
	else:
		form = SpecialAdmRequestForm()
	context = {
		'form': form, 
	}
	return render(request, 'admin_special.html', context)

# Questions
def faq(request):
	return render(request, 'faq.html')
	
def get_course_choices(request):
	if request.is_ajax():
		p_id = request.GET.get('p_id')
		data = {}
		courses = Program.objects.get(id=p_id).courses.values('courses')
		course_id = 1
		for course in courses:
			data[course_id] = course['courses']
			course_id += 1
			
		json = simplejson.dumps(data)
		return HttpResponse(json, content_type='application/json')