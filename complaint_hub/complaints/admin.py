from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(UserType)
admin.site.register(RequestType)
admin.site.register(UserProfile)
admin.site.register(AcademicComplaint)