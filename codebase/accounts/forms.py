from django import forms
from accounts.models import CropPhotoTool, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class ImageForm(forms.ModelForm):
    class Meta:
        model = CropPhotoTool#the old model was directly using: UserProfile
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
        #test if the database already has this email address 
        #registered. if so, raise exception

        #1: try find a User from the database with this email
        try:
            user = User.objects.get(email=data)#pk=email address
        except User.DoesNotExist:
            user = None
        
        #if the user exists raise error
        if user is not None:
            raise forms.ValidationError("The email address is already registered")
        #else return the data as normal

        # Always return the cleaned data, whether you have changed it or
        # not.
        return data
    
    class Meta:
        model = User
        fields = ( "email", "first_name", "last_name", "password1", "password2", )
        exclude = ['username',]

class UserMeasurementsForm(ModelForm):

    def __init__(self, *args, **kwargs): 
        super(ModelForm, self).__init__(*args, **kwargs) 
        # remove username
        #self.fields.pop('user')

    class Meta:
        model = UserProfile
        fields = ('eye_colour','hair_colour','neck','height', 'weight','shoe_size','chest','bust','arm','head','back','waist','inner_leg','outer_leg','wrist','bicep','hips','ethnicity')
        
class UserContactForm(ModelForm):

    def __init__(self, *args, **kwargs): 
        super(ModelForm, self).__init__(*args, **kwargs) 
        # remove username
        #self.fields.pop('user')

    class Meta:
        model = UserProfile
        fields = ('mobile',)

