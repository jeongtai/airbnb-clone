from django.contrib import admin
from . import models

# Register your models here.

# admin.site.register(models.User, CustomUserAdmin)
# 위랑 아래랑 같은 뜻임. admin 패널에서 이 user를 볼 거다.


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = (
        "language",
        "currency",
        "superhost",
    )
