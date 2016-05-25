from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(RequestType)
admin.site.register(StaffProfile)
admin.site.register(StudentProfile)
admin.site.register(AcademicComplaint)
admin.site.register(PPD)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Exeat)
admin.site.register(SpecialAdmRequest)
admin.site.register(WorkStudy)