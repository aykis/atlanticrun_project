from django.urls import path

from . import views


urlpatterns = [
    path(r'', views.inscription, name='inscription'),
    path('cancel/', views.CancelView, name='cancel'),
    path('success/', views.SuccessView, name='success'),
    path('create-checkout-session/<pk>/', views.paiement, name='create-checkout-session')
]