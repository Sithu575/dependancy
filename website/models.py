from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Department(models.Model):
	name=models.CharField(max_length=50)
	
	def __str__(self):
		return self.name

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)
	department=models.ForeignKey(Department, null=True, blank=True,on_delete=models.CASCADE)
	

	def __str__(self):
		return f"{self.first_name}{self.last_name}"
	
class Organization(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)
	type=models.ForeignKey("Type", null=True, blank=True, on_delete=models.SET_NULL)	

	def __str__(self):
		return f"{self.first_name}{self.last_name}"
	


class Type(models.Model):
	type = models.CharField(max_length=50)
	def __str__(self):
			return self.type

class Contacts(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)
	type=models.ForeignKey(Type, null=True, blank=True, on_delete=models.SET_NULL)
	organization=models.ForeignKey(Organization,null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
			return f"{self.first_name}{self.last_name}"
	
class Lead(models.Model):
		organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
		agent = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
		description = models.TextField(blank=True, null=True)
		date_added = models.DateTimeField(default=timezone.now, editable=False)   # Set default to timezone.now)
		phone_number = models.CharField(max_length=20,null=True)
		email = models.EmailField(max_length=100,null=True)
		converted_date = models.DateTimeField(null=True, blank=True)
		approved=models.BooleanField(default=False)
		class Meta:
			permissions=(("can_lead_approval","to approve leads"),)
		
		
		def __str__(self):
			return f"{self.email}"
