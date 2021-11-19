from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



from .models import Arriving, Passenger


class ArrivalForm(ModelForm):
	class Meta:
		model = Arriving
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CreatePassenger(ModelForm):
	class Meta:
		model = Passenger
		fields = '__all__'

		# name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Something...'}))
		# address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Something...'}))
		# parents_Number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Something...'}))

class CreateArrival(ModelForm):
	class Meta:
		model = Arriving
		fields = '__all__'