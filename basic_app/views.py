from django.shortcuts import render
from rest_framework import generics
from basic_app.models import Bots, Users
from basic_app.serializers import BotsSerializer, UsersSerializer
# Create your views here.


class BotsList(generics.ListCreateAPIView):
    queryset = Bots.objects.all()
    serializer_class = BotsSerializer

class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer