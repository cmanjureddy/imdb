from django.db import models



class Writer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    writers = models.ManyToManyField(Writer)
    cast = models.ManyToManyField(Actor)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    plot = models.TextField(max_length=500)

    def __str__(self):
        return self.name

