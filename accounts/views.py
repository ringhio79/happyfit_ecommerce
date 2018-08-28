from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm
from .models import Profile

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
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("events_list")
        else:
            return render(request, "accounts/profile_form.html", {"profile_form": profile_form})
            
    else:
        profile_form=ProfileForm()
        return render(request, "accounts/profile_form.html", {"profile_form": profile_form})

def user_profile(request):
    return render(request, "accounts/user_profile.html")