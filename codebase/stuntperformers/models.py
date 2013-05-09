from django.db import models

from polls.models import Poll


class SASSRAUser(models.Model):
    email = models.EmailField(unique=True,db_index=True,verbose_name='email address')
    first_name = models.CharField(max_length=15)
    last_name =models.CharField(max_length=15)
    #AbstractBaseUser required fields
    
    REQUIRED_FIELDS = ['first_name', 'last_name']#['height','date_of_birth','eye_colour']
    mobile = models.CharField(max_length=10)   
    
    #user traits    
    date_of_birth = models.DateField(default='2110-10-10')
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
    ethnicity = models.CharField(max_length=15)

    has_voted_one = models.CharField(max_length=2,default='N')
    has_voted_two = models.CharField(max_length=2,default='N')
    polls = models.ManyToManyField(Poll)

    


# Create your models here.
class stuntperformer(models.Model):
	
    date_of_birth = models.DateField(default=0)
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
    ethnicity = models.CharField(max_length=15)
    
    


