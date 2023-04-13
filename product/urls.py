from django.contrib import admin
from django.urls import path
from product.views import *

urlpatterns = [
    path('api/v1/products/',products_list_api_view),
    path('/api/v1/products/<int:id>/',product_detail_api_view),
    path('/api/v1/categories/',category_list_api_view),
    path(' /api/v1/categories/<int:id>/',category_detail_api_view),
    path('/api/v1/reviews/',review_list_api_view),
    path('/api/v1/reviews/<int:id>/',review_detail_api_view),
    path('/api/v1/products/reviews/',products_reviews)
]
