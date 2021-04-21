from django.db import models

# Create your models here.
class Product(models.Model):
    seller = models.CharField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True, upload_to = "product_imgs/")