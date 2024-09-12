from rest_framework import serializers

from api.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.FloatField()

    class Meta:
        model = Product
        fields = "__all__"
