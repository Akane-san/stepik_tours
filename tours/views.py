from django.http import HttpResponseServerError, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.
def main_view(request):
    return render(request, "tours/index.html")


def departure_view(request, id):
    return render(request, "tours/departure.html")


def tour_view(request, id):
    return render(request, "tours/tour.html")


def custom_handler500(request):
    # Call when PermissionDenied raised
    return HttpResponseServerError('Внутрення ошибка сервера!')


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')
