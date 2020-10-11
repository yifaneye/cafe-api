from rest_framework import serializers

from order.models import Order, Payment, MenuItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
