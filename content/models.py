from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='cat_logo/',null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=320)

    def __str__(self):
        return self.name




class Article(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField()
    published_date = models.DateTimeField(auto_now_add=True,editable=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    category = TreeForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    main_image = models.ImageField(upload_to='article_images/',null=True, blank=True)
    publishing = models.BooleanField(default=False)


    def __str__(self):
        return self.title

