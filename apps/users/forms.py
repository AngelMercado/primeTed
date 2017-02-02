from django import forms
from .models import User
import re
import json
import pprint
class RegisterStudentForm(forms.ModelForm):
	PERFIL_CHOICES= (
			(True,'Maestro'),
			(False,'Estudiate'),
		)
	is_master = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFIL_CHOICES)
	remainder = forms.CharField(widget=forms.PasswordInput(attrs={
					'class':'form-control',
					 'type':'password',
					 'placeholder':'repite el password',
					 'name':'remainder',
					 'id':'id_remainder'
					}))
	class Meta:
		
		model = User
		fields = ('username','first_name','last_name','email','password','is_master','remainder')
		widgets={
				'username': forms.TextInput(attrs={
					'class':'form-control',
					 'placeholder':'username',
					}),
				'first_name': forms.TextInput(attrs={
					'class':'form-control',
					 'placeholder':'Nombre',
					
					}),
				'last_name': forms.TextInput(attrs={
					'class':'form-control',
					 'placeholder':'Apellidos'
					}),
				'email': forms.TextInput(attrs={
					'class':'form-control',
					 'placeholder':'Correo'
					}),
				'password': forms.TextInput(attrs={
					'class':'form-control',
					 'type':'password',
					 'placeholder':'crea tu password',
					 'name':'password'
					})
		}

	
	def clean_first_name(self):
		#pattern = re.compile('[^\d\W A-Z]|[a-z\[^\d\W]]')
		pattern = re.compile(r"""
		\b             # comienzo de delimitador de palabra
		[a-z]{2,6}       # usuario: Cualquier caracter alfanumerico mas los signos (.%+-)
		       
		\b             # fin de delimitador de palabra
		""", re.X)
		pattern2 = re.compile('\.')
		username = self.cleaned_data['first_name']
		print pattern.search(username)
		if pattern.search(username)==None:
			#self.add_error('first_name', 'el formato no es valido')
			raise forms.ValidationError("ingresa un formato correcto")
		else:
			return self.cleaned_data['first_name']	

	def clean_last_name(self):
		pattern = re.compile(r"""
		\b             # comienzo de delimitador de palabra
		[a-z]{2,10}       # usuario: Cualquier caracter alfanumerico mas los signos (.%+-)
		       
		\b             # fin de delimitador de palabra
		""", re.X)
		lastname = self.cleaned_data['last_name']
		if pattern.search(lastname)==None:
			raise forms.ValidationError("ingresa un formato correcto")
		else:
			return self.cleaned_data['last_name']
	def clean_password(self):
		pattern = re.compile('(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$')
		password = self.cleaned_data['password']
		
		if pattern.match(password)==None:
			raise forms.ValidationError("debe contener almenos 8 caracteres, una letara mayuscula y un numero")
		else:
			return self.cleaned_data['password']
			
class LoginForm(forms.Form):
	username = forms.CharField(max_length=50,
		widget=forms.TextInput(attrs ={
				'type':'text',
				'class':'form-control',
				'placeholder':'usuario'


			}))
	password = forms.CharField(max_length=50,
		widget=forms.TextInput(attrs ={
				'type':'password',
				'class':'form-control',
				'placeholder':'password'

			})
		)