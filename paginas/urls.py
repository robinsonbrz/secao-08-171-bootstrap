from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pagina_inicial'),
    path('sobre/', views.sobre, name='sobre'),
]