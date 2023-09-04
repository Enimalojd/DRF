from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    '''Модель категории товаров'''
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name']), ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:service_list_by_category', args=[self.slug])


class Service(models.Model):
    '''Модель услуг/товаров'''
    category = models.ForeignKey(Category, related_name='services', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(null=True)
    viewers = models.ManyToManyField(User, through='UserServiceRelation', related_name='service')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_service')

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['title']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Id {self.id}: {self.title}'

    def get_absolute_url(self):
        return reverse('store:service_detail', args=[self.id, self.slug])


class UserServiceRelation(models.Model):
    '''Модель оценки пользователем услуги'''
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
