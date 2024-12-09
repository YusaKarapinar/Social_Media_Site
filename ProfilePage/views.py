
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def profile_page(request):
    user_info = {
        'username': 'JohnDoe',
        'email': 'john.doe@example.com',
        'bio': 'Web Developer and Django Enthusiast',
    }
    return render(request, 'profile/profile_page.html', {'user_info': user_info})



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