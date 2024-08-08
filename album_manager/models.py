from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=30, null=False)
    
    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=30, null=False)
    year = models.IntegerField(null=False)  # Elimina max_length
    gender = models.CharField(max_length=30, null=False)  # Sin choices
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='album_images')
    
    def __str__(self):
        return self.name
