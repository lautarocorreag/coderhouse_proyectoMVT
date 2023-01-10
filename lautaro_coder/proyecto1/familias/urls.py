from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_familias, name='lista_familias'),
    path('agregar/', views.agregar_familia, name='agregar_familia'),
    path('editar/<int:id>/', views.editar_familia, name='editar_familia'),
    path('agregar_miembro/<int:id>/', views.agregar_miembro, name='agregar_miembro'),
    path('editar_miembro/<int:id>/', views.editar_miembro, name='editar_miembro'),
    path('ver_familia/<int:id>/', views.ver_familia, name='ver_familia'),
]


