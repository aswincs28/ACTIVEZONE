from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

# Custom function to check if the user is an admin
def is_admin(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(is_admin, login_url='/signin/')  # Redirect unauthorized users
def dashboard(request):
    return render(request, 'admin_panel/dashboard.html')

@user_passes_test(is_admin, login_url='/signin/')
def manage_users(request):
    users = User.objects.all()
    return render(request, 'admin_panel/manage_users.html', {'users': users})

@user_passes_test(is_admin, login_url='/signin/')
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.is_active = request.POST.get('is_active') == "on"
        user.save()
        messages.success(request, "User details updated successfully!")
        return redirect('manage_users')
    return render(request, 'admin_panel/edit_user.html', {'user': user})

@user_passes_test(is_admin, login_url='/signin/')
def deactivate_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = False
    user.save()
    messages.success(request, "User deactivated successfully!")
    return redirect('manage_users')

@user_passes_test(is_admin, login_url='/signin/')
def approve_turfs(request):
    return render(request, 'admin_panel/approve_turfs.html')

@user_passes_test(is_admin, login_url='/signin/')
def system_logs(request):
    return render(request, 'admin_panel/system_logs.html')

@user_passes_test(is_admin, login_url='/signin/')
def reports(request):
    return render(request, 'admin_panel/reports.html')

def view_reports(request):
    return render(request, 'admin_panel/reports.html') 


@user_passes_test(is_admin, login_url='/signin/')
def dispute_handling(request):
    return render(request, 'admin_panel/dispute_handling.html')
