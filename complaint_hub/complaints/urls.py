from django.conf.urls import include, url
from django.contrib import admin

from views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^staff/$', staff_home, name='staff_home'),
    url(r'^user_details/$', more_details, name='more_details'),
    url(r'^academic/$', acad, name='acad'),
    url(r'^academic/makeup/$', makeup, name='makeup'),
    url(r'^academic/portal/$', portal, name='portal'),
    url(r'^academic/special/$', special, name='special'),
    url(r'^academic/verify/$', verify, name='verify'),
    url(r'^administrative/$', administrative, name='administrative'),
    url(r'^administrative/exeat/$', exeat, name='exeat'),
    url(r'^administrative/work_study/$', work_study, name='work_study'),
    url(r'^administrative/PPD/$', ppd, name='ppd'),
    url(r'^administrative/special$', admin_special, name='admin_special'),
    url(r'^staff/academic/$', staff_acad, name='staff_acad'),
    url(r'^staff/academic/makeup/$', staff_makeup, name='staff_makeup'),
    url(r'^staff/academic/portal/$', staff_portal, name='staff_portal'),
    url(r'^staff/academic/special/$', staff_special, name='staff_special'),
    url(r'^staff/academic/verify/$', staff_verify, name='staff_verify'),
    url(r'^staff/administrative/$', staff_administrative, name='staff_administrative'),
    url(r'^staff/administrative/exeat/$', staff_exeat, name='staff_exeat'),
    url(r'^staff/administrative/work_study/$', staff_work_study, name='staff_work_study'),
    url(r'^staff/administrative/PPD/$', staff_ppd, name='staff_ppd'),
    url(r'^staff/administrative/special$', staff_admin_special, name='staff_admin_special'),
    url(r'^course_choices/$', get_course_choices, name='get_course_choices'),
    url(r'^program_choices/$', get_program, name='get_program'),
    url(r'^faq/$', faq, name='faq'),
    url(r'^details/$', staff, name='staff'),
]
