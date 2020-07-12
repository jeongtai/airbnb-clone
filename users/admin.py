from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as rooms_models

# Register your models here.

# admin.site.register(models.User, CustomUserAdmin)
# 위랑 아래랑 같은 뜻임. admin 패널에서 이 user를 볼 거다.


class RoomInline(admin.TabularInline):

    model = rooms_models.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    inlines = (RoomInline,)

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

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )

