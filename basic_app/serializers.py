from rest_framework import serializers
from basic_app.models import Bots, Users
class BotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bots
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'