from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.shortcuts import redirect

class UserManager(BaseUserManager,models.Manager):
	def create(self,username,last_name,email,password,is_staff,is_superuser,**extra_fields):
		
		email=self.normalize_email(email)
		user=self.model(username=username,last_name=last_name,email=email,is_active=True,is_staff=is_staff,is_superuser=is_superuser,**extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user
	def _create_user(self,username,email,password,is_staff,is_superuser,**extra_fields):

		email=self.normalize_email(email)
		if not email:
			
			raise ValueError('el email es obligatorio')
		
		user=self.model(username=username,email=email,is_active=True,is_staff=is_staff,is_superuser=is_superuser,**extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self,username,email,password=None, **extra_fields):
		return self._create_user(username, email, password, False, False, **extra_fields)

	def create_superuser(self, username, email, password, **extra_fields):
		return self._create_user(username, email, password, True, True, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin, models.Model):

	username=models.CharField(max_length=30, unique=True)
	email= models.EmailField(max_length=50, unique=True)
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	acerca_de = models.TextField(max_length = 100, null = True, blank=True)
	paiz= models.CharField(max_length = 50,null = True, blank=True)
	ocupacion = models.CharField(max_length = 100, null = True, blank=True)
	sitio_web= models.URLField(null = True, blank=True)
	avatar=models.URLField(null = True, blank=True)
	objects = UserManager()
	is_active=models.BooleanField(default=True)
	is_staff=models.BooleanField(default=False)
	is_master=models.BooleanField(default=False)
	USERNAME_FIELD= 'username'
	REQUIRED_FIELDS=['email']

	def get_short_name(self):
		return self.username
	def get_user_name(self):
		return self.username+self.last_name
		
