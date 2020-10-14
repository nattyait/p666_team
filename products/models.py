from django.db import models
from django.core.exceptions import ValidationError

class Product(models.Model):
    name = models.CharField(max_length=200)
    point = models.FloatField()
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name