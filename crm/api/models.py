from django.db import models
from django.db import models
from django.core.validators import (
    EmailValidator,
    RegexValidator,
    MaxLengthValidator,
    MinLengthValidator,
    FileExtensionValidator,
)
import uuid


class Company(models.Model):
    company_name = models.CharField(
        max_length=150, unique=True
    )  # Company Name (Non-editable)
    brand_name = models.CharField(
        max_length=150, null=True, blank=True
    )  # Brand Name (Non-editable)
    company_phone = models.CharField(max_length=30)  # Company contact phone number
    website = models.URLField(
        max_length=150, null=True, blank=True
    )  # Company Website address
    company_email = models.EmailField()  # Company support email address
    company_mobile_no = models.CharField(
        max_length=10
    )  # 10 digits company mobile number
    gstin = models.CharField(
        max_length=15, null=True, blank=True
    )  # Goods and Services Taxpayer Identification Number (GSTIN)
    pan_number = models.CharField(
        max_length=10, null=True, blank=True
    )  # Permanent Account Number (PAN)

    # Communication Address
    comm_address = models.CharField(max_length=250)  # Street Address
    location = models.CharField(max_length=50, null=True, blank=True)  # Area Name
    country = models.CharField(max_length=100, null=True, blank=True)  # Country
    pincode = models.CharField(max_length=6, null=True, blank=True)  # 6-digit pincode
    state = models.CharField(max_length=100, null=True, blank=True)  # State
    city = models.CharField(max_length=50, null=True, blank=True)  # City Name

    # Registered Address
    reg_address = models.CharField(
        max_length=750, null=True, blank=True
    )  # Main office address

    # Contact Person
    contact_person_name = models.CharField(
        max_length=100, null=True, blank=True
    )  # Managing contact person name
    contact_person_mobile = models.CharField(
        max_length=10, null=True, blank=True
    )  # Contact person's 10-digit mobile number

    # Additional Fields
    brand_logo = models.ImageField(
        upload_to="company/logos/", null=True, blank=True
    )  # Brand Logo (Image)
    brand_icon = models.ImageField(
        upload_to="company/icons/", null=True, blank=True
    )  # Brand Icon (Favicon)

    enrollment_date = models.DateField(auto_now=True)  # Company Enrollment Date
    
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


class Location(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    map_link = models.CharField(max_length=2000, blank=True, null=True)
    address_line_1 = models.CharField(max_length=750, blank=True, null=True)
    address_line_2 = models.CharField(max_length=750, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    status = models.BooleanField(null=True,blank=True,default=False)
    created_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="locations",
        blank=True,
        null=True,
    )

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
    )
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        verbose_name="Gender",
        help_text="Specify the person's gender.",
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
    )
    password = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(5, "Password must be at least 5 characters long.")
        ],
        verbose_name="Password",
        help_text="Set a password, between 5 and 30 characters.",
    )
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default="Inactive",
        verbose_name="Status",
        help_text="Activate or deactivate the account.",
    )
    notify_via_email_sms = models.BooleanField(
        default=True,
        verbose_name="Email/SMS Notification",
        help_text="Check to send a notification to the client via email/SMS.",
    )
    
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} ({self.username})"


class Product(models.Model):
    product_code = models.CharField(max_length=30, unique=True)
    product_title = models.CharField(max_length=150)
    moq = models.PositiveIntegerField(default=1)
    photo = models.ImageField(upload_to="products/", blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)

    status = models.BooleanField(default=False,null=False,blank=False)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Machine(models.Model):
    machine_id = models.CharField(max_length=30, unique=True)  # Unique machine ID
    machine_name = models.CharField(max_length=150)  # Machine title
    photo = models.ImageField(
        upload_to="machine_photos/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])],
    )
    status = models.BooleanField(default=False,null=True,blank=True)
    attributes = models.JSONField(
        default=dict, blank=True ,null=True
    ) 
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.machine_name} ({self.machine_id})"

    class Meta:
        verbose_name = "Machine"
        verbose_name_plural = "Machines"


