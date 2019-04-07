from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


# for user registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('Sentiment-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# for user profile & user must need to be logged in
@login_required
def profile(request):
    return render(request, 'users/profile.html')