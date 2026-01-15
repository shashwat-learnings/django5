from django.contrib import admin

from school.models import Student, Teacher

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'roll', 'city', 'marks', 'pass_date')
    search_fields = ('name', 'roll', 'city')
    list_filter = ('city', 'pass_date')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'empnum', 'city', 'salary', 'join_date')
    search_fields = ('name', 'empnum', 'city')
    list_filter = ('city', 'join_date')