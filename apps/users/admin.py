from django.contrib import admin # modelo  
from django.contrib.auth.admin import UserAdmin 
from .models import User#modelos de la aplicacion


#Clase para personalizar el administrador

class UserAdmin(UserAdmin):
	#separadores de seccion
	fieldsets= (
		('User',{'fields':('username','password')}),
		('Persona Info',{'fields' : ('first_name',
			                         'last_name',
			                         'email',
			                         'avatar',
			                         'acerca_de',
			                         'ocupacion',
			                         'sitio_web',
			                         'paiz')}),
		('Permissions',{'fields':('is_active',
								  'is_staff',
								  'is_superuser',
								  'is_master',
								  'groups',
								  'user_permissions')}),

	)

admin.site.register(User,UserAdmin)
