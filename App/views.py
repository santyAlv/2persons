from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import FormularioProductos
from .models import *


def Home(request):
    total = Producto.objects.count()
    return render(
        request,
        "Home.html",
        {"total_productos": total},
    )


def Productos(request):
    Villalva = Producto.objects.all().order_by("-fecha_ingreso", "-Codigo")
    data = {"tabla": Villalva}
    return render(request, "Productos.html", data)


def AgregarProducto(request):
    if request.method == "POST":
        form = FormularioProductos(request.POST, request.FILES)
        if form.is_valid():
           
            form.instance.fecha_ingreso = timezone.now().date()
            form.save()
            return redirect("Productos")
    else:
        form = FormularioProductos()

    return render(request, "AgregarProducto.html", {"form": form})
