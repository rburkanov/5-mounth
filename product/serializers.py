from rest_framework import serializers
from product.models import  *

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'name price'.split()

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'.split()

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text product'.split()
