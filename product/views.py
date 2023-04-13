from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import *
from product.serializers import *


@api_view(['GET'])
def products_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')
        product = Product.objects.create(title=title, description=description,
                                     price=price, category=category_id)
        product.save()
        return Response(data=ProductSerializers(product).data)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        movie = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Object not found!'})
    if request.method == 'GET':
        serializer = ProductSerializers(movie)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        movie.title= request.data.get('title')
        movie.description = request.data.get('description')
        movie.price = request.data.get('price')
        movie.category_id = request.data.get('category_id')

        movie.save()
        return Response(data=ProductSerializers(movie).data)

@api_view(['GET'])
def category_list_api_view(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializers(category, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        category = Category.objects.create(name=name)
        category.save()
        return Response(data=ProductSerializers(category).data)




@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        movie = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Object not found!'})
    if request.method == 'GET':
        serializer = CategorySerializers(movie)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.price = request.data.get('price')
        movie.category_id = request.data.get('category_id')
        movie.save()
        return Response(data=CategorySerializers(movie).data)

@api_view(['GET'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializers(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        text = request.data.get('text')
        product_id = request.data.get('product_id')
        review = Review.objects.create(text=text, product_id=product_id)
        review.save()
        return Response(data=ReviewSerializers(review).data)




@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        movie = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Object not found!'})
    if request.method == 'GET':
        serializer = ReviewSerializers(movie)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.price = request.data.get('price')
        movie.category_id = request.data.get('category_id')
        movie.save()
        return Response(data=ReviewSerializers(movie).data)


def products_reviews(request):
    product = Product.objects.all()
    serializer = RatingSerializers(product, many=True)
    return Response(data=serializer.data)

