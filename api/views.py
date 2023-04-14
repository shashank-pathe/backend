from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.contrib.auth.models import User
from .serializers import ProductSerializer, ProductCategorySerializer, UserSerializer, UserDetailSerializer, CreateUserSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

def hello_world(request):
    my_data = CarouselItem.objects.get(id=2)
    print(my_data.product.id,"my_data.........................................")
    return HttpResponse("Hello, world!")

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryList(APIView):
    def get(self, request):
        categories = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data)

class UserDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)

class CreateUser(APIView):
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.http import JsonResponse

def category_products(request, category_id):
    category = get_object_or_404(ProductCategory, pk=category_id)
    products = Product.objects.filter(category=category)
    data = {
        'category': category.name,
        'products': [{
            'id': product.id,
            'name': product.name,
            'price': float(product.price),
            'image': product.image.url if product.image else None,
        } for product in products]
    }
    return JsonResponse(data)


def category_list(request):
    categories = ProductCategory.objects.all()
    data = {
        'categories': [{
            'id': category.id,
            'name': category.name,
        } for category in categories]
    }
    return JsonResponse(data)

#authetication

from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)