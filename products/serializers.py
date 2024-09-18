from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        match (data['price'], data['name']):
            case (price, name) if price <= 0:
                raise serializers.ValidationError("Price must be a positive number.")
            case (_, name) if not name:
                raise serializers.ValidationError("Name cannot be empty.")
        return data