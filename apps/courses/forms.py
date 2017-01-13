from django import forms
from .models import Homework
#type="field"

			
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

class CodigoForm(forms.Form):
	codigo = forms.CharField(max_length=50,
		widget=forms.TextInput(attrs ={
				'type':'password',
				'class':'form-control',
				'placeholder':'Codigo'

			})
		)

class FileForm(forms.Form):
	nombre = forms.CharField(max_length=50,
		widget=forms.TextInput(attrs ={
				'type':'text',
				'class':'form-control',
				'placeholder':'Ingresa el nombre'

			})
		)
	file = forms.FileField(
			widget = forms.FileInput(attrs ={
				'type':'file',
				}
			)
		)

class HomeworkForm(forms.Form):
	nombre = forms.CharField(max_length=50,
		widget=forms.TextInput(attrs ={
				'type':'text',
				'class':'form-control',
				'placeholder':'Ingresa el nombre de la tarea',
				'required' :'False'

			})
		)
	descripcion = forms.CharField(max_length=1500,
		widget=forms.Textarea(attrs ={
				'class':'form-control',
				'placeholder':'Ingresa la descripcion de la tarea'

			})
		)
	file = forms.FileField(
			widget = forms.FileInput(attrs ={
				'type':'file'

				}
			)
		)
class CourseForm(forms.Form):
	rango= (
		('5','5'),
		('10','10'),
		('15','15'),
		('20','20'),
		('25','25'),
		('30','30'),
		('35','35'),
		('40','40'),
		('45','45'),		
	)
	materia = forms.CharField(max_length=50,
		widget=forms.TextInput(attrs ={
				'type':'text',
				'class':'form-control',
				'placeholder':'Materia',
				'required' :'False'

			})
		)
	salon = forms.CharField(max_length=50,
		widget=forms.TextInput(attrs ={
				'class':'form-control',
				'placeholder':'Aula'

			})
		)
	cupo_maximo = forms.ChoiceField(required=False,
        widget=forms.Select, choices=rango)

	descripcion = forms.CharField(max_length=1500,
		widget=forms.Textarea(attrs ={
				'class':'form-control',
				'placeholder':'Ingresa la descripcion del curso'

			})
		)

	codigo = forms.CharField(max_length=1500,
		widget=forms.TextInput(attrs ={
				'class':'form-control',
				'placeholder':'Codigo',
				'name': 'codigo',
				'id':'codigo'

			})
		)

class ReviewForm(forms.Form):
	rango= (
		('1','1'),
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),
		('6','6'),
		('7','7'),
		('8','8'),
		('9','9'),
		('10','10'),		
	)

	descripcion = forms.CharField(max_length=1500,
		widget=forms.Textarea(attrs ={
				'class':'form-control',
				'placeholder':'Ingresa la descripcion'

		})
	)

	calificacion = forms.ChoiceField(required=False,
        widget=forms.Select, choices=rango)
