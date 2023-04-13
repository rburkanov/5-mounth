from rest_framework import serializers
from product.models import  *
from rest_framework.exceptions import  ValidationError



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title price'.split()

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'.split()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text product'.split()
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title rating'.split()
class ValidProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    categdory_id = serializers.IntegerField()

    def Validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError(f"Error! {category_id} does not exists")
        return category_id

class ValidCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
class ValidReview(serializers.ModelSerializer):
    text = serializers.CharField()
    product_id = serializers.IntegerField()
    stars = serializers.IntegerField()

    def Validate_product_id(self, product_id):
        try:
            Review.objects.get(id=product_id)
        except Review.DoesNotExist:
            raise ValidationError(f"Error! {product_id} does not exists")
        return product_id
