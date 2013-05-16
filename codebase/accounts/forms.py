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

    def clean_email(self):
        data = self.cleaned_data['email']
        print 'email is: :%s:'%data
        user = User.objects.get(email="new@mailie.com")#pk=email address
        print 'cleaning email - user is :%s:'%user
        if user is not None:
            raise forms.ValidationError("The email address is already registered")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return data
    
    class Meta:
        model = User
        fields = ( "email", "first_name", "last_name", "password1", "password2", )
        exclude = ['username',]
