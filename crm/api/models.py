from django.db import models
from django.core.validators import (
    EmailValidator,
    RegexValidator,
    MaxLengthValidator,
    MinLengthValidator,
    FileExtensionValidator,
)
import uuid


class OrderStatus(models.Model):
    status = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.status)


class TicketStatus(models.Model):
    status = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.status)


class Company(models.Model):
    company_name = models.CharField(max_length=150, unique=True)
    brand_name = models.CharField(max_length=150, null=False, blank=False)
    company_phone = models.CharField(max_length=30, blank=False, null=False)
    website = models.URLField(max_length=150, null=False, blank=False)
    company_email = models.EmailField(blank=False, null=False)
    company_mobile_no = models.CharField(max_length=10, blank=False, null=False)
    gstin = models.CharField(max_length=15, blank=False, null=False)
    pan_number = models.CharField(max_length=10, blank=False, null=False)
    comm_address = models.CharField(
        max_length=250, blank=False, null=False
    )  # Street Address
    location = models.CharField(max_length=50, blank=False, null=False)
    country = models.CharField(max_length=100, blank=False, null=False)
    pincode = models.CharField(max_length=6, blank=False, null=False)
    state = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)  # City Name
    associated_employee = models.ForeignKey(
        "Client",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="associated_employee",
    )
    reg_address = models.CharField(max_length=750, blank=False, null=False)

    contact_person_name = models.CharField(max_length=100, blank=False, null=False)
    contact_person_mobile = models.CharField(max_length=10, blank=False, null=False)
    brand_logo = models.ImageField(upload_to="company/logos/", null=True, blank=True)
    brand_icon = models.ImageField(upload_to="company/icons/", null=True, blank=True)

    enrollment_date = models.DateField(auto_now=True)

    created_at = models.DateTimeField(auto_now=True)

    trash = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.company_name


class Location(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    map_link = models.CharField(max_length=2000, blank=False, null=False)
    address_line_1 = models.CharField(max_length=750, blank=False, null=False)
    address_line_2 = models.CharField(max_length=750, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=50, blank=False, null=False)
    country = models.CharField(max_length=100, blank=False, null=False)
    pincode = models.CharField(max_length=6, blank=False, null=False)
    status = models.BooleanField(null=False, blank=False, default=False)
    created_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="locations",
        blank=False,
        null=False,
    )
    trash = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title if self.title else "Unnamed Location"

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"


class Client(models.Model):
    admin = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, blank=True
    )
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    # Basic Information
    account_id = models.CharField(
        max_length=30,
        unique=True,
        default=uuid.uuid4,
        auto_created=True,
    )
    full_name = models.CharField(
        max_length=100,
        verbose_name="Full Name",
        help_text="Client's full name, max 100 characters.",
        blank=False,
        null=False,
    )
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        verbose_name="Gender",
        help_text="Specify the person's gender.",
        blank=False,
        null=False,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date of Birth",
        help_text="Optional. Select a birth date from the date picker.",
    )
    photo = models.ImageField(
        upload_to="client_photos/",
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]),
            MaxLengthValidator(5242880),
        ],
        verbose_name="Photo",
        help_text="Optional. Max size: 5MB. Allowed formats: JPG/JPEG/PNG. Best size: 800x800px.",
    )

    # Account Information
    email = models.EmailField(
        null=True,
        blank=True,
        validators=[EmailValidator()],
        verbose_name="Email",
        help_text="Optional. Write the client's email address.",
    )
    mobile_no = models.CharField(
        max_length=10,
        unique=True,
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex=r"^\d{10}$",
                message="Enter a valid 10-digit Indian mobile number.",
            )
        ],
        verbose_name="Mobile Number",
        help_text="Enter a 10-digit Indian mobile number.",
    )
    username = models.CharField(
        max_length=50,
        unique=True,
        validators=[
            MinLengthValidator(3, "Username must be at least 3 characters long.")
        ],
        verbose_name="Username",
        help_text="Unique account username, between 3 and 50 characters.",
        blank=False,
        null=False,
    )
    password = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(5, "Password must be at least 5 characters long.")
        ],
        verbose_name="Password",
        help_text="Set a password, between 5 and 30 characters.",
        blank=False,
        null=False,
    )
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default="Inactive",
        verbose_name="Status",
        help_text="Activate or deactivate the account.",
        blank=False,
        null=False,
    )
    notify_via_email_sms = models.BooleanField(
        default=True,
        verbose_name="Email/SMS Notification",
        help_text="Check to send a notification to the client via email/SMS.",
    )

    created_at = models.DateTimeField(auto_now=True)
    trash = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.username})"


class Product(models.Model):
    product_code = models.CharField(max_length=30, unique=True, blank=False, null=False)
    product_title = models.CharField(max_length=150, null=False, blank=False)
    moq = models.PositiveIntegerField(default=1, blank=False, null=False)
    photo = models.ImageField(upload_to="products/", blank=False, null=False)
    description = models.TextField(max_length=2000, blank=False, null=False)

    status = models.BooleanField(default=False, null=False, blank=False)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    trash = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.product_title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Machine(models.Model):
    machine_id = models.CharField(
        max_length=30, unique=True, blank=False, null=False
    )  # Unique machine ID
    machine_name = models.CharField(
        max_length=150, blank=False, null=False
    )  # Machine title
    photo = models.ImageField(
        upload_to="machine_photos/",
        blank=False,
        null=False,
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])],
    )
    location = models.TextField(blank=False, null=True, unique=True)
    status = models.BooleanField(default=False, null=True, blank=True)

    created_at = models.DateTimeField(auto_now=True)
    trash = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.machine_name} ({self.machine_id})"

    class Meta:
        verbose_name = "Machine"
        verbose_name_plural = "Machines"


