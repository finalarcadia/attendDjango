from django.contrib import admin
from .models import Class, Attendance, UniversityDim

# Register your models here.
admin.site.register(Class)
admin.site.register(Attendance)
admin.site.register(UniversityDim)
