from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
EXEAT_TYPES = (
	('1', 'Home'),
	('2', 'Other'),
	)

SEMESTERS = (
	('1', 'First Semester'),
	('2', 'Second Semester')
	)

LEVELS = (
	('1', 'First Year'),
	('2', 'Second Year'),
	('3', 'Third Year'),
	('4', 'Fourth Year'),
	('5', 'Fifth Year')
	)

class RequestType(models.Model):
	"""Types of requests"""
	request_type = models.CharField(max_length=30)

	def __unicode__(self):
		return self.request_type

class Course(models.Model):
	"""Types of users"""
	courses = models.CharField(max_length=60)

	def __unicode__(self):
		return self.courses

class Program(models.Model):
	"""Types of users"""
	program = models.CharField(max_length=60)
	courses = models.ManyToManyField(Course)

	def __unicode__(self):
		return self.program

class Department(models.Model):
	department = models.CharField(max_length=50)
	programs = models.ManyToManyField(Program)

	def __unicode__(self):
		return self.department
		

class StudentProfile(models.Model):
	""" User Details """
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE)
	matric = models.CharField(max_length=10)
	full_name = models.CharField(max_length=50)
	level = models.CharField(max_length=50, choices=LEVELS)
	program = models.ForeignKey(
		'Program',
		on_delete=models.CASCADE)


	def __unicode__(self):
		return str(self.user)
		

class StaffProfile(models.Model):
	""" User Details """
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE)
	full_name = models.CharField(max_length=50, unique=True)
	
	def __unicode__(self):
		return str(self.full_name)
class AcademicComplaint(models.Model):
	""" Academic complaints """
	user = models.ForeignKey(
		'StudentProfile',
		on_delete=models.CASCADE)
	level = models.CharField(max_length=50, choices=LEVELS)
	department = models.ForeignKey(
		'Department',
		on_delete=models.CASCADE
		)
	semester = models.CharField(max_length=50, choices=SEMESTERS)
	session = models.CharField(max_length=50)
	program = models.ForeignKey(
		'Program',
		on_delete=models.CASCADE,
		null=True)
	course = models.CharField(max_length=50)
	request_type = models.ForeignKey(
		'RequestType',
		on_delete=models.CASCADE)
	request = models.TextField(max_length=50)
	course_lecturer = models.ForeignKey(
		'StaffProfile',
		on_delete=models.CASCADE,
		to_field='full_name'
		)
	timestamp = models.DateTimeField(default=timezone.now())

	def __unicode__(self):
		return str(self.user) + ": " + str(request_type)
		
class Exeat(models.Model):
	user = models.ForeignKey(
		'StudentProfile',
		on_delete=models.CASCADE)
	level = models.CharField(max_length=50, choices=LEVELS)
	department = models.ForeignKey(
		'Department',
		on_delete=models.CASCADE
		)
	exeat_type = models.CharField(max_length=50, choices=EXEAT_TYPES)
	destination = models.CharField(max_length=50)
	application = models.TextField()
	parent_contact = models.CharField(max_length=16)
	timestamp = models.DateTimeField(default=timezone.now())

	def __unicode__(self):
		return str(self.user) + '-' + self.level +": " + self.exeat_type
		
class WorkStudy(models.Model):
	user = models.ForeignKey(
		'StudentProfile',
		on_delete=models.CASCADE)
	level = models.CharField(max_length=50, choices=LEVELS)
	department = models.ForeignKey(
		'Department',
		on_delete=models.CASCADE
		)
	semester = models.CharField(max_length=50, choices=SEMESTERS)
	session = models.CharField(max_length=50)
	application = models.TextField()
	timestamp = models.DateTimeField(default=timezone.now())
	
	def __unicode__(self):
		return str(self.user) + '-' + self.level 
		
class PPD(models.Model):
	user = models.ForeignKey(
		'StudentProfile',
		on_delete=models.CASCADE)
	level = models.CharField(max_length=50, choices=LEVELS)
	hall = models.CharField(max_length=50)
	room = models.CharField(max_length=50)
	site = models.CharField(max_length=50)
	request = models.TextField()
	timestamp = models.DateTimeField(default=timezone.now())
	
	def __unicode__(self):
		return str(self.user) + '-' + self.hall + ", " + self.room + ", " + self.site
		
class SpecialAdmRequest(models.Model):
	user = models.ForeignKey(
		'StudentProfile',
		on_delete=models.CASCADE)
	level = models.CharField(max_length=50, choices=LEVELS)
	department = models.ForeignKey(
		'Department',
		on_delete=models.CASCADE
		)
	hall = models.CharField(max_length=50)
	room = models.CharField(max_length=50)
	request = models.TextField()
	timestamp = models.DateTimeField(default=timezone.now())
	
	def __unicode__(self):
		return str(self.user) 
	