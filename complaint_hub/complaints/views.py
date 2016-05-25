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
	if StaffProfile.objects.filter(user=request.user).exists():
		return redirect('staff_home')
	context = {
	}
	return render(request, 'home.html', context)

@login_required()	
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
@login_required()
def acad(request):
	if StaffProfile.objects.filter(user=request.user).exists():
		return redirect('staff_acad')
	return render(request, 'acad.html')

@login_required()
def makeup(request):
	if StaffProfile.objects.filter(user=request.user).exists():
		return redirect('staff_makeup')
	form = AcademicComplaintForm(data=request.POST)
	user = StudentProfile.objects.get(user=request.user.id)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = user
		instance.request_type = "Makeup"
		instance.save()
		return redirect('acad')
	else:
		print [(field.label, field.errors) for field in form]
		form = AcademicComplaintForm()
	context = {
	'form': form,
	}
	return render(request, 'make_up_validation.html', context)

@login_required()
def portal(request):
	if StaffProfile.objects.filter(user=request.user).exists():
		return redirect('staff_portal')
	form = AcademicComplaintForm(data=request.POST)
	user = StudentProfile.objects.get(user=request.user.id)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = user
		instance.request_type = "Portal"
		instance.save()
		return redirect('acad')
	else:
		form = AcademicComplaintForm()
	context = {
	'form': form,
	}
	return render(request, 'portal_validation.html', context)

@login_required()
def special(request):
	if StaffProfile.objects.filter(user=request.user).exists():
		return redirect('staff_special')
	form = AcademicComplaintForm(data=request.POST)
	user = StudentProfile.objects.get(user=request.user.id)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = user
		instance.request_type = "Special"
		instance.save()
		return redirect('acad')
	else:
		form = AcademicComplaintForm()
	context = {
	'form': form,
	}
	return render(request, 'special_validation.html', context)

@login_required()
def verify(request):
	if StaffProfile.objects.filter(user=request.user).exists():
		return redirect('staff_verify')
	form = AcademicComplaintForm(data=request.POST)
	user = StudentProfile.objects.get(user=request.user.id)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = user
		instance.request_type = "Result"
		instance.save()
		return redirect('acad')
	else:
		form = AcademicComplaintForm()
	context = {
	'form': form,
	}
	return render(request, 'result_validation.html', context)

# Adminstrative
@login_required()
def administrative(request):
	if StaffProfile.objects.filter(user=request.user).exists():
		return redirect('staff_administrative')
	return render(request, 'admin.html')

@login_required()
def exeat(request):
	if StaffProfile.objects.filter(user=request.user).exists():
		return redirect('staff_exeat')
	form = ExeatForm(data=request.POST)
	user = StudentProfile.objects.get(user=request.user.id)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = user
		instance.save()
		return redirect('administrative')
	else:
		form = ExeatForm()
	context = {
		'form': form, 
	}
	return render(request, 'admin_exeat.html', context)

@login_required()
def work_study(request):
	if StaffProfile.objects.filter(user=request.user).exists():
		return redirect('staff_work_study')
	form = WorkStudyForm(data=request.POST)
	user = StudentProfile.objects.get(user=request.user.id)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = user
		instance.save()
		return redirect('administrative')
	else:
		form = WorkStudyForm()
	context = {
		'form': form, 
	}
	return render(request, 'admin_workstudy.html', context)

@login_required()
def ppd(request):
	if StaffProfile.objects.filter(user=request.user).exists():
		return redirect('staff_ppd')
	form = PPDForm(data=request.POST)
	user = StudentProfile.objects.get(user=request.user.id)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = user
		instance.save()
		return redirect('administrative')
	else:
		form = PPDForm()
	context = {
		'form': form, 
	}
	return render(request, 'admin_ppd.html', context)

@login_required()
def admin_special(request):
	if StaffProfile.objects.filter(user=request.user).exists():
		return redirect('staff_admin_special')
	form = SpecialAdmRequestForm(data=request.POST)
	user = StudentProfile.objects.get(user=request.user.id)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = user
		instance.save()
		return redirect('administrative')
	else:
		form = SpecialAdmRequestForm()
	context = {
		'form': form, 
	}
	return render(request, 'admin_special.html', context)

