# Generated by Django 5.0.7 on 2025-01-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0009_alter_product_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machine",
            name="status",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
