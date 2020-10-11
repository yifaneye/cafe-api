from django.db import models

# Create your models here.


class Order(models.Model):
    detail = models.TextField()
    clientName = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    isPaid = models.BooleanField(default=False)


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    isSuccessful = models.BooleanField(default=False)


class MenuItem(models.Model):
    name = models.TextField()
    MENU_ITEM_TYPES = [('coffee', 'Coffee'), ('addition', 'Addition')]
    type = models.CharField(max_length=8, choices=MENU_ITEM_TYPES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
