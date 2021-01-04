from rest_framework import serializers
from django.contrib.auth.models import User



# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'], email=validated_data['email'])
        return user


# User serializer
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']
