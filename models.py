from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(('email address'), unique=True)
    document = models.FileField()
    objects = models.Manager()
    def __str__(self):
        return self.document

