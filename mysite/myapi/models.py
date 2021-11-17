from django.db import models
from django.contrib.auth.models import User


# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.id, filename)

# class Users(models.Model):
#     follow = models.BooleanField()
#     username = models.CharField(max_length=20)


class ImagePost(models.Model):
    # image = models.ImageField(upload_to=user_directory_path)
    caption = models.TextField(max_length=100)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.name
