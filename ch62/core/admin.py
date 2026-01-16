from django.contrib import admin
from .models import Student, Teacher, Contractor, ExamCenter, Candidate, Proudct, DiscountedProduct

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll', 'age', 'fees', 'created_at', 'updated_at')
    search_fields = ('name', 'roll')
    list_filter = ('age',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'salary', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('age',)

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'payment', 'join_date', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('age',)

@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'center_name', 'center_city')
    search_fields = ('center_name', 'center_city')  

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'center_name', 'center_city')
    search_fields = ('name', 'roll', 'center_name')
    list_filter = ('center_city',)

@admin.register(Proudct)
class ProudctAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('price',)

@admin.register(DiscountedProduct)
class DiscountedProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('price',)