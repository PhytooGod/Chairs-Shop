from django.contrib import admin

# Register your models here.

from django.contrib import admin
from core.models import User, Product, Order, Storage
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
#admin.site.register(Storage)