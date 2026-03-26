from django.shortcuts import redirect, render
from django.utils import timezone

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
        nombre = (request.POST.get("nombre") or "").strip()
        try:
            precio_raw = request.POST.get("precio")
            precio_raw = precio_raw.replace(",", ".") if precio_raw else ""
            precio_val = float(precio_raw)
        except (TypeError, ValueError):
            precio_val = None
        try:
            cantidad = int(request.POST.get("cantidad") or "")
        except (TypeError, ValueError):
            cantidad = None
        descripcion = (request.POST.get("descripcion") or "").strip()
        categoria = (request.POST.get("categoria") or "").strip()

        errores = []
        if not nombre:
            errores.append("El nombre es obligatorio.")
        elif len(nombre) > 25:
            errores.append("El nombre admite como máximo 25 caracteres.")
        if precio_val is None or precio_val < 0:
            errores.append("Indicá un precio válido (número mayor o igual a 0).")
        if cantidad is None or cantidad < 0:
            errores.append("Indicá una cantidad válida (entero mayor o igual a 0).")
        if not descripcion:
            errores.append("La descripción es obligatoria.")
        if not categoria:
            errores.append("La categoría es obligatoria.")

        if errores:
            return render(
                request,
                "AgregarProducto.html",
                {
                    "errores": errores,
                    "nombre": nombre,
                    "precio": request.POST.get("precio") or "",
                    "cantidad": request.POST.get("cantidad") or "",
                    "descripcion": descripcion,
                    "categoria": categoria,
                },
            )

        Producto.objects.create(
            Nombre=nombre,
            Precio=precio_val,
            Cantidad=cantidad,
            Descripcion=descripcion,
            Categoria=categoria,
            fecha_ingreso=timezone.now().date(),
        )
        return redirect("Productos")

    return render(request, "AgregarProducto.html", {})
