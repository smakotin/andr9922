from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.gis.geos import Point as P

from leaf_app.models import Point


class MapPageView(TemplateView):
    template_name = 'leaf_app/map_page.html'


class PointListView(ListView):
    model = Point
    template_name = 'leaf_app/point_list.html'
    context_object_name = 'points'


def add_point(request):
    if request.method == "POST":
        title = request.POST.get('title')
        lat = float(request.POST.get('lat'))
        lng = float(request.POST.get('lng'))
        point_object = P(lat, lng)

        point = Point(title=title, coordinate=point_object)
        point.save()

        return render(request, 'leaf_app/map_page.html')
    return render(request, 'leaf_app/map_page.html')