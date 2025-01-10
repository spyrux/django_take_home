from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name


class Product(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return self.name


