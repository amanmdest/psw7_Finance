from django.urls import path
from . import views


app_name = 'contas'
urlpatterns = [
    path('definir_contas/', views.definir_contas, name = 'definir_contas'),
    path('ver_contas/', views.ver_contas, name = 'ver_contas'),
    path('pagar_conta/', views.ver_contas, name = 'pagar_contas'),
]