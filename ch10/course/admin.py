from django.contrib import admin
from  course.models import Profile


# to show model row in admin interface

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'city','roll', 'state')  # specify fields to display in admin list view

# Register your models here.
#  to show Profile model in admin interface
admin.site.register(Profile, ProfileAdmin)

#instead of admin.site.register(Profile)
# we can also use decorator as below    
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id','name', 'email', 'city','roll', 'state')  # specify fields to display in admin list view
