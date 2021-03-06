# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from polls.models import Poll
from django.template import Context, loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404,render_to_response,RequestContext
from polls.models import Choice
from django.core.urlresolvers import reverse
from django import forms
from stuntperformers.admin import UserCreationForm
from stuntperformers.models import stuntperformer



def index(request):
    
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('stuntperformers/index.html')
    context = Context({
        'latest_poll_list': latest_poll_list,
    })
    return render(request, 'stuntperformers/test.html')

# def home(request):
# 	return render(request, 'stuntperformers/test.html')


# class UserCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

#     class Meta:
#         model = stuntperformer
#         fields = ('email', 'first_name', 'last_name')

#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user

def home(request):
    print 'home requested'
    
    template = loader.get_template('index.html')
    
    return render(request, 'index.html')

def news(request):
    print 'news requested'
    
    template = loader.get_template('news.html')
 
    return render(request, 'news.html')

def newsletter(request):
    print 'newsletter requested'
    return render(request, 'sassra_newsletter.html')

def vote(request):
    p = get_object_or_404(Poll, pk=1)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'stuntperformers/index.html')

