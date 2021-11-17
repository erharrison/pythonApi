from django.db import models


# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.id, filename)

class Image(models.Model):
    # image = models.ImageField(upload_to=user_directory_path)
    caption = models.TextField(max_length=100)
    likes = models.IntegerField(default=0)


class User(models.Model):
    follow = models.BooleanField()


def __str__(self):
    return self.name
