from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email


class Tag(models.Model):
    name=models.CharField(max_length=255, blank =True)

class Priority(models.TextChoices):
    pass


class Note(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField(blank=True)
    noteuser=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tag=models.ManyToManyField(Tag, blank=True, related_name='notes')
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created']
        indexes=[ models.Index(fields=['-created'])]

    def __str__(self):
        return self.title