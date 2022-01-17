"""Users models."""
#Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#Utilities
from dkecole.utils.models import DKEcoleModel

class User(DKEcoleModel, AbstractUser):
	"""User model.
	Extend from django's AbstractUser, chanthe the username field
	to email and add some extra fields.
	"""
	email = models.EmailField(
		'email adress',
		unique=True,
		error_messages = {
			'unique':'A user with that email already exists.'		
		}	
	)
	
	"""Regular expression for validate the phone number."""
	phone_regex = RegexValidator(
		regex=r'^\+?1?\d{9,15}$',
		message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
	)
	phone_number = models.CharField(validators=[phone_regex],max_length=17,blank=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username','first_name','last_name']

	is_student = models.BooleanField(
		'student status',
		default=True,
		help_text=(
			'Help easily distinguish users and perform queries.'
			'Clients are the main type of user.'
		)
	)	
	
	is_verified = models.BooleanField(
		'verified',
		default=False,
		help_text=(
			'Set to True when the user verifies its email adress'
		)
	)	
	
def __str__(self):
	"""Return username."""
	return self.username

