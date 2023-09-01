
from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(default='')

    def __str__(self):
        return f'Id {self.id}: {self.title}'




