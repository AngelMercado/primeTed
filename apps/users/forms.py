from django import forms
from .models import User
class RegisterStudentForm(forms.ModelForm):
	PERFIL_CHOICES= (
			(True,'Maestro'),
			(False,'Estudiate'),
		)
	is_master = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFIL_CHOICES)
	class Meta:
		
		model = User
		fields = ('username','first_name','last_name','email','password','is_master')
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
					}),
		}


			
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