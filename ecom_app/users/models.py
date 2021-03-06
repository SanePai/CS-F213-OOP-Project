from django.db import models
from PIL import Image
from django.contrib.auth.models import User

USER_TYPES = (
    ("CUSTOMER", "CUSTOMER"),
    ("RETAILER", "RETAILER"),
    ("WHOLESALER", "WHOLESALER"),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices = USER_TYPES, default = "CUSTOMER")
    location = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return f'{self.user.username} Profile'