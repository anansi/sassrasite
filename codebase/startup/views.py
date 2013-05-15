# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404,render_to_response,RequestContext
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import UserCreateForm

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
    return render(request, 'index.html',{'login_form':login_form})
    # return back to the normal home screen here and set error vars to display
    # also rewire that the startup.views is the call for login

