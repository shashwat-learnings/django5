from django.contrib import admin

from uc.models import UnderConstruction

# Register your models here.
@admin.register(UnderConstruction)
class UnderConstructionAdmin(admin.ModelAdmin):
    list_display = ('id','uc_note','is_under_construction', 'uc_duration', 'updated_at')
    fields = ('uc_note','is_under_construction', 'uc_duration')

    list_filter = ('uc_note', 'is_under_construction', 'updated_at')