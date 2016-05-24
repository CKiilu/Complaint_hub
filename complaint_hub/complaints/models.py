from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
EXEAT_TYPES = (
	('Home', 'Home'),
	('Other', 'Other'),
	)



class UserType(models.Model):
	"""Types of users"""
	category = models.CharField(max_length=30)

	def __unicode__(self):
		return self.category

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

class Department(models.Model):
	department = models.CharField(max_length=50)
	courses = models.ManyToManyField(Course)

	def __unicode__(self):
		return self.department
		

class UserProfile(models.Model):
	""" User Details """
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE)
	category = models.OneToOneField(
		'UserType',
		on_delete=models.CASCADE)


	def __unicode__(self):
		return str(self.user)

class AcademicComplaint(models.Model):
	""" Academic complaints """
	user = models.ForeignKey(
		'UserProfile',
		on_delete=models.CASCADE)
	matric = models.CharField(max_length=50)
	level = models.CharField(max_length=50)
	department = models.ForeignKey(
		'Department',
		on_delete=models.CASCADE
		)
	program = models.CharField(max_length=50)
	semester = models.CharField(max_length=50)
	session = models.CharField(max_length=50)
	course = models.ForeignKey(
		'Course',
		on_delete=models.CASCADE,)
	request_type = models.ForeignKey(
		'RequestType',
		on_delete=models.CASCADE)
	request = models.TextField(max_length=50)
	course_lecturer = models.CharField(max_length=50)
	timestamp = models.DateTimeField(default=timezone.now())

	def __unicode__(self):
		return str(self.user) + ": " + str(request_type)
		
class Exeat(models.Model):
	user = models.ForeignKey(
		'UserProfile',
		on_delete=models.CASCADE)
	level = models.CharField(max_length=50)
	department = models.ForeignKey(
		'Department',
		on_delete=models.CASCADE
		)
	program = models.CharField(max_length=50)
	exeat_type = models.CharField(max_length=50, choices=EXEAT_TYPES)
	destination = models.CharField(max_length=50)
	application = models.TextField()
	parent_contact = models.CharField(max_length=16)
	timestamp = models.DateTimeField(default=timezone.now())

	def __unicode__(self):
		return str(self.user) + '-' + self.level +": " + self.exeat_type
		
class WorkStudy(models.Model):
	user = models.ForeignKey(
		'UserProfile',
		on_delete=models.CASCADE)
	level = models.CharField(max_length=50)
	department = models.ForeignKey(
		'Department',
		on_delete=models.CASCADE
		)
	program = models.CharField(max_length=50)
	semester = models.CharField(max_length=50)
	session = models.CharField(max_length=50)
	application = models.TextField()
	
	def __unicode__(self):
		return str(self.user) + '-' + self.level 
		
class PPD(models.Model):
	user = models.ForeignKey(
		'UserProfile',
		on_delete=models.CASCADE)
	level = models.CharField(max_length=50)
	hall = models.CharField(max_length=50)
	room = models.CharField(max_length=50)
	site = models.CharField(max_length=50)
	request = models.TextField()
	
	def __unicode__(self):
		return str(self.user) + '-' + self.hall + ", " + self.room + ", " + self.site
		
class SpecialAdmRequest(models.Model):
	user = models.ForeignKey(
		'UserProfile',
		on_delete=models.CASCADE)
	level = models.CharField(max_length=50)
	department = models.ForeignKey(
		'Department',
		on_delete=models.CASCADE
		)
	program = models.CharField(max_length=50)
	hall = models.CharField(max_length=50)
	room = models.CharField(max_length=50)
	request = models.TextField()
	
	def __unicode__(self):
		return str(self.user) 
	