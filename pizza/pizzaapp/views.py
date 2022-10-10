from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout
from .models import *
from django.contrib import messages


class AllPizzas(ListView):
    model = Pizza
    template_name = 'pizzaapp/index.html'
    context_object_name = 'pizza_list'


class ByCategory(ListView):
    model = Pizza
    template_name = 'pizzaapp/index.html'
    context_object_name = 'pizza_list'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ByCategory, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Pizza.objects.filter(category__slug=self.kwargs['slug'])


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'pizzaapp/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Пользователь успешно создан')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'pizzaapp/register.html', {'form': form})


class PizzaDetail(DetailView):
    model = Pizza
    template_name = 'pizzaapp/get_pizza.html'
    context_object_name = 'pizza'
