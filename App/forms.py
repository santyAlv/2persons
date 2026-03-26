from django import forms
from django.utils import timezone

from .models import Producto


class FormularioProductos(forms.ModelForm):
  
    fecha_ingreso = forms.DateField(required=False, widget=forms.HiddenInput())
 
    Precio = forms.CharField(max_length=32)

    class Meta:
        model = Producto
        fields = [
            "Nombre",
            "Cantidad",
            "Precio",
            "Descripcion",
            "Categoria",
            "fecha_ingreso",
        ]
        widgets = {
            "Nombre": forms.TextInput(
                attrs={"maxlength": "25", "placeholder": "Nombre del producto"}
            ),
            "Cantidad": forms.NumberInput(attrs={"min": "0", "step": "1"}),
         
            "Precio": forms.TextInput(
                attrs={"placeholder": "Precio", "inputmode": "decimal", "maxlength": "32"}
            ),
            "Descripcion": forms.Textarea(attrs={"rows": 4}),
            "Categoria": forms.TextInput(
                attrs={"maxlength": "80", "placeholder": "Categoría"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.initial.get("fecha_ingreso"):
            self.initial["fecha_ingreso"] = timezone.now().date()

    def clean_Precio(self):
        precio = self.cleaned_data.get("Precio")
        
        if precio is None:
            return precio
        if isinstance(precio, str):
            precio = precio.strip().replace(",", ".")
        precio_val = float(precio)
        if precio_val < 0:
            raise forms.ValidationError("El precio debe ser mayor o igual a 0.")
        return precio_val

