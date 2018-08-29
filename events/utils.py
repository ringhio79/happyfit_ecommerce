from .models import Ticket

def create_ticket(user_id, event_id, first_name, last_name):
    
    ticket = Ticket(first_name =first_name, last_name = last_name, member_id= user_id, event_id= event_id)
    ticket.save()