from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Content(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    story = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title