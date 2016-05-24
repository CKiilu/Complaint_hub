from django.conf.urls import include, url
from django.contrib import admin

from views import *

urlpatterns = [
    url(r'^$', home, name='home'),
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
    url(r'^course_choices/$', get_course_choices, name='get_course_choices'),
    url(r'^program_choices/$', get_program, name='get_program'),
    url(r'^faq/$', faq, name='faq'),
]
