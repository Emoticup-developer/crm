# Generated by Django 5.0.7 on 2025-01-16 08:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_company"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="admin",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.client",
            ),
        ),
        migrations.AddField(
            model_name="client",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.company",
            ),
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                ("map_link", models.CharField(blank=True, max_length=2000, null=True)),
                (
                    "address_line_1",
                    models.CharField(blank=True, max_length=750, null=True),
                ),
                (
                    "address_line_2",
                    models.CharField(blank=True, max_length=750, null=True),
                ),
                ("city", models.CharField(blank=True, max_length=50, null=True)),
                ("state", models.CharField(blank=True, max_length=50, null=True)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("pincode", models.CharField(blank=True, max_length=6, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("Active", "Active"), ("Closed", "Closed")],
                        default="Active",
                        max_length=10,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="locations",
                        to="api.company",
                    ),
                ),
            ],
            options={
                "verbose_name": "Location",
                "verbose_name_plural": "Locations",
            },
        ),
    ]