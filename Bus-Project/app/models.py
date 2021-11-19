from django.db import models

# Create your models here.

class Passenger(models.Model):
	name = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	preferred_Number = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	tag_name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.tag_name

class Arriving(models.Model):
	STATUS = (
			('On the bus', 'On the bus'),
			('Off the bus', 'Off the bus'),
			)

	AGE = (
			('Kid', 'Kid'),
			('Adult', 'Adult'),
		) 

	passenger_name = models.ForeignKey(Passenger, null=True, on_delete= models.SET_NULL)
	age = models.CharField(max_length=5, null=True, choices=AGE)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return self.passenger_name.name