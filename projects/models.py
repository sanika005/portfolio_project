from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 100)
    desc = models.TextField(max_length = 500)
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")