class machine_attributes(models.Model):
    associated = models.ForeignKey(Machine,blank=False,on_delete=models.CASCADE,null=False)
    title = models.TextField(blank=False,null=False)
    value = models.TextField(blank=False,null=False)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self(self.title)



class TicketType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TicketSource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name


class TicketPriority(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Ticket(models.Model):
    ticket_id = models.CharField(max_length=30, unique=True, editable=False, default=uuid.uuid1,)
    type = models.ForeignKey(
        TicketType, on_delete=models.SET_NULL, null=True, blank=True
    )
    source = models.ForeignKey(
        TicketSource, on_delete=models.SET_NULL, null=True, blank=True
    )
    priority = models.ForeignKey(
        TicketPriority, on_delete=models.SET_NULL, null=True, blank=True
    )
    client = models.ForeignKey(
        "Client", on_delete=models.CASCADE, related_name="raised"
    )
    handled_by = models.ForeignKey(
        "Client", on_delete=models.CASCADE, related_name="handle_emp"
    )
    email_sms_notification = models.BooleanField(default=True)
    office = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=True
    )
    machine = models.ForeignKey(
        Machine, on_delete=models.SET_NULL, null=True, blank=True
    )
    subject = models.CharField(max_length=250)
    additional_information = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="ticket_photos/", blank=True, null=True)
    video = models.FileField(upload_to="ticket_videos/", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Ticket {self.ticket_id} - {self.subject}"
    


    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"





class TicketDocs(models.Model):
    associated = models.ForeignKey(Ticket,on_delete=models.CASCADE, blank=False,null=False)
    title = models.TextField(blank=False,null=False)
    file = models.FileField(blank=False,name=False,upload_to="docs/")
    created_at = models.DateTimeField(blank=False,auto_now=True)
    
    def __str__(self):
        return str(self.title)

class TopBarIcon(models.Model):
    title = models.TextField(blank=False,null=False)
    icon = models.ImageField(upload_to="icon/",blank=False,null=False)
    date = models.DateTimeField(auto_now=True)
    link = models.URLField(blank=False,null=False)
    
    def __str__(self):
        return str(self.title)



class SideBarIcon(models.Model):
    title = models.TextField(blank=False,null=False)
    icon = models.ImageField(upload_to="icon/",blank=False,null=False)
    date = models.DateTimeField(auto_now=True)
    link = models.URLField(blank=False,null=False)
    
    def __str__(self):
        return str(self.title)




# General Information Models
class OrderSource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name



# Main Order Model
class Order(models.Model):
    order_id = models.CharField(max_length=36, unique=True, editable=False, default=uuid.uuid4)   
    order_date = models.DateField(auto_now=True)
    source = models.ForeignKey(OrderSource, on_delete=models.SET_NULL, null=True, blank=True)
    po_number = models.CharField(max_length=100, blank=True, null=True)
    additional_note = models.TextField(blank=True, null=True)

    # Client Information
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    handled_by = models.ForeignKey(Client, on_delete=models.CASCADE,related_name="handle")
    email_sms_notification = models.BooleanField(default=True)
    office_delivery = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    machine = models.ForeignKey(Machine, on_delete=models.SET_NULL, null=True, blank=True)

    # Order Products
    products = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='orders')

    # Files & Documents
    documents = models.JSONField(blank=True,null=True)

    # Order Status
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_id}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderDocs(models.Model):
    associated = models.ForeignKey(Order,on_delete=models.CASCADE, blank=False,null=False)
    title = models.TextField(blank=False,null=False)
    file = models.FileField(blank=False,name=False,upload_to="docs/")
    created_at = models.DateTimeField(blank=False,auto_now=True)
    
    def __str__(self):
        return str(self.title)



class Localization(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    status = models.BooleanField(max_length=10, default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Rating(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],  # Ratings from 1 to 5
        verbose_name="Rating (1-5)"
    )
    comments = models.TextField(null=True, blank=True, verbose_name="Comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating for {self.client.name} - {self.rating}"

    class Meta:
        ordering = ['-created_at']