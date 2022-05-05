import json
import logging
from django.http import Http404, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer
from core.models import User

logging.basicConfig(filename='ChairsProject.log', filemode='a', format='%(asctime)s - %(message)s')


class UserDetailAPIView(APIView):
    def get_object(self, id):
        try:
            logging.debug('One user returned')
            return User.objects.get(id=id)
        except User.DoesNotExist as e:
            raise Http404

    def get(self, request, id=None):
        user = self.get_object(id=id)
        user = UserSerializer(user)
        logging.debug('One user returned after serilization')
        return JsonResponse(user.data)

    def put(self, request, id=None):
        user = self.get_object(id)
        user = UserSerializer(instance=user, data=request.data)
        if user.is_valid():
            user.save()
            logging.debug(f'User with id:{id} updated')
            return Response(user.data)
        return Response(user.errors)

    def delete(self, request, id=None):
        user = self.get_object(id)
        user.delete()
        logging.debug(f'User with id:{id} deleted')
        return Response({'message': 'deleted'}, status=204)


class UserListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        users1 = UserSerializer(users, many=True)
        logging.debug(f'All users returned')
        return JsonResponse(users1.data, safe=False)

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
            logging.debug(f'New user created')
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)
        return JsonResponse(user.to_json(), status=200)
