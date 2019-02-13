from django.db import models

# Create your models here.

class Mentee(models.Model):
    nama_mentee = models.CharField(max_length = 255)
    testimoni = models.CharField(max_length = 300)
    # foto_mentee = models.CharField(max_length = 300)
    foto_mentee = models.ImageField(upload_to = 'upload')

    def __str__(self):
        return self.nama_mentee