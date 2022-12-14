from django.db import models

# Create your models here.

class Book(models.Model):
   
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    publish_year = models.PositiveIntegerField()
    rating = models.PositiveIntegerField(default = 3)
    comments = models.CharField(max_length = 1000)
    def __str__(self):
        return self.name