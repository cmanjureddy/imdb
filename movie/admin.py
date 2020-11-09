from django.contrib import admin
from movie.models import (
    Actor,
    Director,
    Genre,
    Movie,
    Writer
)


admin.site.register(
    (
        Actor,
        Director,
        Genre,
        Movie,
        Writer
    )
)