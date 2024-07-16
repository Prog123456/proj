# Generated by Django 5.0.7 on 2024-07-10 07:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
        ("cities_light", "0011_alter_city_country_alter_city_region_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employees",
            name="city",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="cities_light.region",
            ),
        ),
    ]
