# from math import ceil
# from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect
from django.http import Http404
from django_countries import countries

# from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     now = timezone.now()
    #     return context


"""
함수로 표현한 View -> core.urls.py 에 
urlpatterns = [path("", room_views.all_rooms, name="home")]
로 수정
def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        rooms = paginator.page(1)
        return redirect("/")
"""
"""
위와 같은 의미의 함수
def all_rooms(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)
    return render(
        request,
        "rooms/home.html",
        {
            "potato": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count),
        },
    )
"""


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    try:
        model = models.Room
    except models.Room.DoesNotExist:
        raise Http404()


"""
def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()
"""


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    room_types = models.RoomType.objects.all()
    return render(
        request,
        "rooms/search.html",
        {"city": city, "countries": countries, "room_types": room_types},
    )
