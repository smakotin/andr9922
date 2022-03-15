from django.contrib.gis.db import models as gis_models
from django.db import models


class Point(gis_models.Model):
    title = models.CharField(max_length=500, blank=True)
    coordinate = gis_models.PointField()

    def __str__(self):
        return self.title
