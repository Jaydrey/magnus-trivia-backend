from django.shortcuts import render

# rest framework imports views
from rest_framework.views import APIView
from rest_framework import generics
# rest framework import permissions
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
# rest framework import Responses
from rest_framework.response import Response
from rest_framework import status
# django auth model import
from .models import User

# Create your views here.
class GenesisAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    http_method_names: list[str] = ["get"]

    def get(self, request, *args, **kwargs):
        return Response({"message": "successfully accessed the auth api"}, status=status.HTTP_200_OK)

class UserAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names: list[str] = ["get", "post"]

    def post(self, request, *args, **kwargs):
        pass
    