from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to="prof_pics/",null=True,blank=True)
    description = RichTextField(blank=True)
    is_author = models.BooleanField(default=True)

    def __str__(self):
        return self.email