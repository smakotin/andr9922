from django.urls import path

from leaf_app.views import test_page

urlpatterns = [
    path('', test_page)
]
