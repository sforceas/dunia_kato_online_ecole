"""Users serializers"""

# Django
from django.conf import settings
from django.contrib.auth import authenticate, password_validation
from django.db.models.query import QuerySet

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator

# JSON Web Token 
import jwt

# Models
from dkecole.users.models import User, Profile

# Tasks
from dkecole.taskapp.tasks import send_confirmation_email

# Serializers
from dkecole.users.serializers import ProfileModelSerializer

#Utilities
from datetime import timedelta

class UserModelSerializer(serializers.ModelSerializer):
    """User Model Serializer."""

    profile = ProfileModelSerializer(read_only=True)

    class Meta:
        """Meta class"""
        model=User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'profile'
        )
        read_only_fields = ('profile',)
        depth = 1

class UserLoginSerializer(serializers.Serializer):
    """User Login Serializer.
    
    Handle the login request data.
    """
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8,max_length=64)

    def validate(self,data):
        """Verify credentials."""
        user = authenticate(username=data['email'],password=data['password'])
        if not user:
            """Invalid login credentials"""
            raise serializers.ValidationError('Invalid credentials')
        self.context['user']=user
        if not user.is_verified:
            raise serializers.ValidationError('Account is not active yet :(')
        return data
    
    def create(self,data):
        """Generate or retrieve an existing token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'],token.key

class UserSignUpSerializer(serializers.Serializer):
    """Users signup serializer
    
    Handle sign up data validation and user/profile creation.
    """
    # Email
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    
    # Username
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # Phone number
    """Regular expression for validate the phone number."""
    phone_regex = RegexValidator(
		regex=r'^\+?1?\d{9,15}$',
		message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
	)

    phone_number = serializers.CharField(validators=[phone_regex])

    # Password
    password = serializers.CharField(min_length=8,max_length=64)
    password_confirmation = serializers.CharField(min_length=8,max_length=64)

    # Name
    first_name=serializers.CharField(min_length=2,max_length=30)
    last_name=serializers.CharField(min_length=2,max_length=30)

    def validate(self,data):
        """Veryfy passwords match"""
        password=data['password']
        password_confirmation=data['password_confirmation']
        if password != password_confirmation:
            raise serializers.ValidationError('Passwords do not match')
        password_validation.validate_password(password)
        return data

    def create(self,data):
        """Handle user and profile creation"""
        data.pop('password_confirmation')
        user = User.objects.create_user(**data, is_verified=False,is_client=True)
        profile = Profile.objects.create(user=user)
        send_confirmation_email.delay(user_pk=user.pk)
        return user
   
class AccountVerificationSerializer(serializers.Serializer):
    """Account verification serializer"""
    token = serializers.CharField()
    def validate_token(self,data):
        """Verify token is valid"""
        try: 
	        payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Verification link has expired.')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Invalid token')
        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('Invalid token.')
        self.context['payload']=payload
        return data
	
    def save(self):
        """Update user's verified status"""
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()