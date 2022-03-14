from django.urls import path

from leaf_app.views import MapPageView

urlpatterns = [
    path('', MapPageView.as_view())
]
