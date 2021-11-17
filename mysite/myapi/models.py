from django.db import models


class Image(models.Model):
    image = models.ImageField()
    caption = models.TextField(max_length=100)
    likes = models.IntegerField()


class User(models.Model):
    follow = models.BooleanField()


def __str__(self):
    return self.name
