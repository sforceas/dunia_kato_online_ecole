""" Profile models."""

#Django
from django.db import models

# Models
from dkecole.utils import choices
from django_countries.fields import CountryField


#Utilities
from dkecole.utils.models import DKEcoleModel


# Choices
from dkecole.utils.choices import EDUCATION_CHOICES, GENDER_CHOICES

class Profile(DKEcoleModel):
	"""Profile model.
	
    A profile holds a user's public data like biography, 
	picture and statistics.	
	"""
	
	user = models.OneToOneField('users.User',on_delete=models.CASCADE)
	
	picture = models.ImageField(
		'profile picture',
		upload_to='users/pictures/',
		blank=True,
		null=True,
    )
	
	web_page = models.CharField(max_length=50,blank=True)
	phone_number = models.CharField
	biography = models.TextField(max_length=500, blank=True)
	gender = models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True)
	country = CountryField(blank_label='(select country)',blank=True)
	birth_date = models.DateField(blank=True,null=True)
	educational_level = models.CharField(max_length=1,choices=EDUCATION_CHOICES,blank=True)
	is_working = models.BooleanField(blank=True,null=True)
	is_workin_role = models.CharField(max_length=50,blank=True,null=True)
	is_searching_work = models.BooleanField(blank=True,null=True)

	# Interests
	interest_bussiness = models.BooleanField(default=False,null=True)
	interest_marketing = models.BooleanField(default=False,null=True)
	interest_fabrication = models.BooleanField(default=False,null=True)
	interest_programming = models.BooleanField(default=False,null=True)		
	interest_idiomes = models.BooleanField(default=False,null=True)		

	# Stats
	points = models.PositiveIntegerField(default=0)
	answers = models.PositiveIntegerField(default=0)
	questions = models.PositiveIntegerField(default=0)
	courses_joined = models.PositiveIntegerField(default=0)
	courses_completed = models.PositiveIntegerField(default=0)

	# Privacity
	is_public_profile = models.BooleanField(default=False,null=True)
	is_public_name = models.BooleanField(default=False,null=True)

def __str__(self):
	"""Return user's str representation."""
	return str(self.user)
