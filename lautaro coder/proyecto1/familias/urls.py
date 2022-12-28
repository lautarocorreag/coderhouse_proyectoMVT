from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_familias, name='lista_familias'),
    path('agregar/', views.agregar_familia, name='agregar_familia'),
    path('editar/<int:id>/', views.editar_familia, name='editar_familia'),
]
