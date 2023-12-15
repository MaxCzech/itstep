from django.urls import path
from . import views

urlpatterns = [
    path('shipping/', views.shipping, name="shipping"),
    path('gdrp/', views.gdrp, name="gdrp"),
    path('support/', views.support, name="support"),
    path('terms/', views.terms, name="terms"),
    path('payment_options/', views.payment_options, name="payment_options"),
]
