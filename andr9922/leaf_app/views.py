from django.shortcuts import render
from django.views.generic import TemplateView


class MapPageView(TemplateView):
    template_name = 'map_page.html'
