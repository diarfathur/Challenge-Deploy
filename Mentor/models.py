from django.db import models

# Create your models here.
class Mentor(models.Model):
    nama_mentor = models.CharField(max_length = 255)
    testimoni = models.CharField(max_length = 300)
    experience = models.CharField(max_length = 300)
    foto_mentor = models.ImageField(upload_to = 'mentor')

    def __str__(self):
        return self.nama_mentor