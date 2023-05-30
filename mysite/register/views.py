from .forms import RegisterForm, UserProfileForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)  # request.FILES is show django handles file upload
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user  # Set the user created by UserCreationForm to UserProfile
            if not profile.profileImage:
                profile.profileImage = 'C:/Users/sslux/OneDrive/Desktop/SIC/Self-Improvement-Club-Website/mysite/media/profile_pics/defaultImage.jpg'
            # You may want to login the user here
            profile.save()
            login(request, user)
            return redirect('home')
            
    else:
        user_form = RegisterForm()
        profile_form = UserProfileForm()

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }

    return render(request, 'register/register.html', context)
