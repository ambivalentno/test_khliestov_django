from django.db import models

class Note(models.Model):
    
    title = models.CharField(max_length=50)
    text = models.TextField()