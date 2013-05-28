# Create your views here.
from stuntperformers.admin import UserChangeForm 
from django.shortcuts import render, get_object_or_404,render_to_response,RequestContext
from django.contrib.auth import authenticate, login as auth_login, logout
from accounts.forms import UserCreateForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from accounts.models import UserProfile, CropPhotoTool
from django.template import Context, loader
from easy_thumbnails.files import get_thumbnailer
from example.models import Image
from accounts.forms import ImageForm, UserMeasurementsForm, UserContactForm
from django.contrib.auth.forms import AuthenticationForm
from easy_thumbnails.files import ThumbnailFile
from PIL import Image as PILImage
import re

def thumbnail_options(request):
    print 'user is %s'%request.user.email
    try:
        image = Image.objects.all()[0]
        print 'working image val: %s' %image.image_field
        up = UserProfile.objects.get(user=request.user)
        print 'userpro image val: %s' %up.image
        
        image = up.image
    except (Image.DoesNotExist, IndexError,):
        image = None
    return render(request, 'modelform_example.html', {'userProfile': up})

#local method for getting user profile photos
def photo_from_user_profile (image_id, user_profile):
    #image_id map:
    #1: front headshot pic
    #2: front 45' headshot pic
    #3: side headshot
    #4: back headshot
    #5: front full
    #6: front 45' full
    #7: side full
    #8: full back
    try:
        if image_id == 1:
            image = user_profile.front_headshot
        elif image_id == 2:
            image = user_profile.front_45_headshot
        if image == '':
            image = None
    except (Image.DoesNotExist, IndexError,):
        image = None
    return image


def cropPicture(request, image_id=None):
    #image_id map:
    #1: front headshot pic
    #2: front 45' headshot pic
    #3: side headshot
    #4: back headshot
    #5: front full
    #6: front 45' full
    #7: side full
    #8: full back
    if request.method != "POST":

        up = UserProfile.objects.get(user=request.user)
        image = photo_from_user_profile(1,up)

        print 'user is %s'%request.user.email
        print 'image_id is %s'%image_id
        
        for filename, file in request.FILES.iteritems():
            name = request.FILES[filename].name
            print 'value of uploaded image: %s'%name
        #check the userProfile to see if the user has already uploaded the photo
        up = UserProfile.objects.get(user=request.user)

        image = photo_from_user_profile(1,up)
        
        if image == None:
            #the image hasnt been uploaded
            print 'requested user profile image doesnt exist'        
            crop_photo_instance = CropPhotoTool()
            form = ImageForm(instance=crop_photo_instance)
            return render(request, 'accounts/modelform_example.html', {'form': form})        
        else:
            #the image exists
            print 'requested user profile image exists: %s'%image
            pass
        
    else: # request.method does == "POST":
        print 'save pressed'
        #obtain the images/objects from the form
        crop_photo_instance = CropPhotoTool()
        
        
        form = ImageForm(request.POST, request.FILES, instance=crop_photo_instance)

        if form.is_valid():
            print 'form valid'
            #determine if the initial upload was done, or if this was a cropping save call
            image = form.save()
            print 'image url %s'%form.cleaned_data['image']
            crop_photo_instance = CropPhotoTool(instance=image)
            form = ImageForm(request.POST, request.FILES, instance=crop_photo_instance)
            return render(request, 'accounts/modelform_example.html', {'form': form})

            #get the crop coordinates from the form
            # print 'cropping: %s'% form.cleaned_data['cropping']
            # #x1, y1, x2, y2 = form.cleaned_data['cropping'].split(',') 
            
            # #get the picture uploaded
            # print 'image url %s'%form.cleaned_data['image']
            # im = PILImage.open('media/casualPicturesCropTool/%s'%form.cleaned_data['image'])
            
            # #create the new image from the crop coordinates
            # #region = im.crop((int(x1),int(y1),int(x2),int(y2)))
            # #create the user email as id string
            # user_id = str(request.user.email)
            # #remove all non-alphanumeric keys (ie @ or . ) from the email so that it makes a safe foldername. also makes a distinct ID
            # user_id = re.sub(r'[^\w]', '', user_id)
            # #create the userId directory in profile_pictures
            # import os
            # dirname = 'media/profile_pictures/%s'%user_id
            # try:
            #     os.mkdir(dirname)
            # except OSError:
            #     pass #folder name already exists
            # #save the file
            # file_url = dirname+'/'+user_id+'_headshot_front'+'.jpeg'
            #region.save(file_url,"jpeg")
            

            
            
            #return HttpResponseRedirect(reverse('accounts:cropPicture', args=(image.pk,)))
        else:
            print 'form not valid'
    print 'cropPicture \'picture\' page loading'
    return render(request, 'accounts/modelform_example.html', {'form': form, 'crop_photo_instance': crop_photo_instance})

