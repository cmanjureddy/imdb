from django.urls import path
from rest_framework import routers
from movie import views as movie_views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('', movie_views.MovieViewSet)


urlpatterns = [
    path('token', obtain_auth_token, name='get-token'),
    path('actors', movie_views.ActorView.as_view(), name='actors'),
    path('directors', movie_views.DirectorView.as_view(), name='directors'),
    path('writers', movie_views.WriterView.as_view(), name='writers'),
    path('genres', movie_views.GenreView.as_view(), name='genres'),
    path('create/user', movie_views.UserCreateView.as_view(), name='create-user'),
    path('create/staff', movie_views.StaffCreateView.as_view(), name='create-staff'),
]

urlpatterns += router.urls

