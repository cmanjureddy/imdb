from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


from movie.models import (
    Actor,
    Director,
    Genre,
    Movie,
    Writer
)

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name'
        ]
    
    def validate(self, data):
        if len(data['username']) < 7:
            raise serializers.ValidationError("The username length should be at least 8.")
        try:
            password_validation.validate_password(data['password'])
        except Exception as e:
            raise serializers.ValidationError(e)
        return data

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user

class StaffCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name'
        ]
    
    def validate(self, data):
        if len(data['username']) < 7:
            raise serializers.ValidationError("The username length should be at least 8.")
        try:
            password_validation.validate_password(data['password'])
        except Exception as e:
            raise serializers.ValidationError(e)
        return data

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        user.is_staff = True
        user.save()
        return user




class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        depth = 1


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'