
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm  # Formu içe aktardık

@login_required(login_url='/login/')
def profile_page(request):
    user_info = request.user
    return render(request, 'profile/profile_page.html', {'user_info': user_info})

@login_required(login_url='/login/')
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile:profile_page')
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'profile/edit_profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hesabınız başarıyla oluşturuldu, {username}!')
            return redirect('login')  # Varsayılan giriş URL'si
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})