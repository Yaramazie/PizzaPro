from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    pizzas = Pizza.objects.all()
    context = {
        'pizzas': pizzas
    }
    return render(request, 'pizzaapp/index.html', context=context)
