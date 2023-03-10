from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import CarDealer, CarModel, CarMake
# from .restapis import get_dealers_from_cf, get_dealers_by_state_from_cf, get_dealer_by_id_from_cf, get_dealer_reviews_from_cf, add_review_to_cf
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):
    return render(request, "djangoapp/about.html")


# Create a `contact` view to return a static contact page
def contact(request):
    return render(request, "djangoapp/contact.html")

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            context['message'] = 'Wrong username or password combination.'
    return render(request, "djangoapp/user_login.html", context)
# ...

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    if request.user is not None and request.user.is_authenticated:
        print("Logging out user {}".format(request.user.username))
        logout(request)
    return redirect('djangoapp:index')

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        password2 = request.POST['psw2']
        if password == password2:
            email = request.POST['email']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            users = User.objects.filter(username=username)
            if users.count() == 0:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                login(request, user)
                return redirect('djangoapp:index')
            else:
                context['message'] = "User {} already exists! Please try another unique username.".format(username)
        else:
            context['message'] = "Entered passwords do not match. Please try again and make sure they are correct."
    return render(request, "djangoapp/registration.html", context)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

