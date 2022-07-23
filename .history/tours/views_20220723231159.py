from django.shortcuts import render

# Create your views here.
def main_view(request):
    authors = Author.objects.all()
    context = {
        "authors": authors
    }
    return render(request, "index.html", context=context)


def departure_view(request, id):
    return render(request, "departure.html")

def tour_view(request, id):
    return render(request, "tour.html")
