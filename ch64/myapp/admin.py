from django.contrib import admin
from .models import Profile, Page, Like

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'city')
    search_fields = ('user__username', 'name', 'city')
    list_filter = ('name', 'city')

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'page_name')
    search_fields = ('profile_name', 'page_name')
    list_filter = ('page_name',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'page_name',)