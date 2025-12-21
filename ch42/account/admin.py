from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User

# Register your models here.

class UserModelAdmin(UserAdmin):
    model = User
    #  The fields to be used in displaying the user model
    #  These override the definitions on the base UserModelAdmin
    #  that reference specific fields on auth.user
    list_display = ["id","email","name","is_active","is_superuser","is_staff","is_customer","is_seller"]
    list_filter = ["is_superuser"]
    fieldsets = [("User Credentials", {"fields":["email","password"]}),
                 ("Personal Informations",{"fields":["name","city"]}),
                 ("Permissions",{"fields":["is_active","is_staff","is_superuser","is_customer","is_seller","groups","user_permissions"]})
                 ]
    
    # add_fieldsets is not a standard ModalAdmin attribute.
    # UserModelAdmin
    # override get_fieldsets to user this attribute when creating a user
    # add_fieldsets is list of tuples. Each tuple represents a section in the Add User Form

    add_fieldsets = [
        (
            # it is the title of the section. setting this to
            #  None leave the section title blank
            None,
            {
                # it's a css class to make full width admin layout
                "classes":["wide"],
                # This field will appear in admin panel add user form
                "fields":["email","password1","password2"]
            }
        )
    ]

    search_fields = ["email"]
    ordering = ["email","id"]
    filter_horizontal = ["groups","user_permissions"]

admin.site.register(User,UserModelAdmin)