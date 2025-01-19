from django.db import models
from core.models import PublishedModel
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(PublishedModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)

class Location(PublishedModel):
    name = models.CharField(max_length=256)

class Post(PublishedModel):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)





