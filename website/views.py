from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from .models import Event, Profile
from django.contrib.auth.models import User


def index(request):
    latest_event_list = Event.objects.order_by('pub_date')[:5]
    template = loader.get_template('website/index.html')
    context = {
        'latest_event_list': latest_event_list,
    }
    return HttpResponse(template.render(context, request))

def events(request):
    event_list = Event.objects.order_by('pub_date')
    template = loader.get_template('website/events.html')
    context = {
        'event_list': event_list,
    }
    return HttpResponse(template.render(context, request))

def event(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    return render(request, 'website/event.html', {'event': event})

def about(request):
    members_list = Profile.objects.all()
    template = loader.get_template('website/about.html')
    context = {
        'members': members_list
    }
    return HttpResponse(template.render(context,request))

def curriculum(request,user_id):
    try:
        user = User.objects.get(pk=user_id)
    except Event.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'website/curriculum.html', {'user': user})