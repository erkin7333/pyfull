from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):

    model = User

    list_display = (
        "id", "username", "email", "phone",
        "group_name", "is_staff", "is_active"
    )

    fieldsets = UserAdmin.fieldsets + (
        ("Extra info", {
            "fields": (
                "phone",
                "group_name",
                "address",
                "birth_date",
                "image",
            )
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Extra info", {
            "fields": (
                "phone",
                "group_name",
                "address",
                "birth_date",
                "image",
            )
        }),
    )

admin.site.register(User, CustomUserAdmin)