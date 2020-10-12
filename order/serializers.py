from rest_framework import serializers

from order.models import Order, MenuItem


class OrderSerializer(serializers.ModelSerializer):
    detail = serializers.CharField(initial='1 Latte with soy milk', default='1 Latte', help_text='Order detail')
    clientName = serializers.CharField(initial='John Doe', default='John Doe', help_text='Order client name')
    price = serializers.FloatField(initial='4', default='4', help_text='Order total price')
    isPaid = serializers.BooleanField(initial=False, default=False, help_text='Is order paid?')
    paymentDetail = serializers.CharField(initial='Cash', default='Cash', help_text='Order payment detail')
    isCancelled = serializers.BooleanField(initial=False, default=False, help_text='Is order cancelled?')

    class Meta:
        model = Order
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(initial='Latte', default='Latte', help_text='Menu Item Name')
    price = serializers.FloatField(initial='4', default='4', help_text='Menu Item price')

    class Meta:
        model = MenuItem
        fields = '__all__'
