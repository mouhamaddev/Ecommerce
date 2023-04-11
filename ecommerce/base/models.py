from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from django import forms


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/')
    address = models.CharField(max_length=255)
    user_first_name = models.CharField(max_length=30)
    user_last_name = models.CharField(max_length=30)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=128)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    user_last_login = models.DateTimeField(null=True, blank=True)
    payment_methods = models.TextField(null=True, blank=True)
    wishlist = ArrayField(models.PositiveIntegerField(), blank=True, null=True)
    order_history = ArrayField(models.PositiveIntegerField(), blank=True, null=True)

    def __str__(self):
        return self.user.username

class Country(models.Model):
    name = models.CharField(max_length=255)

class Image(models.Model):
    image = models.ImageField(upload_to='item_images/')

class Item(models.Model):
    name = models.CharField(max_length=255)
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    comments = models.TextField()
    num_sold = models.PositiveIntegerField(default=0)
    num_rated = models.PositiveIntegerField(default=0)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    countries = models.ManyToManyField(Country)
    num_remaining = models.PositiveIntegerField()
    delivery_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    images = models.ManyToManyField(Image)
    video_link = models.URLField()
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    promotion = models.CharField(max_length=255, null=True, blank=True)
    order_status = models.CharField(max_length=255, null=True, blank=True)
    order_date = models.DateTimeField(null=True, blank=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name='order_items')
    order_number = models.CharField(max_length=10)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MyForm(forms.Form):
    form_first_name = models.CharField(max_length=30)
    captcha = ReCaptchaField()