from rest_framework import generics,status
from .serializers import UserSerializer
from .models import User
from django.db import IntegrityError
from rest_framework.response import Response
from django.http import Http404




class CreateUser(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response({'error': 'Integrity Error: Email must be unique.'}, status=status.HTTP_400_BAD_REQUEST)


class ListUsers(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer

    

class GetUserByIdView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Http404:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)