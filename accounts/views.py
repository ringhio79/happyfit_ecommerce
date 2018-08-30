from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import ProfileForm
from payments.forms import CardForm
from .models import Profile
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def register(request):
    if request.method == 'POST':
        # Load the HTTP Request into two forms, for the User, and the Profile
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # Save the User object to DB, by calling save directly on the Form.
            # Return the User object so that we can use it later to set the user of the Profile.
            user = form.save()
            
            # Now we can log in as the new user 
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('add_profile')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', { 'form': form })

def add_profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES)
        card_form = CardForm(request.POST)
        print(card_form.is_valid())
        if profile_form.is_valid() and card_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            
            token=card_form.cleaned_data['stripe_id']
            customer = stripe.Customer.create(
                source=token,
                email='admin@example.com',
                )
            profile.stripe_id = customer.id
            profile.save()
            return redirect('events_list')
        else:
            print(card_form.errors)
            return render(request, "accounts/profile_form.html", {"profile_form": profile_form, "card_form": card_form, "publishable": settings.STRIPE_PUBLISHABLE_KEY})
            
    else:
        card_form = CardForm()
        profile_form=ProfileForm()
        return render(request, "accounts/profile_form.html", {"profile_form": profile_form, "card_form": card_form, "publishable": settings.STRIPE_PUBLISHABLE_KEY})

def user_profile(request):
    return render(request, "accounts/user_profile.html")
    
def edit_profile(request, id):
    profile = get_object_or_404(Profile, pk=id)
    
    if request.method == "POST":
        
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect("user_profile")
        else:
            return render(request, "accounts/profile_form.html", {"profile_form": profile_form})
            
    else:
        profile_form = ProfileForm(instance=profile)
        return render(request, "accounts/profile_form.html", {"profile_form": profile_form})
        
def subscriptions(request):
    return render (request, "accounts/subscriptions.html")
    
    
