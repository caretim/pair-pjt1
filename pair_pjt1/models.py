from django.db import models


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(default='Null')
    created_at = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)