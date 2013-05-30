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
from image_cropping.fields import ImageRatioField

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
def photo_from_user_profile (image_id, user_profile, file_url=None,image_on_disk_to_save=None):
    #image_id map:
    #1: front headshot pic
    #2: front 45' headshot pic
    #3: side headshot
    #4: back headshot
    #5: front full
    #6: front 45' full
    #7: side full
    #8: full back
    print 'entered photo_from_user_profile %s'%image_id
    image = None
    try:
        if image_id == '1':
            if file_url:
                #define the relivant string for updating 'headshot front'
                file_name = '_headshot_front'
                #print the data for clarity
                print 'saving user profile for '+file_name
                print file_url+file_name+'.jpeg'
                #save the data
                image_on_disk_to_save.save('media/'+file_url+file_name+'.jpeg',"jpeg")
                user_profile.front_headshot = file_url+file_name+'.jpeg'
                user_profile.save()
            image = user_profile.front_headshot
        elif image_id == '2':
            if file_url:
                #define the relivant string for updating 
                file_name = '_headshot_45_front'
                #print the data for clarity
                print 'saving user profile for '+file_name
                print file_url+file_name+'.jpeg'
                #save the data
                image_on_disk_to_save.save('media/'+file_url+file_name+'.jpeg',"jpeg")
                user_profile.front_45_headshot = file_url+file_name+'.jpeg'
                user_profile.save()
            image = user_profile.front_45_headshot
        elif image_id == '3':
            if file_url:
                #define the relivant string for updating 
                file_name = '_side_headshot'
                #print the data for clarity
                print 'saving user profile for '+file_name
                print file_url+file_name+'.jpeg'
                #save the data
                image_on_disk_to_save.save('media/'+file_url+file_name+'.jpeg',"jpeg")
                user_profile.side_headshot = file_url+file_name+'.jpeg'
                user_profile.save()
            image = user_profile.side_headshot
        elif image_id == '4':
            if file_url:
                file_name = '_back_of_headshot'#define the relivant string for updating 
                #print the data for clarity
                print 'saving user profile for '+file_name
                print file_url+file_name+'.jpeg'
                #save the data
                image_on_disk_to_save.save('media/'+file_url+file_name+'.jpeg',"jpeg")
                #save the userprofile
                user_profile.back_of_headshot = file_url+file_name+'.jpeg'
                user_profile.save()
            image = user_profile.back_of_headshot
        elif image_id == '5':
            if file_url:
                file_name = '_front_full_body'#define the relivant string for updating 
                #print the data for clarity
                print 'saving user profile for '+file_name
                print file_url+file_name+'.jpeg'
                #save the data
                image_on_disk_to_save.save('media/'+file_url+file_name+'.jpeg',"jpeg")
                #save the userprofile
                user_profile.front_full_body = file_url+file_name+'.jpeg'
                user_profile.save()
            image = user_profile.front_full_body
        elif image_id == '6':
            if file_url:
                file_name = '_front_45_full_body'#define the relivant string for updating 
                #print the data for clarity
                print 'saving user profile for '+file_name
                print file_url+file_name+'.jpeg'
                #save the data
                image_on_disk_to_save.save('media/'+file_url+file_name+'.jpeg',"jpeg")
                #save the userprofile
                user_profile.front_45_full_body = file_url+file_name+'.jpeg'
                user_profile.save()
            image = user_profile.front_45_full_body
        elif image_id == '7':
            if file_url:
                file_name = '_side_full_body'#define the relivant string for updating 
                #print the data for clarity
                print 'saving user profile for '+file_name
                print file_url+file_name+'.jpeg'
                #save the data
                image_on_disk_to_save.save('media/'+file_url+file_name+'.jpeg',"jpeg")
                #save the userprofile
                user_profile.side_full_body = file_url+file_name+'.jpeg'
                user_profile.save()
            image = user_profile.side_full_body
        elif image_id == '8':
            if file_url:
                file_name = '_back_of_full_body'#define the relivant string for updating 
                #print the data for clarity
                print 'saving user profile for '+file_name
                print file_url+file_name+'.jpeg'
                #save the data
                image_on_disk_to_save.save('media/'+file_url+file_name+'.jpeg',"jpeg")
                #save the userprofile
                user_profile.back_of_full_body = file_url+file_name+'.jpeg'
                user_profile.save()
            image = user_profile.back_of_full_body

        if image == '':
            image = None


    except (Image.DoesNotExist, IndexError,):
        image = None
    return image

