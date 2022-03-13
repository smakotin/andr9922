from django.http import HttpResponse
from django.shortcuts import render


def test_page(request):
    return HttpResponse('Hello from fiiiiiirst page')
