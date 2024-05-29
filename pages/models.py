from django.db import models
from datetime import datetime


# Create your models here.

class Contacts(models.Model):
    suggestion = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.suggestion
    
class Studies(models.Model):
    subject = models.TextField()
    url = models.CharField(max_length = 150)
    image = models.FileField()
    publish_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['publish_date']
