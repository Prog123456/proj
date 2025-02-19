# Generated by Django 5.0.7 on 2024-07-10 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cities_light", "0011_alter_city_country_alter_city_region_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employees",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("profile_pic", models.FileField(upload_to="")),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("father_name", models.CharField(max_length=30)),
                ("husband_name", models.CharField(max_length=30)),
                ("date_of_birth", models.DateField()),
                ("blood_group", models.CharField(max_length=10)),
                ("employee_id", models.CharField(max_length=12)),
                (
                    "department",
                    models.CharField(
                        choices=[
                            ("CRM", "Customer Relationship Management"),
                            ("E&P", "Editorial and  Publications"),
                            ("R&D", "Research and Development"),
                            ("S&D", "Software and Development"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "designation",
                    models.CharField(
                        choices=[
                            ("Jr.Software Developer", "Junior Software Developer"),
                            ("Jr.Technical Writer", "Junior Technical Writer"),
                            ("BDE", "Business Development Executive"),
                            ("Reasearch Associate", "Research Associate"),
                            ("Assistant Editor", "Assistant Editor"),
                            (
                                "Client Relationship Associate",
                                "Client Relationship Associate",
                            ),
                            ("Research Assistant", "Research Assistant"),
                            ("Executive Assistant", "Executive Assistant"),
                            ("Assistant Team Lead", "Assistant Team Lead"),
                            ("Team Lead", "Team Lead"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("F", "Female"), ("M", "Male")], max_length=50
                    ),
                ),
                (
                    "marital_status",
                    models.CharField(
                        choices=[
                            ("Married", "Married"),
                            ("Unmarried", "Unmarried"),
                            ("Widow", "Widowed"),
                            ("Divorced", "Divorced"),
                        ],
                        max_length=50,
                    ),
                ),
                ("date_of_joining", models.DateField()),
                ("door_no", models.CharField(max_length=10)),
                ("address", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "city",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="cities_light.city",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="cities_light.country",
                    ),
                ),
            ],
        ),
    ]
