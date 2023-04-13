from rest_framework import serializers
from product.models import  *

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title price'.split()

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'.split()

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text product'.split()
class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title rating'.split()
