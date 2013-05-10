# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404,render_to_response,RequestContext

def home(request):
    print 'home requested'
    if request.method == "POST":
        print 'post received from home'
        #determine which form was 
        print 'req.items() %s'%request.items()

    return render(request, 'landing_page.html')

def news(request):
    print 'news requested'
    template = loader.get_template('news.html')
 
    return render(request, 'news.html')

def newsletter(request):
    print 'newsletter requested'
    return render(request, 'sassra_newsletter.html')
