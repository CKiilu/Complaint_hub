from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(UserType)
admin.site.register(RequestType)
admin.site.register(UserProfile)
admin.site.register(AcademicComplaint)
admin.site.register(PPD)
admin.site.register(Exeat)
admin.site.register(SpecialAdmRequest)
admin.site.register(WorkStudy)