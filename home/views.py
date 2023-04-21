from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    categories= Category.objects.all()
    coursal=Coursal.objects.all()
    params={
        'categories':categories,
        'coursal':coursal,
    }

    return render(request,'index.html',params)

def category(request,string):
    categories= Category.objects.all()
    category=Category.objects.get(name=string)
    products=Product.objects.filter(category=category)
    params={
        'categories':categories,
        'products':products,
    }
    return render(request,'category.html',params)

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
        else:
            messages.error(request, "Invalid Credentials")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def signout(request):
    if request.method == "POST":
        print("here")
        logout(request)
        return HttpResponseRedirect("/")
def signup(request):
    if request.method == "POST":
        # we can also write like this
        # username=request.POST['username']
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Your Account has been successfully created.")
        except Exception as e:
            messages.error(request, "Something went wrong try again later !")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def about(request):
    categories = Category.objects.all()
    return render(request,'aboutus.html',{'categories':categories})

def feedback(request):
    categories = Category.objects.all()
    return render(request,'feedback.html',{'categories':categories})

def help(request):
    categories = Category.objects.all()
    return render(request,'help.html',{'categories':categories})

def submitfeedback(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name= request.POST['name']
        email= request.POST['email']
        mobileno= request.POST['mobileno']
        feedback= request.POST['feedback']
        fd=Feedback.objects.create(name=name,email=email,mobile_number=mobileno,feedback=feedback)
        fd.save()
    return render(request,'feedback.html',{'categories':categories})