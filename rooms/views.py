# from math import ceil
# from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect
from django.http import Http404
from django_countries import countries

# from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView
from . import models, forms


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    try:
        model = models.Room
    except models.Room.DoesNotExist:
        raise Http404()


def search(request):

    form = forms.SearchForm()

    return render(request, "rooms/search.html", {"form": form})
