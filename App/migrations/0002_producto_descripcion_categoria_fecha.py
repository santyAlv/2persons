import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="producto",
            name="Descripcion",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="producto",
            name="Categoria",
            field=models.CharField(default="Sin categoría", max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="producto",
            name="fecha_ingreso",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
