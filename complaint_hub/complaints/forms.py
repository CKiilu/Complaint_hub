from django import forms

from .models import *

SEMESTERS = (
	('1', 'First Semester'),
	('2', 'Second Semester'),
	('3', 'Third Semester')
	)

LEVELS = (
	('1', 'First Year'),
	('2', 'Second Year'),
	('3', 'Third Year'),
	('4', 'Fourth Year')
	)


class AcademicComplaintForm(forms.ModelForm):
	class Meta:
		model = AcademicComplaint
		fields = [
		'matric',
		'level',
		'department',
		'program',
		'semester',
		'session',
		'course',
		'request',
		'course_lecturer',]
		widgets = {
		'matric': forms.TextInput(attrs={
			'class': 'columns'
			}),
		'level': forms.Select(attrs={
			'class': 'columns'
			},
			choices=LEVELS
			),
		'semester': forms.Select(attrs={
			'class': 'columns'
			},
			choices=SEMESTERS
			),
		'course': forms.Select(attrs={
			'class': 'columns'
			}),
		'session': forms.TextInput(attrs={
			'class': 'columns'
			}),
		'request_type': forms.Select(attrs={
			'class': 'columns'
			}),
		}