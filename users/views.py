from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():     ## Django performs backend checks
            form.save()
            username = form.cleaned_data.get('username') ## validated username will store in "cleaned_data" dictionary
            messages.success(request, f"Your account has been created! You are now able to log in")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})