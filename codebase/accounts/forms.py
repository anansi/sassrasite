from django import forms
from accounts.models import UserProfile


class ImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image','cropping')

