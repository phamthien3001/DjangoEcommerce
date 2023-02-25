from django.db import models
import datetime
import os
from django.contrib.auth.models import User
# Create your models here.
def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:$M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)

class Category(models.Model):
    slug = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Tredning")
    meta_title = models.CharField(max_length=150, null = True, blank=True)
    meta_keywords = models.CharField(max_length=150, null = True, blank=True)
    meta_description = models.TextField(max_length=500, null = True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    small_description = models.CharField(max_length=150)
    quantity = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Tredning")
    tag = models.CharField(max_length=255)
    meta_title = models.CharField(max_length=150, null = True, blank=True)
    meta_keywords = models.CharField(max_length=150, null = True, blank=True)
    meta_description = models.TextField(max_length=500, null = True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
     


