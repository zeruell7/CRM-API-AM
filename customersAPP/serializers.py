from rest_framework import serializers
from .models import Costumer
from django.contrib.auth.models import User

class CostumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costumer
        fields = (
            'id',
            'name',
            'surname',
            'photo',
            'creatoruser',
            'lastupdateuser'
        )
    

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def create(self, validated_data):
        instance = User()
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance
    
    def validate_username(self,data):
        users = User.objects.filter(username = data)
        if len(users) != 0:
            raise serializers.ValidationError("This username does exists, try a diferent username")
        else:
            return data




