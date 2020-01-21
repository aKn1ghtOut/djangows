from django.db import models

# Create your models here.
class Article(models.Model):
    id=models.PositiveIntegerField()
    title=models.TextField()
    body=models.TextField()
    time=models.DateTimeField()