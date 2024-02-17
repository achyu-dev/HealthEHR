from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    age = models.IntegerField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")



class NLPModel:
    @staticmethod
    def process(file):
        # Process the file here
        return "NLP Result"


class DIPModel:
    @staticmethod
    def process(file):
        # Process the file here
        return True


class UploadedFile(models.Model):
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    illness = models.CharField(max_length=500)
    file1 = models.FileField(upload_to='uploads/')
    file2 = models.FileField(upload_to='uploads/')
    # NLPresult = models.ForeignKey(NLPModel, on_delete=models.CASCADE, null=True)
    # DIPresult = models.ForeignKey(DIPModel, on_delete=models.CASCADE, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name.name

