from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Product, Comment
from .serializers import ProductSerializer, ProfileSerializer, CommentSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserRegisterationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = {'user': user.id,
                    'message': 'User registration successfully'

                    }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

class CommentAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []