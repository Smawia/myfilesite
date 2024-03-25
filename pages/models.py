from django.db import models

# Create your models here.

class Contacts(models.Model):
    suggestion = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.suggestion
