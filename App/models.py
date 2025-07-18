from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.TextField()
    artist = models.TextField()
    image = models.ImageField()
    audio_file = models.FileField()
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return  self.title