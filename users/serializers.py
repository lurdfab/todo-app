from rest_framework import serializers
from .models import *
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=20, min_length=5)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True) #we used write only because we don't want it returned back to the server


    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password") #these are the fields we want to appear on the client side / converted from the model to json


    def validate(self, attrs): #this method is used to validate our emails to avoid an email being used twice

        email_exists = User.objects.filter(email=attrs["email"]).first()
        if email_exists:
            raise ValidationError("Email already exists")
        return super().validate(attrs)
        
    def create(self, validated_data): #this method is used to hash password & generate token during registration.
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
    


class LoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=20, min_length=5)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True) #we used write only because we don't want it returned back to the server

    class Meta:
        model = User
        fields = ("username", "password") #these are the fields we want to appear on the client side / converted from the model to json
     


#this connects the todo or post to the owner / user
class CurrentUserToDoSerializer(serializers.ModelSerializer):

    todo = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ("id", "username", "email")