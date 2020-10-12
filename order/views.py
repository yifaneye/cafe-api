from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import GenericViewSet

from order.models import Order, MenuItem
from order.serializers import OrderSerializer, MenuItemSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    lookup_field = 'id'
    serializer_class = OrderSerializer


class MenuItemViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
