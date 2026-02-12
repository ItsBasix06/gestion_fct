from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.probar_base, name='probar_base'),
    path('quienes-somos/', views.about, name='about'),
    path('registro/', views.registro, name='registro'),
]