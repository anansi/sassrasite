from django import forms
from accounts.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image','cropping')


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=30)
    # username = forms.CharField(required=True, max_length=30)

    def __init__(self, *args, **kwargs): 
        super(UserCreationForm, self).__init__(*args, **kwargs) 
        # remove username
        self.fields.pop('username')

    class Meta:
        model = User
        fields = ( "email", "first_name", "last_name", "password1", "password2", )
        exclude = ['username',]
