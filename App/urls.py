from django.urls import path

from .views import *

urlpatterns = [
    path("", Home, name="Inicio"),
    path("Productos", Productos, name="Productos"),
    path("AgregarProductos", AgregarProducto, name="AgregarProducto"),
]
