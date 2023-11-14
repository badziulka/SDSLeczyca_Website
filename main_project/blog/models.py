from django.db import models
from photologue.models import PhotoEffect

class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='', null=True)
    effect = models.ForeignKey(PhotoEffect, on_delete=models.CASCADE, null=True, related_name='blog_photos')