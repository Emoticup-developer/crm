# Generated by Django 5.0.7 on 2025-01-22 07:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0018_alter_client_account_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="status",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
