from django.urls import path

from leaf_app.views import MapPageView, PointListView

urlpatterns = [
    path('', MapPageView.as_view()),
    path('coordinates/', PointListView.as_view()),
]
