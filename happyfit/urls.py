"""happyfit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.conf import settings
from events.views import home, events_list, event_details, event_booking, event_booking_confirm
from django.urls import path, reverse_lazy
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from accounts.views import register, add_profile, user_profile, edit_profile, subscriptions, subscribe, unsubscribe,view_subscription
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('events', events_list, name="events_list"),
    path('<int:id>', event_details, name="event_details"),
    path('event/book', event_booking, name="event_booking"),
    path('event/confirmation', event_booking_confirm, name="booking_confirmation"),
    

    
    path('accounts/register/', register, name='register'),
    path('accounts/login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    path('accounts/logout/', logout, name='logout'),
    path('accounts/password-reset/', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done'), 'template_name': 'accounts/password_reset_form.html'}, name='password_reset'),
    path('accounts/password-reset/done/', password_reset_done, {'template_name': 'accounts/password_reset_done.html'}, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete'), 'template_name': 'accounts/password_reset_confirm.html'}, name='password_reset_confirm'),
    path('accounts/password-reset/complete/', password_reset_complete, {'template_name': 'accounts/password_reset_complete.html'}, name='password_reset_complete'),
    
    path('accounts/profile_form/', add_profile, name='add_profile'),
    path('accounts/profile/', user_profile, name='user_profile'),
    path('accounts/edit_profile/<int:id>', edit_profile, name='edit_profile'),
    path('subscriptions', subscriptions, name='subscriptions'),
    path('subscribe', subscribe, name='subscribe'),
    path('unsubscribe', unsubscribe, name='unsubscribe'),
    path('view_subscription', view_subscription, name='view_subscription'),
    
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
