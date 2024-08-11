from django.db import models

# Create your models here.

class NanoLink(models.Model):
    original_link = models.URLField()
    key = models.URLField(max_length=10, unique=True)
    acces_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    