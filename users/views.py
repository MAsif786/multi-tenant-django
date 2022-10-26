from django.shortcuts import redirect, render
from django.contrib.auth.models import User as AuthUser
from tenants.middlewares import get_current_db_name
from users.models import User
from django.db import connection

# Create your views here.

def create_user(request):
    users = User.objects.all()
    print("USERS", get_current_db_name())
    tenant = request.META['HTTP_HOST'].split('.')[0]
    db = get_current_db_name()
    return render(request, 'create_user.html', {'users': users, 'db': db, 'tenant':db})

def save_user(request):
    email = request.POST['email']
    name = request.POST['username']
    password = request.POST['password']
    user = User(email=email, name=name)
    user.set_password(password)
    user.save()
    return redirect('create_user')