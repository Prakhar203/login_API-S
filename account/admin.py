from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# This code is user to change the superuser django admin face to the line 37 it is useful for changing django admin pannel.
class UserModelAdmin(BaseUserAdmin):
    list_display = ["id","email", "name", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
    (None, {"fields": ["email", "password"]}),
    ("Personal info", {"fields": ["name"]}),
    ("Permissions", {"fields": ["is_admin"]}),
    ]
    add_fieldsets = [
        (
        None,
            {
            "classes": ["wide"],
            "fields": ["email", "name", "password1", "password2"],
            },
        ),
        ]
    search_fields = ["email"]
    ordering = ["email","id"]
    filter_horizontal = []

admin.site.register(User, UserModelAdmin)