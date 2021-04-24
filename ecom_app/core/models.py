from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator
from decimal import Decimal


CAT_CHOICES = (
    ("veg", "Vegetables"),
    ("fruit", "Fruits"),
    ("groc", "Groceries"),
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
    stock = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    img = models.FileField(default = "default.png", upload_to = "", blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, validators=[MinValueValidator(Decimal('0.00'))])
    tags = models.CharField(
        max_length = 20,
        choices = CAT_CHOICES,
        default = 'veg',
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
    

    