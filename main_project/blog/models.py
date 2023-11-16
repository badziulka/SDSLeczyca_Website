from django.db import models
from photologue.models import PhotoEffect

from photologue.models import Photo as PhotologuePhoto

class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/', null=True)

    def get_next_photo(self):
        return PhotologuePhoto.objects.filter(id__gt=self.id).order_by('id').first()

    def get_previous_photo(self):
        return PhotologuePhoto.objects.filter(id__lt=self.id).order_by('-id').first()

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    photos = models.ManyToManyField(Photo, through='GalleryPhoto')

class GalleryPhoto(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

