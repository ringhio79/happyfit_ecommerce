from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import ProfileForm, UserRegForm
from payments.forms import CardForm
from .models import Profile
from django.conf import settings
import datetime
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('add_profile')
    else:
        form = UserRegForm()
    return render(request, 'accounts/register.html', { 'form': form })

def add_profile(request):
    redirect_to = request.GET.get('next', '/')
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES)
        card_form = CardForm(request.POST)
        
        if profile_form.is_valid() and card_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            
            token=card_form.cleaned_data['stripe_id']
            customer = stripe.Customer.create(
                source=token,
                email=request.user.email,
                )
            profile.stripe_id = customer.id
            profile.save()
            return redirect(redirect_to)
            
        else:
            return render(request, "accounts/profile_form.html", {"profile_form": profile_form, "card_form": card_form, "publishable": settings.STRIPE_PUBLISHABLE_KEY})
            
    else:
        card_form = CardForm()
        profile_form=ProfileForm()
        return render(request, "accounts/profile_form.html", {"profile_form": profile_form, "card_form": card_form, "publishable": settings.STRIPE_PUBLISHABLE_KEY})

def user_profile(request):
    try:
        hasattr ("request.user", "profile")
        membership_no = "%05d" % request.user.profile.id
        subscription = stripe.Subscription.retrieve(request.user.profile.subscription_id)
        end_date_str = subscription.current_period_end
        end_date = datetime.datetime.fromtimestamp(float(end_date_str))
        return render(request, "accounts/user_profile.html", {"membership_no": membership_no, "subscription":subscription, "end_date":end_date})
    except:
        return render(request, "accounts/user_profile.html")
    
def edit_profile(request, id):
    profile = get_object_or_404(Profile, pk=id)
    
    if request.user.profile.id != profile.id:
        return HttpResponse("You are not authorised to view this page")
    else:
        if request.method == "POST":
            
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
            card_form = CardForm(request.POST)
            if profile_form.is_valid() and card_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = request.user
                
                token=card_form.cleaned_data['stripe_id']
                customer = stripe.Customer.create(
                    source=token,
                    email=request.user.email,
                    )
                profile.stripe_id = customer.id
                profile.save()
                return redirect("user_profile")
            else:
                return render(request, "accounts/profile_form.html", {"profile_form": profile_form, "card_form": card_form, "publishable": settings.STRIPE_PUBLISHABLE_KEY})
                
                
        else:
            profile_form = ProfileForm(instance=profile)
            card_form = CardForm()
            return render(request, "accounts/profile_form.html", {"profile_form": profile_form, "card_form": card_form, "publishable": settings.STRIPE_PUBLISHABLE_KEY})
        
def subscriptions(request):
    return render(request, "accounts/subscriptions.html")
    
def subscribe(request):
    
    if request.method == "POST":
        plan = request.POST['plan']
        
        print(request.user.profile.stripe_id)
        
        subscription = stripe.Subscription.create(
          customer=request.user.profile.stripe_id,
          items=[{'plan': plan}],
        )
        request.user.profile.subscription_id = subscription.id
        request.user.profile.save()
        return redirect('events_list')
    else:
        return render(request, 'checkout/subscribe.html')
    
def unsubscribe(request):
    stripe.Subscription.modify(request.user.profile.subscription_id, cancel_at_period_end=True)
    return redirect('user_profile')

def view_subscription(request):
    subscription = stripe.Subscription.retrieve(request.user.profile.subscription_id)
    return render(request, "accounts/view_subscription.html", {'subscription': subscription})
