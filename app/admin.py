from django.contrib import admin
from .models import CustomUser, Officer, Teacher, Student, Subject

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Officer)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
