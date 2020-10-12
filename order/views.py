from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from order.models import Order, MenuItem
from order.serializers import OrderSerializer, MenuItemSerializer


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class MenuItemViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
