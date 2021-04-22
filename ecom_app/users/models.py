from django.db import models
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    user_type = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.user.username} Profile'

# ****Find another way of doing this, whatever you are doing here****
'''
    def save(self, **kwargs):
        super().save(self)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
'''