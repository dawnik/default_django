from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('user_name')
            messages.success(request, f'Account created')
            return redirect('index')
    else:
        form = UserCreationForm() #generation empty blank
    return render(request, 'default_users_app/register.html', {'form': form})