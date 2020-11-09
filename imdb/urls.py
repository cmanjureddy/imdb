from movie import views as movie_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include("movie.urls")),
    path('', movie_views.RedirectToMovie.as_view(), name='home')
]
