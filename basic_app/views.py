from django.shortcuts import render
from rest_framework import generics
from basic_app.models import Bots, Users
from basic_app.serializers import BotsSerializer, UsersSerializer
# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response

class BotsList(generics.ListCreateAPIView):
    queryset = Bots.objects.all()
    serializer_class = BotsSerializer



class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.copy()

        chat_id = data.get("chat_id")
        bot_id = data.get("bot_id")

        if not chat_id or not bot_id:
            return Response(
                {"detail": "chat_id va bot_id majburiy"},
                status=status.HTTP_400_BAD_REQUEST
            )

        obj, created = Users.objects.update_or_create(
            chat_id=chat_id,
            bot_id=bot_id,
            defaults={
                **data,
                "status": "active"
            }
        )

        return Response(
            UsersSerializer(obj).data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK
        )


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer