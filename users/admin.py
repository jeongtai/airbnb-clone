from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.

# admin.site.register(models.User, CustomUserAdmin)
# 위랑 아래랑 같은 뜻임. admin 패널에서 이 user를 볼 거다.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
