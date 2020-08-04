from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=1000)


class Item(models.Model):
    name = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
