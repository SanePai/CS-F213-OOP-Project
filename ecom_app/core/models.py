from django.db import models

# Create your models here.
class Product(models.Model):
    seller = models.CharField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    img = models.ImageField(default = "default.png", upload_to = "product_imgs/", blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    