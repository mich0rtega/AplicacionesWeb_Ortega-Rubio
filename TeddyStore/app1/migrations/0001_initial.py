# Generated by Django 5.1.2 on 2024-10-28 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('cod_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=40)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('usuario', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=8)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField(max_length=10)),
            ],
        ),
    ]
