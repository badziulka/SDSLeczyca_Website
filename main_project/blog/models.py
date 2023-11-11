import os.path
from io import BytesIO

from django.db import models
from django.core.files import File


class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='', null=True)
# Create your models here.


    @classmethod
    def create_from_file(cls, file):
        abs_path = os.path.abspath(file)
        if abs_path.endswith('.jpg'):
            new_photo_object = cls.objects.create(title='tmp')
            new_photo_object.image.save('test', File(open(abs_path, 'rb')))


