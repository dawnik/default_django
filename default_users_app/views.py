from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    form = UserCreationForm()
    return render(request, 'default_users_app/register.html', {'form': form})