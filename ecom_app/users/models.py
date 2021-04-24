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
    def __str__(self):
        return f'{self.user.username} Profile'