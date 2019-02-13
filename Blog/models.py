from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    judul = models.CharField(max_length = 255)
    isi_post = models.CharField(max_length = 3000)
    created_at = models.DateField(default=timezone.now())
    foto = models.ImageField(upload_to = 'post')

    def __str__(self):
        return self.judul