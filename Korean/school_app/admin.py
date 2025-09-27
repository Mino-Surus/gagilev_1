from django.contrib import admin
from .models import *

admin.site.register(student)
admin.site.register(lessons)
admin.site.register(teacher)
admin.site.register(enrollments)
admin.site.register(course)