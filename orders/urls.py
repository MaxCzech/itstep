from django.urls import path, re_path
from .views import order_create

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
]
