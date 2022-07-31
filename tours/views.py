from django.http import HttpResponseServerError, HttpResponseNotFound
from django.shortcuts import render
from random import sample
from tours.data import title, subtitle, description, departures, tours


# Create your views here.
def main_view(request):
    random_6_tours = sample(range(1, len(tours)+1), 6)
    suitable_tours = {k: v for k, v in tours.items() if k in random_6_tours}
    return render(request, "tours/index.html", {"title": title, "subtitle": subtitle,"description": description, "suitable_tours": suitable_tours})


def departure_view(request, departure_name):
    suitable_tours = {k: v for k, v in tours.items() if v["departure"] == departure_name}
    min_cost = min(suitable_tours.items(), key=lambda x: x[1].get("price"))[1]['price']
    max_cost = max(suitable_tours.items(), key=lambda x: x[1].get("price"))[1]['price']
    min_nights = min(suitable_tours.items(), key=lambda x: x[1].get("nights"))[1]['nights']
    max_nights = max(suitable_tours.items(), key=lambda x: x[1].get("nights"))[1]['nights']
    tours_count = len(suitable_tours)
    return render(request, "tours/departure.html", {"departure": departures[departure_name],
        "departure_name": departure_name, "min_cost": min_cost, "max_cost": max_cost,
        "tours_count": tours_count, "min_nights": min_nights,
        "max_nights": max_nights, "suitable_tours": suitable_tours})


def tour_view(request, tour_id):
    return render(request, "tours/tour.html", {"tour_info": tours[tour_id],
        "departure": departures[tours[tour_id]["departure"]]})


def custom_handler500(request):
    # Call when PermissionDenied raised
    return HttpResponseServerError('Внутрення ошибка сервера!')


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')
