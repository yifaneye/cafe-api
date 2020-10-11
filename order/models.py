from django.db import models

# Create your models here.


class Order(models.Model):
    detail = models.TextField()
    clientName = models.TextField()
    price = models.FloatField()
    isPaid = models.BooleanField(default=False)
    isCancelled = models.BooleanField(default=False)


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    detail = models.TextField(blank=True, null=True)
    price = models.FloatField()


class MenuItem(models.Model):
    name = models.TextField()
    MENU_ITEM_TYPES = [('coffee', 'Coffee'), ('addition', 'Addition')]
    type = models.CharField(max_length=8, choices=MENU_ITEM_TYPES)
    price = models.FloatField()
