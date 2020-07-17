from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from home.models import Demo

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.http import request


# Create your views here.
def index(request):
    context = {
        "variable1": "VICKY IS GREAT",
        "variable2": "VICKY IS GREAT"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("HELLO WORLD")


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def services(request):
    return render(request, 'services.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, "register.html")


def demo(request):
    if request.method == "POST":
        name = request.POST.get('dname')
        phone = request.POST.get('dphone')
        email = request.POST.get('demail')
        review = request.POST.get('dreview')
        address = request.POST.get('daddress')
        print(name, phone, email, review, address)
        demo = Demo(name=name, email=email, phone=phone,
                    address=address, review=review, date=datetime.today())
        demo.save()
        messages.success(request, 'YOUR FORM HAS BEEN SUBMITTED SUCCESSFULLY!')
    return render(request, "demo.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        review = request.POST.get('review')
        wesite = request.POST.get('wesite')
        contact = Contact(name=name, email=email, phone=phone,
                          wesite=wesite, review=review, date=datetime.today())
        contact.save()
        messages.success(request, 'YOUR FORM HAS BEEN SUBMITTED SUCCESSFULLY!')

    return render(request, 'contact.html')

# login function
# Create your views here.


def handlesignup(request):
    print("inside handlesignup")
    print(request.method)
    if request.method == 'POST':
        # PARAMETERS lena Hai
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # check karna padega error....

        # user creation
        myuser = User.objects.create_user(
            username=username, password=password1, email=email)
        myuser.save()
        print(myuser)
        messages.success(
            request, "YOUR SHIFT ACCOUNT HAS BEEN SUCCESSFULLY CREATEDD")

        return redirect("login")

    else:
        return HttpResponse('404 -NOT FOUNDDD')


def handleLogin(request):
    if request.user.is_anonymous:
        messages.info(
            request, "YOU HAVE TO LOGIN FIRST TO ACCESS FURTHER PAGES-:")

    if request.method == 'POST':
        # PARAMETERS lena Hai
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(
            request=request, username=loginusername, password=loginpassword)

        if user is not None:
            login(request)
            messages.info(request, "LOGIN HOOGAYA BRO")
            return redirect("home")

        else:
            messages.error(request, "PASSWORD GALAT HAI BRO")
            return redirect("login")

    if request.method == 'GET':
        return render(request, 'login.html')

    return HttpResponse('login')


def handleLogout(request):
    logout(request)
    messages.success(request, "LOGOUT HOOGAYA BRO")
    return redirect('login')

    return HttpResponse('handleLogout')
