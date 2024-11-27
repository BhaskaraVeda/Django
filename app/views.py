from django.shortcuts import render
from .models import UserAccount
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

# Create your views here.
def register(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        pwd=make_password(password)
        # print(f"Name: {name}, Mobile: {mobile}, Password: {password}")
        # UserAccount.objects.create(name=name, mobile=mobile,password=pwd)
        # UserAccount.save()
        user_account = UserAccount(name=name, email=email, password=pwd)
        user_account.save()  # This manually saves the instance
        # print('success')
        return redirect('signin')

    return render(request,'register.html')


def signin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
          # Get the user object
        try:
            user = UserAccount.objects.get(email=email)
            print(f'user found {user}')
        except Exception as e:
            print(e)
            return redirect('signin')
        user = UserAccount.objects.filter(email=email).first()
        # print(user.password)
        # pwd=make_password(password)
        # print(pwd)
        valid=check_password(password,user.password)
        print(valid)
        if valid :
            print(user)
            # login(request,user)
            print('login success')
            return render(request,'home.html')
        else:
            return redirect('signin')
    
    return render(request, 'signin.html')

