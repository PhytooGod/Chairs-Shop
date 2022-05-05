from django.http.response import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import *
from core.models import User, Product, Order, Storage


@csrf_exempt
def users_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_json = [user.to_json() for user in users]
        return JsonResponse(users_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            users = User.objects.create(
                name=data['name'],
                surname=data['surname'],
                email=data['email'],
                password=data['password'],
                address=data['address']
            )
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)
        return JsonResponse(users.to_json(), status=200)


@csrf_exempt
def user(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    if request.method == 'GET':
        return JsonResponse(user.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        try:
            user.name = data['name']
        except:
            pass
        try:
            user.password = data['password']
        except:
            pass
        try:
            user.surname = data['surname']
        except:
            pass
        try:
            user.email = data['email']
        except:
            pass
        try:
            user.address = data['address']
        except:
            pass
        user.save()
        return JsonResponse(user.to_json())
    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'deleted'}, status=204)


@csrf_exempt
def products_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_json = [product.to_json() for product in products]
        return JsonResponse(products_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            products = Product.objects.create(
                name=data['name'],
                category=data['category'],
                description=data['description'],
                code=data['code'],
                price=data['price'],
                quantity=data['quantity'],
                rating=data['rating'],
            )
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)
        return JsonResponse(products.to_json(), status=200)


@csrf_exempt
def product(request, id):
    try:
        product = Product.objects.get(id=id)
    except User.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    if request.method == 'GET':
        return JsonResponse(user.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        try:
            product.name = data['name']
        except:
            pass
        try:
            product.category = data['category']
        except:
            pass
        try:
            product.description = data['description']
        except:
            pass
        try:
            product.code = data['code']
        except:
            pass
        try:
            product.price = data['price']
        except:
            pass
        try:
            product.quantity = data['quantity']
        except:
            pass
        try:
            product.rating = data['rating']
        except:
            pass
        product.save()
        return JsonResponse(user.to_json())
    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({'message': 'deleted'}, status=204)





class UserDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist as e:
            raise Http404

    def get(self, request, id=None):
        user = self.get_object(id=id)
        return JsonResponse(user.to_json())

    def put(self, request, id=None):
        pass

    def delete(self, request, id=None):
        user = self.get_object(id)
        user.delete()
        return Response({'message': 'deleted'}, status=204)


class UserListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        users = users.to_json()
        return Response(users.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = json.loads(request.body)
        try:
            user = User.objects.create(
                name=data['name'],
                surname=data['surname'],
                email=data['email'],
                password=data['password'],
                address=data['address']
            )
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)
        return JsonResponse(user.to_json(), status=200)


"""api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.filter(name__contains='a').order_by('id')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

"""

class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(id=pk)
        except Product.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        product = self.get_object(pk)
        serializer = ProductSerializer1(product)
        return Response(serializer.data)

    def put(self, request, pk=None):
        product = self.get_object(pk)
        serializer = ProductSerializer1(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        product = self.get_object(pk)
        product.delete()
        return Response({'message': 'deleted'}, status=204)