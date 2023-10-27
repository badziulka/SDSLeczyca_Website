from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='')
# Create your models here.
