from django.db import models
from shop.models import Product
from orders.models import Order


class Codes(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.PROTECT)
    serialNum = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    loadDate = models.DateField(auto_now_add=True)
    ignor = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)
    soldDate = models.DateField(auto_now=True)
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = 'Subscriptions List'
        verbose_name_plural = 'Subscriptions List'
        ordering = ('-id',)

    def __str__(self):
        return '{}'.format(self.code)