first_hit_on_cropPicture_from_profile_screen = None
cropInstance = None

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

    if first_hit_on_cropPicture_from_profile_screen is None:
        global first_hit_on_cropPicture_from_profile_screen    
        first_hit_on_cropPicture_from_profile_screen = image_id
        image = get_object_or_404(CropPhotoTool, pk=0) 
        print 'hit first time'
    else:
        print 'done itting first time %s'%first_hit_on_cropPicture_from_profile_screen
        image = get_object_or_404(CropPhotoTool, pk=image_id) if image_id else None
        CropPhotoTool.cropping = ImageRatioField('image', '420x800', size_warning=True)
    print 'cropPicture view started: image is: |%s|'%image
    if request.method != "POST":

        up = UserProfile.objects.get(user=request.user)
        print 'user is %s'%request.user.email
        print 'image_id is %s'%image_id
        
        for filename, file in request.FILES.iteritems():
            name = request.FILES[filename].name
            print 'value of uploaded image: %s'%name
        #check the userProfile to see if the user has already uploaded the photo
        
        profile_image = photo_from_user_profile(first_hit_on_cropPicture_from_profile_screen,up)
        print 'profile image is: %s'%profile_image
        # if image == None:
        #     #the image hasnt been uploaded
        #     print 'requested user profile image doesnt exist'        
        #     crop_photo_instance = CropPhotoTool()
        #     form = ImageForm(instance=crop_photo_instance)
        #     return render(request, 'accounts/modelform_example.html', {'form': form})
        # else:
        #     #the image exists
        #     print 'requested user profile image exists: %s'%image
        #     pass
        
        form = ImageForm(instance=image)
        return render(request, 'accounts/modelform_example.html', {'form': form, 'image': image})
    else: # request.method does == "POST":
        print 'button pressed'
        print 'image id in post %s'%image_id
        #obtain the images/objects from the form
        crop_photo_instance = get_object_or_404(CropPhotoTool, pk=first_hit_on_cropPicture_from_profile_screen) if first_hit_on_cropPicture_from_profile_screen else None
        
        form = ImageForm(request.POST, request.FILES, instance=crop_photo_instance)
        
        if form.is_valid():
            print 'form valid'
            #determine if the initial upload was done, or if this was a cropping save call
            image = form.save()

            print 'image url %s'%form.cleaned_data['image']
            print 'image id %s'%image.id
            #image = get_object_or_404(Image, pk=image.id) if image.id else None

            if 'preview' in request.POST:
                print 'save was in reequest.possssssssssssssst'    
            else:
                #the 'keep photo' button was pressed
                print 'keep photo pressed!'
                #get the crop coordinates from the form
                print 'cropping: %s'% form.cleaned_data['cropping']
                x1, y1, x2, y2 = form.cleaned_data['cropping'].split(',') 
                
                #get the picture uploaded
                print 'image url %s'%form.cleaned_data['image']
                im = PILImage.open('media/%s'%form.cleaned_data['image'])
                
                #create the new image from the crop coordinates
                region = im.crop((int(x1),int(y1),int(x2),int(y2)))
                #create the user email as id string
                user_id = str(request.user.email)
                #remove all non-alphanumeric keys (ie @ or . ) from the email so that it makes a safe foldername. also makes a distinct ID
                user_id = re.sub(r'[^\w]', '', user_id)
                #create the userId directory in profile_pictures
                import os
                dirname = 'profile_pictures/%s'%user_id
                try:
                    os.mkdir('media/'+dirname)
                except OSError:
                    pass #folder name already exists
                #save the file to the right 
                
                file_url = dirname+'/'+user_id
                print 'saving time'
                print 'file_url %s'%file_url
                
                up = UserProfile.objects.get(user=request.user)
                image_for_profile = photo_from_user_profile(first_hit_on_cropPicture_from_profile_screen,up,file_url,region)
                print 'im_fo_pr %s'%image_for_profile
                first_hit_on_cropPicture_from_profile_screen = None

                crop_photo_instance = get_object_or_404(CropPhotoTool, pk=0)
                image.image = crop_photo_instance.image
                image.save()

                return HttpResponseRedirect(reverse('accounts:stunt_profile'))

                
            return HttpResponseRedirect(reverse('accounts:cropPictureA', args=(first_hit_on_cropPicture_from_profile_screen,)))

        else:
            print 'form not valid'
    return render(request, 'accounts/modelform_example.html', {'form': form})

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
                return render(request, 'accounts/stunt_profile_update_contact.html', {'measurements_form': measurements_form, 'contact_form':contact_form, 'userProfileI':userProfileI})
        else:

            measurements_form = UserMeasurementsForm(request.POST, instance = userProfileI)
            if measurements_form.is_valid():
                print 'form is valid'            
                measurements_form.save()
            else:
                print 'form is NOT valid'
                return render(request, 'accounts/stunt_profile_update_measurements.html', {'measurements_form': measurements_form, 'contact_form':contact_form, 'userProfileI':userProfileI})
        return render(request, 'accounts/stunt_profile.html', {'measurements_form': measurements_form, 'contact_form':contact_form, 'userProfileI':userProfileI})
    return render(request, 'accounts/stunt_profile.html', {'measurements_form': measurements_form, 'contact_form':contact_form, 'userProfileI':userProfileI})

