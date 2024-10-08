# Generated by Django 5.1 on 2024-08-31 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaUab',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_Uab', models.CharField(choices=[('MA_UAB_ReservaForetsalProtectoraProductora', 'RFPP'), ('MA_UAB_ReservaLey2da', 'Reserva ley 2da'), ('MA_UAB_ReservaForestalProtectoraNacional', 'RFPN'), ('MA_UAB_SustraccionLey2da', 'Sustraccion ley 2da')])),
                ('nom_ley2', models.CharField()),
                ('res_zoni', models.CharField()),
                ('acto_admin', models.CharField()),
                ('fecha_acto', models.CharField()),
                ('fecha_ingreso', models.DateTimeField()),
                ('fecha_recoleccion', models.DateTimeField()),
            ],
        ),
    ]
