from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Book
from django.contrib.auth import authenticate
from rest_framework import exceptions
class Bookserializer(ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"

class Loginserializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self,data):
        username=data.get("username")
        password=data.get("password")
        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                data["user"]=user
            else:
                msg="unable to login"
                raise exceptions.ValidationError(msg)
        else:
            msg="you have to pride username and password"
            raise exceptions.ValidationError(msg)
        return data
