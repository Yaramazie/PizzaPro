from django.urls import path
from .views import *

urlpatterns = [
    path('', AllPizzas.as_view(), name='home'),
    path('pizza/<str:slug>/', PizzaDetail.as_view(), name='get_pizza'),
    path('category/<str:slug>/', ByCategory.as_view(), name='get_category'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
