from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from order.models import Order, Payment, MenuItem
from order.serializers import OrderSerializer, PaymentSerializer, MenuItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PaymentViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     GenericViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class MenuItemViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
