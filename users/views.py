from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required ## checks whether user is logged in, if not, cannot access certain pages(profile in our case)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # Django performs backend checks
            form.save()
            # validated username will store in "cleaned_data" dictionary
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Your account has been created! You are now able to log in")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required ## decorators - adds functionality to an existing function 
def profile(request):
    return render(request, 'users/profile.html')
