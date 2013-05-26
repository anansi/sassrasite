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
    image = ImageCropField( upload_to='casualPictures')
    test = models.ImageField(upload_to='testpics')
    
    # size is "width x height"
    cropping = ImageRatioField('image', '430x360')
    class Meta:
        app_label = 'accounts'

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


    