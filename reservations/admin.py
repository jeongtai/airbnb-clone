from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Model Definition """

    pass

