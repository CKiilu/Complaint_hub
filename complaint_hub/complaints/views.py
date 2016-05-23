from django.shortcuts import render

from .forms import *
from .models import *

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
	return render(request, 'admin_exeat.html')

def work_study(request):
	return render(request, 'admin_workstudy.html')

def PPD(request):
	return render(request, 'admin_ppd.html')

def admin_special(request):
	return render(request, 'admin_special.html')

# Questions
def faq(request):
	return render(request, 'faq.html')