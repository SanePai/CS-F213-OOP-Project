from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator
from decimal import Decimal


CAT_CHOICES = (
    ("vegetables", "Vegetables"),
    ("fruits", "Fruits"),
    ("groceries", "Groceries"),
)

UNIT_CHOICES = (
    ("kg", "Kilograms"),
    ("lb", "Pounds (lb)"),
    ("l", "Litres"),
    ("no", "Number (Individual pieces)"),
    ("bags", "Bags"),
)





class Product(models.Model):
    seller = models.ForeignKey(User, on_delete = models.CASCADE, related_name="seller")
    date_posted = models.DateTimeField(auto_now_add=True)
    stock = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, validators=[MinValueValidator(Decimal('0.00'))])
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    img = models.FileField(default = "default.png", upload_to = "", blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, validators=[MinValueValidator(Decimal('0.00'))])
    tags = models.CharField(
        max_length = 20,
        choices = CAT_CHOICES,
        default = 'vegetables',
    )
    measurment_unit = models.CharField(
        max_length = 5,
        choices = UNIT_CHOICES,
        default = 'kg',

    )
    price_per_unit = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('prod-detail', kwargs={'pk': self.pk})
    

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, validators=[MinValueValidator(Decimal('0.00'))])

class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    phone_num = models.PositiveIntegerField(blank=True, null=True)
    address1 = models.CharField(max_length = 255)
    address2 = models.CharField(max_length = 255, blank=True, null=True)
    country = models.CharField(max_length = 30)
    state = models.CharField(max_length = 30)
    zip_code = models.PositiveIntegerField()

    

