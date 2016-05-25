from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import render, HttpResponse, redirect

from .forms import *
from .models import *

import simplejson

# Create your views here.
# Home
@login_required()
def home(request):
	context = {
	}
	return render(request, 'home.html', context)
	
def more_details(request):
	staff = cache.get('staff')
	
	if StaffProfile.objects.filter(user=request.user).exists():
		return redirect('staff_home')
	elif StudentProfile.objects.filter(user=request.user).exists():
		return redirect('home')
	
	if staff == "Staff":
		form = StaffProfileForm(data=request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect('staff_home')
		else:
			form = StaffProfileForm()
	elif staff == "Student":
		form = StudentProfileForm(data=request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect('home')
		else:
			form = StudentProfileForm()
	
	context = {
		'form': form,
	}
	
	return render(request, 'user_profile.html', context)

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

# Staff pages
def staff_home(request):
	return render(request, 'staff_home.html')

def staff_acad(request):
	return render(request, 'acad.html')

def staff_makeup(request):
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
	return render(request, 'make_up_staff.html', context)

def staff_portal(request):
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
	return render(request, 'portal_staff.html', context)

def staff_special(request):
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
	return render(request, 'special_staff.html', context)

def staff_verify(request):
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
	return render(request, 'result_staff.html', context)

# Adminstrative
def staff_administrative(request):
	return render(request, 'admin.html')

def staff_exeat(request):
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
	return render(request, 'exeat_staff.html', context)

def staff_work_study(request):
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
	return render(request, 'workstudy_staff.html', context)

def staff_ppd(request):
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
	return render(request, 'PPD_staff.html', context)

def staff_admin_special(request):
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
	return render(request, 'special_admin_staff.html', context)
	
def staff(request):
	if request.is_ajax():
		teach = request.GET.get('staff')
		
		if teach == 'covenant':
			cache.set('staff', "Staff")
		else:
			cache.set('staff', "Student")
			
		data = {'member_type': teach}
		json = simplejson.dumps(data)
		return HttpResponse(json, 'application/json')
	
def get_course_choices(request):
	if request.is_ajax():
		p_id = request.GET.get('p_id')
		data = {}
		courses = Program.objects.get(id=p_id).courses.values()
		
		for course in courses:
			data[course['id']] = course['courses']
			
		json = simplejson.dumps(data)
		return HttpResponse(json, content_type='application/json')
		
def get_program(request):
	if request.is_ajax():
		d_id = request.GET.get('d_id')
		data = {}
		programs = Department.objects.get(id=d_id).programs.values()
		
		for program in programs:
			data[program['id']] = program['program']
			
		json = simplejson.dumps(data)
		return HttpResponse(json, content_type='application/json')