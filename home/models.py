from django.db import models

# Create your models here.
class Testimonials(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    video = models.FileField()

