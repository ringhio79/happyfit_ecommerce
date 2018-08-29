from django.shortcuts import render, get_object_or_404
from .models import Event, Ticket
from .utils import create_ticket


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
    tickets = range(1, quantity)
    grand_total = event.price * quantity
    return render(request, "events/event_booking.html", {"tickets": tickets, "event": event, "quantity": quantity, "grand_total": grand_total})

def event_booking_confirm(request):
    member = request.POST['user_id']
    event = request.POST['id']
    quantity = int(request.POST["ticket_quantity"])
    guests = range(1, quantity)
    
    create_ticket(member, event, "Annie", "Admin" )
    for guest in guests:
       
        first_name = request.POST['first_name_'+str(guest)]
        last_name = request.POST['last_name_'+str(guest)]
      
        create_ticket(member, event, first_name, last_name )
        
    return render(request, "events/booking_confirmation.html")


