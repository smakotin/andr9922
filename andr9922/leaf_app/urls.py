from django.urls import path

from leaf_app.views import MapPageView, PointListView, add_point

urlpatterns = [
    path('', MapPageView.as_view()),
    path('coordinates/', PointListView.as_view()),
    path('add_point/', add_point, name='add_point'),
]
