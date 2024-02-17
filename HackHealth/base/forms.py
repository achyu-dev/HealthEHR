from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, UploadedFile


class UploadForm(ModelForm):
    class Meta:
        model = UploadedFile
        fields = '__all__'


class FileUploadForm(ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file1', 'file2']


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email']
