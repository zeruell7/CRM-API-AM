from rest_framework import serializers
from .models import Costumer
from django.contrib.auth.models import User


# this class is used to serialize the costumer information
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
        extra_kwargs = {'creatoruser':{'read_only':True},'lastupdateuser':{'read_only':True}} # this properties avoid to show the fields in the formview
    
# this class is used to serialize the user information
class USerSerializerModelView(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'is_staff'
        )
        extra_kwargs = {'password':{'write_only':True}} # this properties avoid to show the password field in the formview
    # this method perform the user creation 
    def save(self, validated_data):
        instance = User()
        instance.is_staff = validated_data.get('is_staff')
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance
    # this method perform the user update
    def update(self, validated_data, pk=None):
        instance = User()
        instance.id = pk
        instance.is_staff = validated_data.get('is_staff')
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance



