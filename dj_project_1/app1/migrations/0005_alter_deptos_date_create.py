# Generated by Django 5.0.6 on 2024-06-28 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_deptos_update_at_mpios_update_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deptos',
            name='date_create',
            field=models.DateTimeField(),
        ),
    ]