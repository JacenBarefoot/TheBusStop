from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreatePassenger, ArrivalForm, CreateUserForm, CreateArrival
from .filters import ArrivalFilter

def signupPage(request):
	if request.user.is_authenticated:
		return redirect('home')         
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			  

		context = {'form':form}
		return render(request, 'signup.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)
   
def logoutUser(request):
	logout(request)
	return redirect('home')

def home(request):
	return render(request, 'home.html')


def dashboard(request):
	if request.user.is_authenticated:
		arriving = Arriving.objects.all()
		passenger = Passenger.objects.all()

		total_passengers = passenger.count()

		total_arriving = arriving.count()
		on_the_bus = arriving.filter(status='On the bus').count()
		off_the_bus = arriving.filter(status='Off the bus').count()

		context = {'arriving':arriving, 'passenger':passenger,
		'total_arriving': total_arriving,'on_the_bus': on_the_bus,
		'off_the_bus': off_the_bus }

		return render(request, 'dashboard.html', context)
	else: 
		return render(request, 'notloggedin.html')

def allPassengers(request):
	if request.user.is_authenticated:
		passenger = Passenger.objects.all()
		return render(request, 'allpassengers.html', {'passenger':passenger})
	else:
		return render(request, 'notloggedin.html')

def createpassenger(request):
	form = CreatePassenger()
	if request.user.is_authenticated:
		if request.method == "POST":
			form = CreatePassenger(request.POST)
			if form.is_valid():
				form.save()
				return redirect("home")
	else:
		return redirect("dashboard")
	context = {"form": form}
	return render(request, "createpassenger.html", context)

def createarrival(request):
	form = CreateArrival()
	if request.user.is_authenticated:
		if request.method == "POST":
			form = CreateArrival(request.POST)
			if form.is_valid():
				form.save()
				return redirect("dashboard")
	else:
		return redirect("home")
	context = {"form": form}
	return render(request, "createarrival.html", context)

@login_required(login_url='login')
def passenger(request, pk_test):
	passenger = Passenger.objects.get(id=pk_test)
	all_passengers = Passenger.objects.all()
	orders = passenger.order_set.all()
	order_count = orders.count()

	myFilter = ArrivalFilter(request.GET, queryset=orders)
	orders = myFilter.qs 

	context = {'passenger':passenger, 'orders':orders, 'order_count':order_count,
	'myFilter':myFilter,'all_passengers': all_passengers}
	return render(request, 'student.html',context)

@login_required(login_url='login')
def createArriving(request, pk):
	ArrivalFormSet = inlineformset_factory(Passenger, Arriving, fields=('product', 'status'), extra=10 )
	student = Passenger.objects.get(id=pk)
	formset = ArrivalFormSet(queryset=Arriving.objects.none(),instance=student)
	if request.method == 'POST':
		form = ArrivalForm(request.POST)
		formset = ArrivalFormSet(request.POST, instance=student)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset} 
	return render(request, 'arrival_form.html', context)

@login_required(login_url='login')
def updateArriving(request, pk):

	arriving = Arriving.objects.get(id=pk)
	form = ArrivalForm(instance=arriving)

	if request.method == 'POST':
		form = ArrivalForm(request.POST, instance=arriving)
		if form.is_valid():
			form.save()
			return redirect('dashboard')

	context = {'form':form}
	return render(request, 'arrival_form.html', context)

@login_required(login_url='login')
def deleteArriving(request, pk):
	arriving = Arriving.objects.get(id=pk)
	if request.method == "POST":
		arriving.delete()
		return redirect('dashboard')

	context = {'item':arriving}
	return render(request, 'delete.html', context)
