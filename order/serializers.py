from rest_framework import serializers

from order.models import Order, Payment, MenuItem


class OrderSerializer(serializers.ModelSerializer):
    detail = serializers.CharField(help_text='Order detail')
    clientName = serializers.CharField(help_text='Order client name')
    price = serializers.FloatField(help_text='Order total price', read_only=True)
    isPaid = serializers.BooleanField(help_text='Is order paid?', read_only=True)
    isCancelled = serializers.BooleanField(help_text='Is order cancelled?', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['price', 'isPaid', 'isCancelled']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
