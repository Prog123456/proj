# Generated by Django 5.0.7 on 2024-07-17 04:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_rename_city_employees_state"),
        ("cities_light", "0011_alter_city_country_alter_city_region_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="employees",
            name="district",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="cities_light.city",
            ),
        ),
    ]
