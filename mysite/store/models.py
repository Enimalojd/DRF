from django.contrib.auth.models import User
from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(null=True)
    viewers = models.ManyToManyField(User, through='UserServiceRelation', related_name='service')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_service')

    def __str__(self):
        return f'Id {self.id}: {self.title}'


class UserServiceRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Terribly'),
        (2, 'Bad'),
        (3, 'Fine'),
        (4, 'Good'),
        (5, 'Awsome')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    like = models.BooleanField(default=False)
    in_bookmark = models.BooleanField(default=False)
    rate = models.PositiveIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return f'{self.user.username} {self.service}, rate: {self.rate}'
