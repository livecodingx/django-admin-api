from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'El nombre de usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )
        return Response({'message': 'Usuario registrado con éxito'}, status=status.HTTP_201_CREATED)
