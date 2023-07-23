from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .forms import UserProfileForm
from .forms import UserLoginForm
from .models import UserProfile
from django.urls import reverse

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            if created:
                login(request, user)
            return redirect(reverse('home'))  # Redirect to the home page after registration
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
    
@login_required
def user_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)  # Save the form data to the user_profile object but do not save it to the database yet
            user_profile.user = request.user  # Set the user field manually to the current user
            user_profile.save()  # Save the user_profile object to the database
            return redirect('users:userprofile')  # Redirect to the profile page after successful save
    else:
        # Set the username field value manually in the form
        form = UserProfileForm(instance=user_profile, initial={'username': request.user.username})

    context = {
        'form': form
    }
    return render(request, 'users/userprofile.html', context)
    
@user_passes_test(lambda user: user.is_superuser)
def user_list(request):
    # View function for the user list page (for admin users only)
    users = UserProfile.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))  # Redirect to the home page after successful login
    else:
        form = UserLoginForm(request)

    return render(request, 'users/login.html', {'form': form})
    
@login_required
def member_page(request):
    # Assuming you have a UserProfile model related to the User model
    user_profile = request.user.userprofile

    # Retrieve additional information related to the user profile
    favorite_products = user_profile.favorite_products.all()

    # You can perform other actions or queries here to get the required data

    # Pass the data to the template
    context = {
        'user_profile': user_profile,
        'favorite_products': favorite_products,
    }

    return render(request, 'membersonly.html', context)

def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html')