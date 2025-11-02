from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.user_type == 'admin':
                return redirect('admin_dashboard')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def admin_dashboard(request):
    if request.user.user_type != 'admin':
        return redirect('home')
    students = CustomUser.objects.filter(user_type='student')
    lecturers = CustomUser.objects.filter(user_type='lecturer')
    return render(request, 'users/dashboard.html', {'students': students, 'lecturers': lecturers})

@login_required
def manage_users(request):
    if request.user.user_type != 'admin':
        return redirect('home')
    users = CustomUser.objects.exclude(id=request.user.id)
    return render(request, 'users/manage_users.html', {'users': users})

@login_required
def delete_user(request, user_id):
    if request.user.user_type != 'admin':
        return redirect('home')
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    messages.success(request, 'User deleted successfully')
    return redirect('manage_users')
