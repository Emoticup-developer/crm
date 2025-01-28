# Generated by Django 5.0.7 on 2025-01-28 06:00

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Authorize",
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
                ("key", models.TextField(unique=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("request", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Company",
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
                ("company_name", models.CharField(max_length=150, unique=True)),
                ("brand_name", models.CharField(max_length=150)),
                ("company_phone", models.CharField(max_length=30)),
                ("website", models.URLField(max_length=150)),
                ("company_email", models.EmailField(max_length=254)),
                ("company_mobile_no", models.CharField(max_length=10)),
                ("gstin", models.CharField(max_length=15)),
                ("pan_number", models.CharField(max_length=10)),
                ("comm_address", models.CharField(max_length=250)),
                ("location", models.CharField(max_length=50)),
                ("country", models.CharField(max_length=100)),
                ("pincode", models.CharField(max_length=6)),
                ("state", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=50)),
                ("reg_address", models.CharField(max_length=750)),
                ("contact_person_name", models.CharField(max_length=100)),
                ("contact_person_mobile", models.CharField(max_length=10)),
                (
                    "brand_logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="company/logos/"
                    ),
                ),
                (
                    "brand_icon",
                    models.ImageField(
                        blank=True, null=True, upload_to="company/icons/"
                    ),
                ),
                ("enrollment_date", models.DateField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("trash", models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Country",
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
                ("country", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Localization",
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
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="item_images/"),
                ),
                ("status", models.BooleanField(default=False, max_length=10)),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Machine",
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
                ("machine_id", models.CharField(max_length=30, unique=True)),
                ("machine_name", models.CharField(max_length=150)),
                (
                    "photo",
                    models.ImageField(
                        upload_to="machine_photos/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["jpg", "jpeg", "png"]
                            )
                        ],
                    ),
                ),
                ("status", models.BooleanField(blank=True, default=False, null=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("trash", models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                "verbose_name": "Machine",
                "verbose_name_plural": "Machines",
            },
        ),
        migrations.CreateModel(
            name="OrderSource",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="OrderStatus",
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
                ("status", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("product_code", models.CharField(max_length=30, unique=True)),
                ("product_title", models.CharField(max_length=150)),
                ("moq", models.PositiveIntegerField(default=1)),
                ("photo", models.ImageField(upload_to="products/")),
                ("description", models.TextField(max_length=2000)),
                ("status", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("trash", models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
        migrations.CreateModel(
            name="SideBarIcon",
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
                ("title", models.TextField()),
                ("icon", models.ImageField(upload_to="icon/")),
                ("date", models.DateTimeField(auto_now=True)),
                ("link", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="TicketPriority",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="TicketSource",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="TicketStatus",
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
                ("status", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="TicketType",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="TopBarIcon",
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
                ("title", models.TextField()),
                ("icon", models.ImageField(upload_to="icon/")),
                ("date", models.DateTimeField(auto_now=True)),
                ("link", models.URLField()),
            ],
        ),
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
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="client",
            name="trash",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="client",
            name="account_id",
            field=models.CharField(
                auto_created=True, default=uuid.uuid4, max_length=30, unique=True
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
                ("title", models.CharField(max_length=100)),
                ("map_link", models.CharField(max_length=2000)),
                ("address_line_1", models.CharField(max_length=750)),
                ("address_line_2", models.CharField(max_length=750)),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("country", models.CharField(max_length=100)),
                ("pincode", models.CharField(max_length=6)),
                ("status", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("trash", models.BooleanField(blank=True, default=False, null=True)),
                (
                    "company",
                    models.ForeignKey(
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
        migrations.CreateModel(
            name="CompanyMachineTable",
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
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.company"
                    ),
                ),
                (
                    "used_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.client"
                    ),
                ),
                (
                    "machine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.machine"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="machine_attributes",
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
                ("title", models.TextField()),
                ("value", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "associated",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.machine"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                (
                    "order_id",
                    models.CharField(
                        default=uuid.uuid4, editable=False, max_length=36, unique=True
                    ),
                ),
                ("order_date", models.DateField(auto_now=True)),
                ("po_number", models.CharField(max_length=100)),
                ("dc_number", models.CharField(max_length=100)),
                ("additional_note", models.TextField(blank=True)),
                ("email_sms_notification", models.BooleanField(default=True)),
                (
                    "dc_copy",
                    models.FileField(blank=True, null=True, upload_to="dc_copy"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("on_hold", models.BooleanField(blank=True, default=False, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("trash", models.BooleanField(blank=True, default=False, null=True)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.client"
                    ),
                ),
                (
                    "handled_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="handle",
                        to="api.client",
                    ),
                ),
                (
                    "machine",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.machine",
                    ),
                ),
                (
                    "office_delivery",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.company",
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.ordersource",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.orderstatus",
                    ),
                ),
                (
                    "products",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="api.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Order",
                "verbose_name_plural": "Orders",
            },
        ),
        migrations.CreateModel(
            name="OrderDocs",
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
                ("title", models.TextField()),
                ("file", models.FileField(upload_to="docs/")),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "associated",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.order"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rating",
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
                (
                    "rating",
                    models.PositiveIntegerField(
                        choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
                        verbose_name="Rating (1-5)",
                    ),
                ),
                (
                    "comments",
                    models.TextField(blank=True, null=True, verbose_name="Comments"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("trash", models.BooleanField(blank=True, default=False, null=True)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ratings",
                        to="api.client",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="State",
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
                ("state", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.country"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
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
                (
                    "ticket_id",
                    models.CharField(
                        default=uuid.uuid1, editable=False, max_length=30, unique=True
                    ),
                ),
                ("email_sms_notification", models.BooleanField(default=True)),
                ("subject", models.CharField(max_length=250)),
                ("additional_information", models.TextField()),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="ticket_photos/"
                    ),
                ),
                (
                    "video",
                    models.FileField(blank=True, null=True, upload_to="ticket_videos/"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("resolution_status", models.BooleanField(default=False)),
                ("root_cause", models.TextField(null=True)),
                ("observation", models.TextField(null=True)),
                ("trash", models.BooleanField(blank=True, default=False, null=True)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="raised",
                        to="api.client",
                    ),
                ),
                (
                    "handled_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="handle_emp",
                        to="api.client",
                    ),
                ),
                (
                    "machine",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.machine",
                    ),
                ),
                (
                    "office",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.company",
                    ),
                ),
                (
                    "priority",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.ticketpriority",
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.ticketsource",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.ticketstatus",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.tickettype"
                    ),
                ),
            ],
            options={
                "verbose_name": "Ticket",
                "verbose_name_plural": "Tickets",
            },
        ),
        migrations.CreateModel(
            name="TicketDocs",
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
                ("title", models.TextField()),
                ("file", models.FileField(upload_to="docs/")),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "associated",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.ticket"
                    ),
                ),
            ],
        ),
    ]
