from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Hello world!! You will see the website soon. It is under construction.')

def products(request):
    return HttpResponse('Products will be displayed soon.')