# Questions
@login_required()
def faq(request):
	return render(request, 'faq.html')

# Staff pages
@login_required()
def staff_home(request):
	if StudentProfile.objects.filter(user=request.user).exists():
		return redirect('home')
	return render(request, 'staff_home.html')

@login_required()
def staff_acad(request):
	if StudentProfile.objects.filter(user=request.user).exists():
		return redirect('acad')
	return render(request, 'staff_acad.html')

@login_required()
def staff_makeup(request):
	if StudentProfile.objects.filter(user=request.user).exists():
		return redirect('makeup')
	complaints = AcademicComplaint.objects.filter(request_type="Makeup").all()
	if request.GET.get('id'):
		complaint_id = request.GET.get('id')
		c = AcademicComplaint.objects.get(id=complaint_id)
		c.delete()
	
	context = {
	'complaints': complaints,
	}
	return render(request, 'make_up_staff.html', context)

@login_required()
def staff_portal(request):
	if StudentProfile.objects.filter(user=request.user).exists():
		return redirect('portal')
	complaints = AcademicComplaint.objects.filter(request_type="Portal").all()
	if request.GET.get('id'):
		complaint_id = request.GET.get('id')
		c = AcademicComplaint.objects.get(id=complaint_id)
		c.delete()
	
	context = {
	'complaints': complaints,
	}
	return render(request, 'portal_staff.html', context)

@login_required()
def staff_special(request):
	if StudentProfile.objects.filter(user=request.user).exists():
		return redirect('special')
	complaints = AcademicComplaint.objects.filter(request_type="Special").all()
	
	context = {
	'complaints': complaints,
	}
	return render(request, 'special_staff.html', context)

@login_required()
def staff_verify(request):
	if StudentProfile.objects.filter(user=request.user).exists():
		return redirect('verify')
	complaints = AcademicComplaint.objects.filter(request_type="Result").all()
	if request.GET.get('id'):
		complaint_id = request.GET.get('id')
		c = AcademicComplaint.objects.get(id=complaint_id)
		c.delete()
	
	context = {
	'complaints': complaints,
	}
	return render(request, 'result_staff.html', context)

# Adminstrative
@login_required()
def staff_administrative(request):
	if StudentProfile.objects.filter(user=request.user).exists():
		return redirect('administrative')
	return render(request, 'staff_admin.html')

@login_required()
def staff_exeat(request):
	if StudentProfile.objects.filter(user=request.user).exists():
		return redirect('exeat')
	complaints = Exeat.objects.all()
	if request.GET.get('id'):
		complaint_id = request.GET.get('id')
		c = Exeat.objects.get(id=complaint_id)
		c.delete()
	context = {
	'complaints': complaints,
	}
	return render(request, 'exeat_staff.html', context)

@login_required()
def staff_work_study(request):
	if StudentProfile.objects.filter(user=request.user).exists():
		return redirect('work_study')
	complaints = WorkStudy.objects.all()
	if request.GET.get('id'):
		complaint_id = request.GET.get('id')
		c = WorkStudy.objects.get(id=complaint_id)
		c.delete()
	
	context = {
	'complaints': complaints,
	}
	return render(request, 'work_study_staff.html', context)

@login_required()
def staff_ppd(request):
	if StudentProfile.objects.filter(user=request.user).exists():
		return redirect('ppd')
	complaints = PPD.objects.all()
	if request.GET.get('id'):
		complaint_id = request.GET.get('id')
		c = PPD.objects.get(id=complaint_id)
		c.delete()
	
	context = {
	'complaints': complaints,
	}
	return render(request, 'PPD_staff.html', context)

@login_required()
def staff_admin_special(request):
	if StudentProfile.objects.filter(user=request.user).exists():
		return redirect('admin_special')
	complaints = SpecialAdmRequest.objects.all()
	if request.GET.get('id'):
		complaint_id = request.GET.get('id')
		c = SpecialAdmRequest.objects.get(id=complaint_id)
		c.delete()
	
	context = {
	'complaints': complaints,
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