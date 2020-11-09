from django.shortcuts import render, redirect
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import views
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


from movie.models import (
    Actor,
    Director,
    Genre,
    Movie,
    Writer
)

from movie.serializers import (
    MovieSerializer,
    ActorSerializer,
    DirectorSerializer,
    GenreSerializer,
    WriterSerializer,
    UserCreateSerializer,
    StaffCreateSerializer
)


class StaffPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method == 'GET':
                return True
            else:
                if request.user.is_staff:
                    return True


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [StaffPermission]
    authentication_classes = [authentication.TokenAuthentication]


class ActorView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [StaffPermission]
    authentication_classes = [authentication.TokenAuthentication]


class DirectorView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [StaffPermission]
    authentication_classes = [authentication.TokenAuthentication]


class WriterView(generics.ListCreateAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    permission_classes = [StaffPermission]
    authentication_classes = [authentication.TokenAuthentication]


class GenreView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [StaffPermission]
    authentication_classes = [authentication.TokenAuthentication]


class RedirectToMovie(views.APIView):
    def get(self, request):
        return redirect('api-root')

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]
    
class StaffCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = StaffCreateSerializer
    permission_classes = [permissions.AllowAny]
    