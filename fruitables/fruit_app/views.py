from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from . forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import Feedback, Cart_components

# Create your views here.
def index(request):
    # products = Product.object.all()
    return render(request,'index.html',{})
@login_required(login_url='fruit_app:login')
def contact(request):
    if request.method == 'POST':
        connect= Feedback(
            name = request.POST['name'],
            email = request.POST['email'],
            message = request.POST['message']
        )
        connect.save()
        messages.success(request,'thankyou for the feedback')
        return redirect('fruit_app:index')
    else:
        messages.success(request,'error')
        return render(request,'contact.html')
    
@login_required(login_url='fruit_app:login')
def shopdetails(request):
    return render(request,'shop-detail.html')

def shop(request):
    return render(request,'shop.html')

def checkout(request):
    # Check if its a post method
    if request.method == 'POST':
        # Create variable to pick the input fields
        components = Cart_components(
            # list the input fields here
            name = request.POST['name'],
            email = request.POST['email'],
            product_img = request.POST['product'],
            address = request.POST['address'],
            town = request.POST['town'],
            phone_num = request.POST['phone_num'],
            price = request.POST['price'],
        )
        # save the variable
        components.save()
        # redirect to a page
        return redirect('fruit_app:index')
    else:
        return render(request, 'checkout.html')

def testimonials(request):
    return render(request,'testimonial.html')

@login_required(login_url='fruit_app:login')
def cart(request):
    
    return render(request,'cart.html')

def page404(request):
    return render (request,'404.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('logged in successfully'))
            return redirect('fruit_app:index')
        else:
            messages.success(request, ('something went wrong'))
            return redirect('fruit_app:login')
    else:
        return render(request,'login.html')

def logout_view(request):
    logout(request,)
    messages.success(request, ('you have logged out successfully'))
    return redirect('fruit_app:index')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,('Registered successfully'))
            return redirect('fruit_app:index')
        else:
            messages.error(request,('error'))
            return render(request,'register.html')
    return render(request,'register.html', {'form': form})




