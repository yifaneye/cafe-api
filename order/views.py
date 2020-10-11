from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets

from order.models import Order, Payment, MenuItem
from order.serializers import OrderSerializer, PaymentSerializer, MenuItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
