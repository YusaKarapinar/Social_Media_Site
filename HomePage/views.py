# HomePage/views.py
from .forms import CustomUserCreationForm
from django.shortcuts import render,redirect  
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Mesajları içe aktar

@login_required(login_url='/login/')
def notifications(request):
    return render(request, 'notifications.html')

@login_required(login_url='/login/')
def settings(request):
    return render(request, 'HomePage/settings.html', {'page_title': 'Settings'})

@login_required(login_url='/login/')
def homepage(request):
    return render(request, 'HomePage/homepage.html', {
        'page_title': 'Home Page',
    })

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed! Please check your information.')
    else:
        form = CustomUserCreationForm()
    
    # Şablon yolunun doğru olduğundan emin olun
    return render(request, 'HomePage/register.html', {'form': form})