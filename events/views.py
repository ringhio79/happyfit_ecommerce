from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Ticket, Booking
from .utils import create_ticket
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .filters import CategoryFilter
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY



# Create your views here.
def class_schedule(request):
    return render(request, "events/class_schedule.html")

def events_list(request):
    events_list = Event.objects.all()
    category_filter = CategoryFilter(request.GET, queryset=events_list)
    return render(request, "events/events_list.html", {'filter': category_filter, 'events': events_list})


def event_details(request, id):
    event = get_object_or_404(Event, pk=id)
    tickets = Ticket.objects.filter(event=event)
    available = event.capacity - len(tickets)
    
    can_book = available >=1
    
    return render(request, "events/event_details.html", {"event": event, "available": available, "can_book": can_book})
    
@login_required()
def event_booking(request):
    id = request.GET["id"]
    event = get_object_or_404(Event, pk=id)
    quantity = int(request.GET["quantity"])
    tickets = range(1, quantity)
    grand_total = event.price * quantity
    return render(request, "events/event_booking.html", {"tickets": tickets, "event": event, "quantity": quantity, "grand_total": grand_total})

# ------------create tickets and booking --------------


def event_booking_confirm(request):
    if request.method == "GET":
        return redirect('/')
    
    else:
        member = request.POST['user_id']
        event = request.POST['id']
        quantity = int(request.POST["ticket_quantity"])
        guests = range(1, quantity)
        member_first_name = request.user.profile.first_name
        member_last_name = request.user.profile.last_name
        subscription = stripe.Subscription.retrieve(request.user.profile.subscription_id)
        total_in_cent = int(float(request.POST["grand_total"]))*100
        
        charge = stripe.Charge.create(
            amount=total_in_cent,
            currency='EUR',
            customer=request.user.profile.stripe_id,
            )
        
        if charge.paid:
            booking= Booking(booking_member_id=member)
            booking.save()
            booking_no = "%05d" % booking.id

            create_ticket(member, event, member_first_name, member_last_name, booking)
            for guest in guests:
               
                first_name = request.POST['first_name_'+str(guest)]
                last_name = request.POST['last_name_'+str(guest)]
              
                create_ticket(member, event, first_name, last_name, booking)

            return render(request, "events/booking_confirmation.html", {"member_first_name": member_first_name, "member_last_name": member_last_name, "quantity": quantity, "event":event, "booking_no": booking_no})
        
        else:
            message = "Charge Not Paid"
            return render(request, "home/custom_error.html", {"message":message})

def booking_details(request, id):
    booking = get_object_or_404(Booking, pk=id)
    if request.user != booking.booking_member:
        message="You are not authorised to view this page."
        return render(request, "home/custom_error.html", {"message":message})
    else:
        booking_no = "%05d" % booking.id
        tickets = Ticket.objects.filter(booking=booking)
        
        return render(request, "events/booking_details.html", {"booking": booking, "booking_no": booking_no, "tickets": tickets})
    
    
    


