from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import TerminForm
from .models import Termin

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # user_name = form.cleaned_data.get('user_name')
            messages.success(request, f'Account created')
            return redirect('index')
    else:
        form = UserCreationForm() #generation empty blank
    return render(request, 'default_users_app/register.html', {'form': form})

@login_required
def profile_user_view(request):
    return render(request, 'default_users_app/profile.html')

def termin(request):
    form_class = TerminForm
    form = form_class(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            autor_id = form_class.cleaned_data.get('user_name')
            status = request.POST.get('status')
            telefon = request.POST.get('telefon')
            kwota = request.POST.get('telefon')
            messages.success(request, f'Account created')
            return redirect('index')

    return render(request, 'default_users_app/termin.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.profile.bio = profile_form.cleaned_data.get('bio')
            user.profile.location = profile_form.cleaned_data.get('location')
            user.profile.save()
def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            profile_form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = user_form.cleaned_data.get('birth_date')
            user.save()
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')