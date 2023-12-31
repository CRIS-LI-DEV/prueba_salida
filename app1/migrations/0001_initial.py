# Generated by Django 4.2.3 on 2023-07-11 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_total', models.IntegerField(null=True)),
                ('precio_total', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FormaDePago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ImagenesAuxiliares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('imagen_b', models.BinaryField(null=True)),
                ('imagen_f', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=200, null=True)),
                ('direccion', models.CharField(max_length=200, null=True)),
                ('rut', models.CharField(max_length=200, null=True)),
                ('imagen_b', models.BinaryField(null=True)),
                ('imagen_f', models.ImageField(null=True, upload_to='images/')),
                ('comuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.comuna')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.region')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('permiso_staff', 'puede acceder a las intefaces del staff')],
            },
        ),
        migrations.CreateModel(
            name='Productor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=200, null=True)),
                ('direccion', models.CharField(max_length=200, null=True)),
                ('rut', models.CharField(max_length=100)),
                ('razon_social', models.CharField(max_length=200, null=True)),
                ('imagen_b', models.BinaryField(null=True)),
                ('imagen_f', models.ImageField(null=True, upload_to='images/')),
                ('nombre_contacto', models.CharField(max_length=200, null=True)),
                ('comuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.comuna')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.region')),
                ('rubro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.rubro')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('permiso_proveedor', 'puede acceder a las intefaces del proveedor')],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=255, null=True)),
                ('precio', models.IntegerField(null=True)),
                ('stock', models.IntegerField(null=True)),
                ('imagen_b', models.BinaryField(null=True)),
                ('imagen_f', models.ImageField(null=True, upload_to='images/')),
                ('productor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.productor')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True)),
                ('calle_entrega', models.CharField(max_length=200, null=True)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.carrito')),
                ('comuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.comuna')),
                ('estado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.estadopedido')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.region')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleProductoSocilicitado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_producto', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=200, null=True)),
                ('telefono', models.CharField(max_length=200, null=True)),
                ('rut', models.CharField(max_length=200, null=True)),
                ('direccion', models.CharField(max_length=200, null=True)),
                ('imagen_b', models.BinaryField()),
                ('imagen_f', models.ImageField(upload_to='images/')),
                ('comuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.comuna')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.region')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('permiso_cliente', 'puede acceder a las intefaces del cliente')],
            },
        ),
        migrations.AddField(
            model_name='carrito',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.cliente'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='empleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.usuariostaff'),
        ),
    ]
