from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Comments(models.Model):
    name = models.CharField(max_length = 150)
    comment = models.TextField()
    email = models.EmailField(max_length = 254)
    publish_date = models.DateTimeField(default=datetime.now)
    type = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-publish_date']

class Publish(models.Model):
    post = models.TextField()
    post_date = models.DateTimeField(default=datetime.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length = 100)
    is_allowed = models.BooleanField(default=False)
    file = models.FileField()
    file2 = models.FileField()

    def __str__(self):
        return self.post
    
    class Meta:
        ordering = ['-post_date']


