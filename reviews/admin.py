from django.contrib import admin
from . import models


@admin.register(models.Review)
class RevieAdmin(admin.ModelAdmin):

    """ Review Admin Definition """

    # 리뷰 평점 구하는 메소드-보류
    list_display = ("__str__", "rating_average")

