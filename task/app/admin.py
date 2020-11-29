from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User,Student,Teacher,Subjects


class UserAdmin(UserAdmin):
    list_display = ['id','username','password','role']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','student_name']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','teacher_name','student']


class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['id','subject_name','teacher']


admin.site.register(User,UserAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Subjects,SubjectsAdmin)

