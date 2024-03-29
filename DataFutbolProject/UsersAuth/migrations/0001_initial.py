# Generated by Django 4.2.1 on 2023-05-16 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('equipo_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnicos',
            fields=[
                ('tecnico_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.DateField()),
                ('nacionalidad', models.CharField(max_length=50)),
                ('equipo_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='UsersAuth.equipos')),
            ],
        ),
        migrations.CreateModel(
            name='Jugadores',
            fields=[
                ('jugador_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('posicion', models.CharField(max_length=3)),
                ('edad', models.DateField()),
                ('altura', models.CharField(max_length=5)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('equipo_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='UsersAuth.equipos')),
            ],
        ),
    ]
