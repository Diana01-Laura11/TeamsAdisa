# Generated by Django 4.2.1 on 2023-05-18 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appteams', '0003_alter_cedulas_fecha_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
