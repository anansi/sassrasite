# Create your views here.
from stuntperformers.admin import UserChangeForm 
from django.shortcuts import render, get_object_or_404,render_to_response,RequestContext
from django.contrib.auth import authenticate, login as auth_login, logout
from stuntperformers.admin import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.template import Context, loader
from easy_thumbnails.files import get_thumbnailer
from example.models import Image
from accounts.forms import ImageForm

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
    return HttpResponseRedirect(reverse('news'))

def logout_user(request):
    logout(request)
    return render(request, 'accounts/logged_out.html')

def login(request):
    return render(request, 'accounts/login.html')

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

def register(request):
    print 'register started in views.py'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        print 'were in post'
        print 'email valid: '
        print form.is_valid()
        if form.is_valid():
            print 'form first name %s'%form.cleaned_data['first_name']
            user = User.objects.create_user(form.cleaned_data['email'], form.cleaned_data['email'],form.cleaned_data['password1'] )
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            profile = UserProfile(user=user)
            profile.save()
            print 'logging user in'
            user = authenticate(username=request.POST['email'],password=request.POST['password1'])
            if user is not None:
                # the password verified for the user
                if user.is_active:
                   print("User is valid, active and authenticated")
                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
            auth_login (request,user)
            print 'form being submitted'
            return HttpResponseRedirect(reverse('news'))
    else:
        form = UserCreationForm()
        print 'form created'
    return render(request, 'accounts/register.html',{'form':form})
