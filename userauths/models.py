from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image", null=True, blank=True)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True) 
    address = models.CharField(max_length=200, null=True, blank=True) 
    country = models.CharField(max_length=200, null=True, blank=True) 
    verified = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Profiles"

    def profile_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return f"{self.user.username} - {self.full_name} - {self.bio}"