from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from api.views import views, views_generics, views_fbv, views_cbv

urlpatterns = [
    path('login/', obtain_jwt_token),

    path('users/<int:id>', views_cbv.UserDetailAPIView.as_view(), name='userDetail'),
    path('users/', views_cbv.UserListAPIView.as_view(), name='userList'),

    path('storages/', views_fbv.storage_list, name='storageList'),
    path('storages/<int:id>', views_fbv.storage_detail, name='storageList'),

    path('orders/', views_generics.OrderListAPIView.as_view(), name='orderList'),
    path('orders/<int:pk>', views_generics.OrderDetailAPIView.as_view(), name='orderList'),

    path('products/', views_generics.ProductListAPIView.as_view(), name='productList'),
    path('products/<int:pk>/', views.ProductDetailAPIView.as_view(), name='productDetail'),
]
