# Generated by Django 5.0.7 on 2025-01-28 07:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_alter_machine_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="associated_employee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="associated_employee",
                to="api.client",
            ),
        ),
    ]
