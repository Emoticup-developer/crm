# Generated by Django 5.0.7 on 2025-01-17 07:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_localization_ordersource_ticketpriority_ticketsource_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="localization",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]