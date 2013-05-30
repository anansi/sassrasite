from django.db import models
from django.contrib.auth.models import User
from polls.models import Poll
from image_cropping.fields import ImageRatioField, ImageCropField

# Create your models here.
class UserProfile(models.Model):
    #the referential user object
    user = models.OneToOneField(User, unique=True)

    #the polls that the user has already voted on
    polls_voted = models.ManyToManyField(Poll)
    #profile pic - the standard one
    front_headshot =  models.ImageField(upload_to='casualPicturesCropTool',null=True)
    front_45_headshot = models.ImageField(upload_to='casualPicturesCropTool',null=True)
    side_headshot = models.ImageField(upload_to='casualPicturesCropTool',null=True)
    back_of_headshot = models.ImageField(upload_to='casualPicturesCropTool',null=True)
    front_full_body = models.ImageField(upload_to='casualPicturesCropTool',null=True)
    front_45_full_body = models.ImageField(upload_to='casualPicturesCropTool',null=True)
    side_full_body = models.ImageField(upload_to='casualPicturesCropTool',null=True)
    back_of_full_body = models.ImageField(upload_to='casualPicturesCropTool',null=True)

    # size is "width x height"

    mobile = models.CharField(max_length=10)   
    
    WHITE = 'WH'
    COLOURED = 'CO'
    BLACK = 'BL'
    ASIAN = 'AS'
    INDIAN = 'IN'
    RACE_CHOICES = (
        (WHITE, 'White'),
        (COLOURED, 'Coloured'),
        (BLACK, 'Black'),
        (INDIAN, 'Indian'),
        (ASIAN, 'Asian'),
    )


    #user traits    
    date_of_birth = models.DateField(default='1992-10-10')
    height = models.IntegerField(default=0)
    eye_colour = models.CharField(max_length=15)
    background = models.CharField(max_length=200)
    hair_colour = models.CharField(max_length=15)
    neck = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    shoe_size = models.IntegerField(default=0)
    chest = models.IntegerField(default=0)
    bust = models.IntegerField(default=0)
    arm = models.IntegerField(default=0)
    head = models.IntegerField(default=0)
    back = models.IntegerField(default=0)
    waist = models.IntegerField(default=0)
    inner_leg = models.IntegerField(default=0)
    outer_leg = models.IntegerField(default=0)
    wrist = models.IntegerField(default=0)
    bicep = models.IntegerField(default=0)
    hips = models.IntegerField(default=0)

    ethnicity = models.CharField(max_length=2,
                                      choices=RACE_CHOICES,
                                      default=WHITE)
    def username(self):
    	if self.user.first_name == '':
    	    if self.user.email == '':
                return self.user.username
            else:
                return self.user.email

    	else:
    		return self.user.first_name + ' ' + self.user.last_name 

    def email(self):
        return self.user.username


class CropPhotoTool(models.Model):
    #The Field that allows you to crop an image
    image = ImageCropField( upload_to='casualPicturesCropTool')
    
    # size is "width x height"
    cropping = ImageRatioField('image', '420x500', size_warning=True)
    class Meta:
        app_label = 'accounts'

