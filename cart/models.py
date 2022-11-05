from django.db import models
from app.models import Book
# Create your models here.
class WishItem(models.Model):
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default = 1)
    def __str__(self):
        return f"{self.quantity} of {self.product}"
