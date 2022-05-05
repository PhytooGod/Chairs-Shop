from django.db import models

# Create your models here.
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer



class User(models.Model):
    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    address = models.CharField(max_length=300, default='None')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'password': self.password,
            'address': self.address,
        }


class Product(models.Model):
    name = models.CharField(max_length=300)
    category = models.CharField(max_length=30, default='None')
    description = models.TextField()
    code = models.CharField(max_length=10,default='None')
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    photo = models.CharField(max_length=300, default ='Photo')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'code': self.code,
            'price': self.price,
            'quantity': self.quantity,
            'rating': self.rating,
            'photo' : self.photo
        }


class Order(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0)
    totalPrice = models.FloatField(default=0)
    delivery = models.BooleanField(default=False)
    address = models.CharField(max_length=300, default='None')
    paymentMethod = models.CharField(max_length=10, default='cash')

    def to_json(self):
        return {
            'id': self.id,
            'productId': self.productId,
            'userId': self.userId,
            'quantity': self.quantity,
            'totalPrice': self.totalPrice,
            'delivery': self.delivery,
            'address': self.address,
        }


class Storage(models.Model):
    name = models.CharField(max_length=100)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    address = models.CharField(max_length=100)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'productId': self.productId,
            'quantity': self.quantity,
            'address': self.address,
        }