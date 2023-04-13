from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import *
from product.serializers import *


@api_view(['GET'])
def products_list_api_view(request):
    products = Product.objects.all()
    serializer = ProductSerializers(products, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        movie = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Object not found!'})
    serializer = ProductSerializers(movie)
    return Response(data=serializer.data)

@api_view(['GET'])
def category_list_api_view(request):
    category = Category.objects.all()
    serializer = CategorySerializers(Category, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Object not found!'})
    serializer = CategorySerializers(category,many = True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializers(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        movie = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Object not found!'})
    serializer = ReviewSerializers(movie)
    return Response(data=serializer.data)

def products_reviews(request):
    product = Product.objects.all()
    serializer = RatingSerializers(product, many=True)
    return Response(data=serializer.data)