from django.db import models
from shop.models import Product


class Codes_load(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.PROTECT)
    passFile = models.TextField()
    loadDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.passFile

    class Meta:
        verbose_name = 'Subscriptions test Files'
        verbose_name_plural = 'Subscriptions test Files'
