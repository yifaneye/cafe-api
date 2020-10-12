from django.db import models

# Create your models here.


class Order(models.Model):
    detail = models.TextField()
    clientName = models.TextField()
    price = models.FloatField(blank=True, null=True)
    ORDER_STATUS_CHOICES = [('unpaid', 'Unpaid'), ('cancelled', 'Cancelled'), ('paid', 'Paid'), ('finished', 'Finished')]
    status = models.CharField(max_length=9, choices=ORDER_STATUS_CHOICES, default='unpaid')
    paymentDetail = models.TextField(blank=True, null=True)


class MenuItem(models.Model):
    name = models.TextField()
    MENU_ITEM_TYPES = [('coffee', 'Coffee'), ('addition', 'Addition')]
    type = models.CharField(max_length=8, choices=MENU_ITEM_TYPES)
    price = models.FloatField()
