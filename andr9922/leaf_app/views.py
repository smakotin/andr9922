from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from leaf_app.models import Point


class MapPageView(TemplateView):
    template_name = 'leaf_app/map_page.html'


class PointListView(ListView):
    model = Point
    template_name = 'leaf_app/point_list.html'
    context_object_name = 'points'

