from email.policy import default
from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL
class Product(models.Model):
    length = 120
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=length,null=True)
    content = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.9)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)

    def get_discount(self):
        return "%.2f" %((float(self.price)) - (float(self.price) * 0.8))

    def __str__(self):
        return f"{self.title} {self.price}"