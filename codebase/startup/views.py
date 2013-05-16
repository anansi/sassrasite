# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404,render_to_response,RequestContext
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import UserCreateForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render_to_response
from accounts.models import UserProfile
from django.core.urlresolvers import reverse

def home(request):
    print 'home page requested'
    if request.method == "POST":
        print 'post received from home'
        #determine which form was 
        print 'req.items() %s'%request.items()

    reg_form = UserCreateForm()
    login_form = AuthenticationForm()
    return render(request, 'index.html',{'login_form':login_form})

def news(request):
    print 'news requested'
    template = loader.get_template('news.html')
 
    return render(request, 'news.html')

def newsletter(request):
    print 'newsletter requested'
    return render(request, 'sassra_newsletter.html')


def login_user(request):
    print 'login page requested'
    login_error=''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None: 
            print 'user detected therefore auth passed'
            if user.is_active:
                print 'user is active'
                auth_login(request, user)
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                print 'login failed disabled account'
        else:
            # Return an 'invalid login' error message.
            print 'login failed invalid login'
            login_error = 'Not a matching email address and password'
    return render(request, 'index.html',{'login_error':login_error})
    # return back to the normal home screen here and set error vars to display
    # also rewire that the startup.views is the call for login

def register(request):
    print 'register started in views.py'
    if request.method == 'POST':
        register_form = UserCreateForm(request.POST)


        print 'were in post'
        # print 'email valid: %s'%request.POST['email']
        # print 'first name: %s'%request.POST['first_name']
        # print 'last name: %s'%request.POST['last_name']
        #print 'password1 : %s'%request.POST['password1']
        #print 'password2 : %s'%request.POST['password2']

        # form.first_name = request.POST['first_name']
        # form.password1 = request.POST['password1']
        # form.password2 = request.POST['password2']
        # form.email = request.POST['email']
        

        register_form.username = "asdf"

        
        #print form.is_valid()
        register_error = 'asdf'
        
        if register_form.is_valid():
            #save the new user in the database but check if his email already exists
            print 'form first name %s'%register_form.cleaned_data['first_name']
            # try:
            user = User.objects.create_user(register_form.cleaned_data['email'], register_form.cleaned_data['email'],register_form.cleaned_data['password1'] )
            user.first_name = register_form.cleaned_data['first_name']
            user.last_name = register_form.cleaned_data['last_name']
            user.save()

            # except IntegrityError, e:
            #     print 'integrity exception'
            #     register_form.email.errors.append('a new error');
            #     return render(request, 'index.html', {'register_form': register_form,'register_error':register_error})
            #create a blank userprofile for the new user
            profile = UserProfile(user=user)
            profile.save()
            print 'logging user in'
            #log new user in
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
            #done. user now logged in. redirect to news page for introductions for the user
            print 'form being submitted'
            return HttpResponseRedirect(reverse('news'))
            print 'type is %s'%type(register_form.non_field_errors)
        print 'form errors %s'%register_form.non_field_errors
    else:
        register_form = UserCreateForm()
        print 'form created'
    
    return render(request, 'index.html', {'register_form': register_form,'register_error':register_error})