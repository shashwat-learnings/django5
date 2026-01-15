from django.contrib import admin

from school.models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'roll', 'city', 'marks', 'pass_date')
    search_fields = ('name', 'roll', 'city')
    list_filter = ('city', 'pass_date')

