from django.contrib import admin
from accounts.models import UserProfile
from image_cropping import ImageCroppingMixin


from django import forms


class UserProfileAdmin(ImageCroppingMixin,admin.ModelAdmin):
    fieldsets = [
    	('User Profile for User', {'fields': ['user',]}),
        ('Personal information', {'fields': ['mobile','date_of_birth']}),
        ('Measurements and body specifics', {'fields': ['eye_colour','hair_colour','neck','weight','shoe_size','chest','bust','arm','head','back','waist','inner_leg','outer_leg','wrist','bicep','hips','ethnicity']}),
    	('Pictures', {'fields': ['image','cropping','test']}),
    ]
    list_display = ('username',)

admin.site.register(UserProfile,UserProfileAdmin)