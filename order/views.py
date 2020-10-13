from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet

from order.models import Order, MenuItem
from order.serializers import OrderSerializer, MenuItemSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('status',)


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    lookup_field = 'id'
    serializer_class = OrderSerializer


class MenuItemViewSet(ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('type',)
