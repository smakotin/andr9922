from django.contrib.gis.db import models


class Point(models.Model):
    coordinate = models.PointField()

    def __str__(self):
        return self.coordinate

