from django.shortcuts import render, get_object_or_404
from .models import Event


# Create your views here.
def events_list(request):
    events = Event.objects.all()
    return render(request, "events/events_list.html", {'events': events})

def event_details(request, id):
    event = get_object_or_404(Event, pk=id)
    return render(request, "events/event_details.html", {"event": event})
    
def event_booking(request):
    id = request.GET["id"]
    event = get_object_or_404(Event, pk=id)
    quantity = int(request.GET["quantity"])
    tickets = range(1, quantity + 1)
    return render(request, "events/event_booking.html", {"tickets": tickets, "event": event, "quantity": quantity})
    