def profile(request):    
    return HttpResponseRedirect(reverse('home'))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def login_user(request):
    print 'login page requested'
    login_form = AuthenticationForm(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print 'user detected therefore auth passed'
            if user.is_active:
                print 'user is active'
                login(request, user)
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                print 'login failed disabled account'
        else:
            # Return an 'invalid login' error message.
            print 'login failed invalid login'
            login_form.is_valid()
    return HttpResponseRedirect(reverse('home'),{'login_form': login_form})



def viewProfile(request):
    userProfileI = UserProfile(user=request.user)
    print 'pic :%s:'%userProfileI.test

    #image = get_object_or_404(Image, pk=image_id)
    thumbnail_url = get_thumbnailer(userProfileI.test).get_thumbnail({
        'size': (430, 360),
        'box': userProfileI.cropping,
        'crop': False,
        'detail': False,
    }).url

    print 'thumbn %s'%thumbnail_url

    template = loader.get_template('accounts/picture.html')
    context = Context({
        'image': userProfileI,
    })
    return HttpResponse(template.render(context))

def stunt_profile_update_measurements(request):
    print 'meas update requested'
    userProfileI = UserProfile.objects.get(user=request.user)
    print 'arm is %s'%userProfileI.id
    
    measurements_form = UserMeasurementsForm(instance = userProfileI)
    return render(request, 'accounts/stunt_profile_update_measurements.html', {'measurements_form': measurements_form})

def stunt_profile_update_contact(request):
    print 'meas update requested' 
    userProfileI = UserProfile.objects.get(user=request.user)
    print 'arm is %s'%userProfileI.id
    
    contact_form = UserContactForm(instance = userProfileI)
    return render(request, 'accounts/stunt_profile_update_contact.html', {'contact_form': contact_form})


def stunt_profile(request):
    print 'stunt_profile requested from accounts.views'
    userProfileI = UserProfile.objects.get(user=request.user)
    print 'arm is %s'%request.POST.lists()
    
    measurements_form = UserMeasurementsForm(instance = userProfileI)
    contact_form = UserContactForm(instance=userProfileI)
    print 'contact form %s'%contact_form.__dict__
    if request.method == 'POST':
        print 'post received in accounts.stunt_profile'

        #determine if the form is the contact form, so we know which form to process
        if 'mobile' in request.POST:
            print 'contact found, called molder and skully'

            contact_form = UserContactForm(request.POST, instance = userProfileI)
            if contact_form.is_valid():
                print 'form is valid'            
                contact_form.save()
            else:
                print 'form not valid'            
                return render(request, 'accounts/stunt_profile_update_contact.html', {'measurements_form': measurements_form, 'contact_form':contact_form})
        else:
            
            measurements_form = UserMeasurementsForm(request.POST, instance = userProfileI)
            if measurements_form.is_valid():
                print 'form is valid'            
                measurements_form.save()
            else:
                print 'form is NOT valid'
                return render(request, 'accounts/stunt_profile_update_measurements.html', {'measurements_form': measurements_form, 'contact_form':contact_form})
        return render(request, 'accounts/stunt_profile.html', {'measurements_form': measurements_form, 'contact_form':contact_form})
    return render(request, 'accounts/stunt_profile.html', {'measurements_form': measurements_form, 'contact_form':contact_form})

