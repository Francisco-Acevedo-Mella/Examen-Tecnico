
from pickle import TRUE
from django.db import models



class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=TRUE)
    description =  models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=TRUE)
    updated_at = models.DateTimeField(auto_now_add=True, null=TRUE)
    