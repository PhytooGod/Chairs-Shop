from rest_framework import serializers

from core.models import Product, Storage, Order, User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    surname = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    address = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'email', 'password', 'address']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


class ProductSerializer1(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    category = serializers.CharField()
    price = serializers.FloatField()
    code = serializers.CharField()
    quantity = serializers.IntegerField()
    rating = serializers.IntegerField()
    photo = serializers.CharField()

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.category = validated_data['category']
        instance.price = validated_data['price']
        instance.code = validated_data['code']
        instance.quantity = validated_data['quantity']
        instance.rating = validated_data['rating']
        instance.photo = validated_data['photo']
        instance.save()
        logging.debug(f'One product updated')
        return instance

    def create(self, validated_data):
        product = Product.objects.create(name=validated_data["name"],
                                         description=validated_data["description"],
                                         category=validated_data["category"],
                                         price=validated_data["price"],
                                         code=validated_data["code"],
                                         quantity=validated_data["quantity"],
                                         rating=validated_data["rating"],
                                         photo=validated_data["photo"])

        logging.debug(f'One product created')
        return product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'price', 'code', 'quantity', 'rating', 'photo')


class StorageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    productId = serializers.IntegerField(write_only=True)
    quantity = serializers.IntegerField()
    address = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Storage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)


class StorageSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ('id', 'name', 'productId', 'quantity', 'address')


class OrderSerializer(serializers.Serializer):
    productId = serializers.IntegerField(write_only=True)
    userId = serializers.IntegerField(write_only=True)
    quantity = serializers.IntegerField()
    totalPrice = serializers.IntegerField()
    delivery = serializers.BooleanField()
    address = serializers.CharField()
    paymentMethod = serializers.CharField()

    def create(self, validated_data):
        logging.debug(f'One order created')
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        logging.debug(f'One order updated')
        instance.name = validated_data.get('name', instance.name)


class OrderSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'productId', 'userId', 'quantity', 'totalPrice', 'delivery', 'address', 'paymentMethod')
