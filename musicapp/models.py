from django.db import models
from datetime import datetime

# Create your models here.

class Song(models.Model):
    title=models.CharField(max_length=400)
    date_released=models.CharField(max_length=400)
    artiste_id=models.IntegerField()
    likes=models.CharField(max_length=400)

class Artiste(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    age=models.IntegerField()
    
class Lyric(models.Model):
    content=models.CharField(max_length=400)
    song_id=models.CharField(max_length=400)