class machine_attributes(models.Model):
    associated = models.ForeignKey(
        Machine, blank=False, on_delete=models.CASCADE, null=False
    )
    title = models.TextField(blank=False, null=False)
    value = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self(self.title)


class TicketType(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TicketSource(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TicketPriority(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    ticket_id = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        default=uuid.uuid1,
    )
    type = models.ForeignKey(
        TicketType, on_delete=models.CASCADE, null=False, blank=False
    )
    source = models.ForeignKey(
        TicketSource, on_delete=models.CASCADE, null=False, blank=False
    )
    priority = models.ForeignKey(
        TicketPriority, on_delete=models.CASCADE, null=True, blank=True
    )
    client = models.ForeignKey(
        "Client", on_delete=models.CASCADE, related_name="raised", blank=False
    )

    email_sms_notification = models.BooleanField(default=True)
    office = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=False
    )
    machine = models.ForeignKey(
        Machine, on_delete=models.SET_NULL, null=True, blank=False
    )
    subject = models.CharField(max_length=250, blank=False)
    additional_information = models.TextField(blank=False, null=False)
    photo = models.ImageField(upload_to="ticket_photos/", blank=True, null=True)
    video = models.FileField(upload_to="ticket_videos/", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    resolution_status = models.BooleanField(blank=True, null=True, default=True)
    root_cause = models.TextField(blank=True, null=True)
    observation = models.TextField(blank=True, null=True)

    status = models.ForeignKey(
        TicketStatus, on_delete=models.CASCADE, null=True, blank=True, default=1
    )
    trash = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"Ticket {self.ticket_id} - {self.subject}"

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"


class TicketDocs(models.Model):
    associated = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, blank=False, null=False
    )
    title = models.TextField(blank=False, null=False)
    file = models.FileField(blank=False, name=False, upload_to="docs/")
    created_at = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return str(self.title)


class TopBarIcon(models.Model):
    title = models.TextField(blank=False, null=False)
    icon = models.ImageField(upload_to="icon/", blank=False, null=False)
    date = models.DateTimeField(auto_now=True)
    link = models.URLField(blank=False, null=False)

    def __str__(self):
        return str(self.title)


class SideBarIcon(models.Model):
    title = models.TextField(blank=False, null=False)
    icon = models.ImageField(upload_to="icon/", blank=False, null=False)
    date = models.DateTimeField(auto_now=True)
    link = models.URLField(blank=False, null=False)

    def __str__(self):
        return str(self.title)


# General Information Models
class OrderSource(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.CharField(
        max_length=36, unique=True, editable=False, default=uuid.uuid4
    )
    order_date = models.DateField(auto_now=True, blank=False)
    source = models.ForeignKey(
        OrderSource, on_delete=models.SET_NULL, null=True, blank=False
    )
    po_number = models.CharField(max_length=100, blank=False, null=False)
    dc_number = models.CharField(max_length=100, blank=False, null=False)
    additional_note = models.TextField(blank=True, null=False)

    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)
    handled_by = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="handle", blank=False
    )
    email_sms_notification = models.BooleanField(default=True)
    office_delivery = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=False
    )
    machine = models.ForeignKey(
        Machine, on_delete=models.SET_NULL, null=True, blank=False
    )

    # Order Products
    products = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="orders", blank=False
    )

    dc_copy = models.FileField(upload_to="dc_copy", blank=True, null=True)

    # Order Status
    created_at = models.DateTimeField(auto_now_add=True)
    on_hold = models.BooleanField(default=False, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        OrderStatus, on_delete=models.CASCADE, null=True, blank=False
    )

    trash = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"Order {self.order_id}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderDocs(models.Model):
    associated = models.ForeignKey(
        Order, on_delete=models.CASCADE, blank=False, null=False
    )
    title = models.TextField(blank=False, null=False)
    file = models.FileField(blank=False, name=False, upload_to="docs/")
    created_at = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return str(self.title)


class Localization(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to="item_images/", blank=True, null=True)
    status = models.BooleanField(max_length=10, default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="ratings")
    rating = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],  # Ratings from 1 to 5
        verbose_name="Rating (1-5)",
    )
    comments = models.TextField(null=True, blank=True, verbose_name="Comments")
    created_at = models.DateTimeField(auto_now_add=True)

    trash = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"Rating for {self.client.name} - {self.rating}"

    class Meta:
        ordering = ["-created_at"]


class Authorize(models.Model):
    key = models.TextField(blank=False, null=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    request = models.TextField(blank=False, null=False)

    def __str__(self):
        return str(self.key)

    @classmethod
    def checkout(cls, keys):
        try:
            return cls.objects.get(key=keys)
        except cls.DoesNotExist:
            return None


class Country(models.Model):
    country = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(blank=False, null=False, auto_now=True)

    def __str__(self):
        return str(self.country)


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(blank=False, null=False, auto_now=True)

    def __str__(self):
        return str(self.country)


class CompanyMachineTable(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False)
    used_by = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return str(self.company)
