from django.contrib import admin
from leaf_app.models import Point


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ['id', 'coordinate']


