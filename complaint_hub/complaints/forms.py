from django import forms

from .models import *

class AcademicComplaintForm(forms.ModelForm):
	class Meta:
		model = AcademicComplaint
		exclude = [
			'user',
			'timestamp']
		widgets = {
			'course': forms.Select()
		}
		
class ExeatForm(forms.ModelForm):
	class Meta:
		model = Exeat
		exclude = [
			'user',
			'timestamp']

class PPDForm(forms.ModelForm):
	class Meta:
		model = PPD
		exclude = [
			'user',
			'timestamp']
		
class SpecialAdmRequestForm(forms.ModelForm):
	class Meta:
		model = SpecialAdmRequest
		exclude = [
			'user',
			'timestamp']
		
class WorkStudyForm(forms.ModelForm):
	class Meta:
		model = WorkStudy
		exclude = [
			'user',
			'timestamp']
			
class StaffProfileForm(forms.ModelForm):
	class Meta:
		model = StaffProfile
		exclude = [
			'user']
			
class StudentProfileForm(forms.ModelForm):
	class Meta:
		model = StudentProfile
		exclude = [
			'user']