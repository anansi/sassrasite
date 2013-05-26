# Create your views here.
from stuntperformers.admin import UserChangeForm 
from django.shortcuts import render, get_object_or_404,render_to_response,RequestContext
from django.contrib.auth import authenticate, login as auth_login, logout
from accounts.forms import UserCreateForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.template import Context, loader
from easy_thumbnails.files import get_thumbnailer
from example.models import Image
from accounts.forms import ImageForm, UserMeasurementsForm, UserContactForm
from django.contrib.auth.forms import AuthenticationForm

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

def cropPicture(request, image_id=None):
    print 'user is %s'%request.user.email
    print 'image_id is %s'%image_id
    for filename, file in request.FILES.iteritems():
        name = request.FILES[filename].name
        print 'value of uploaded image: %s'%name
    try:
        image = Image.objects.all()[0]
        print 'working image val: %s' %image.image_field
        up = UserProfile.objects.get(user=request.user)
        print 'userpro image val: %s' %up.image
        image = up.image
    except (Image.DoesNotExist, IndexError,):
        image = None
    form = ImageForm(instance=up)
    if request.method == "POST":
        print 'save pressed'
        form = ImageForm(request.POST, request.FILES, instance=up)
        if form.is_valid():
            print 'form valid'
            image = form.save()
            return HttpResponseRedirect(reverse('accounts:cropPicture', args=(image.pk,)))
    print 'cropPicture \'picture\' page loading'
    return render(request, 'accounts/modelform_example.html', {'form': form, 'up': up})

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

