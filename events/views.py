from django.shortcuts import render, get_object_or_404
from .models import Event


# Create your views here.
def events_list(request):
    events = Event.objects.all()
    return render(request, "events/events_list.html", {'events': events})

def event_details(request, id):
    event = get_object_or_404(Event, pk=id)
    return render(request, "events/event_details.html", {"event": event})
