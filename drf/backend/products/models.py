import random
from cgitb import lookup
from email.policy import default
from django.conf import settings
from django.db import models
from django.db.models import Q
# Create your models here.

User = settings.AUTH_USER_MODEL

TAGS_MODEL_VALUES = ['electronics', 'cars', 'boats', 'airports']

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True) 
    
    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query) 
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)
    
    def search(self, query, user=None):
        return self.get_queryset().search(query, user= user)
    


class Product(models.Model):
    length = 120
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=length,null=True)
    content = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.9)
    public = models.BooleanField(default=True)

    objects = ProductManager()

    # Algolia function for public field

    def is_public(self) -> bool:
        return self.public

    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]
        # ends
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)

    def get_discount(self):
        return "%.2f" %((float(self.price)) - (float(self.price) * 0.8))

    def __str__(self):
        return f"{self.user} {self.title} {self.price}"

    
    