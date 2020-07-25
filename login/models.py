from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Blog(models.Model):
    text = models.TextField()

class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="blogimg")
    image_thumbnail = ImageSpecField(source = 'image', processors=[ResizeToFill(120, 100)], format='JPEG', options={'quality':60})
    #확장자랑 압축도 지정 가능