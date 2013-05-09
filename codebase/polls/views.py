# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from polls.models import Poll
from django.template import Context, loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from polls.models import Choice
from django.core.urlresolvers import reverse
from accounts.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    print latest_poll_list
    template = loader.get_template('polls/index.html')
    context = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))

def detail(request, poll_id):
    print 'exec detail'
    p = get_object_or_404(Poll, pk=poll_id)
    user = request.user
    hasVoted = True
    print 'has_voted_one:'
    
    try:
        profile = UserProfile.objects.get(userObject=user)
    except ObjectDoesNotExist:
        profile = UserProfile(userObject=user)
        profile.save()
        print 'created profile for user'
    
    #hasVotedOnPoll = p in pollsVoted.objects.get(pk=1)
    print profile.pollsVoted.all()
    hasVotedOnPoll = True
    try:
        profile.pollsVoted.get(pk=poll_id)
    except ObjectDoesNotExist:
        hasVotedOnPoll=False
        print 'caught exc and hasvoted=false'
    print 'hasVotedOnPoll'
    print hasVotedOnPoll

    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': poll, 'hasAlreadyVoted':hasVotedOnPoll})

def results(request, poll_id):
    #note that the user has voted 
    print "poll id is:"
    # print poll_id
    # print type(poll_id)
    # user = request.user
    # print 'poles for user:'
    # print user.poles.all()
    # print type(user.poles.all())
    # queryset = user.poles.all().filter(poll_id = poll_id)
    # print "queryset"
    # print queryset
    #poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})
    
def vote(request, poll_id):
    #note that the user has voted 
    print "poll id is:"
    print poll_id
    print type(poll_id)
    user = request.user
    print 'poles for user:'
    
    profile = UserProfile.objects.get(userObject=user)

    

    poll = get_object_or_404(Poll, pk=poll_id)
    profile.pollsVoted.add(poll)

    #print type(user.polls.all())
    
    p = get_object_or_404(Poll, pk=poll_id)
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


        if poll_id != u'2':
            user.has_voted_one = 'Y'
            print 'poll 1 voted on'
        else:
            user.has_voted_two = 'Y'
            print 'poll 2 voted on'
        
        user.save()
        profile.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))