from django.db import models
from apps.users.models import User
class Course(models.Model):
	
	materia = models.CharField(max_length=50,null=True ,blank=True)
	salon = models.CharField(max_length=50,null=True,blank=True)
	cupo_maximo = models.IntegerField()
	descripcion = models.TextField(max_length=2000)
	users=models.ManyToManyField('users.User',null=True)
	codigo = models.CharField(max_length=6)
	def __str__(self):
		return self.materia + " "+self.salon

class FilesCourse(models.Model):
	name = models.CharField(max_length=30, null=True)
	docfile = models.FileField(upload_to='ContentCourse/%Y/%m/%d', null = True)
	course=models.ForeignKey(Course)
	
	def __str__(self):
		return "file"+str(self.id)+"de "+self.course.materia

class Question(models.Model):
	titulo = models.CharField(max_length = 50, null = True, blank = True)
	contenido = models.CharField(max_length = 50, null= True, blank = True)
	course = models.ForeignKey('Course',null=True)
	user = models.ForeignKey('users.User')

class Response(models.Model):
	user = models.ForeignKey('users.User')
	question = models.ForeignKey('Question')
	titulo= models.CharField(max_length = 50, null = True, blank = True)
	descripcion = models.CharField(max_length = 50, null= True)

class Post(models.Model):
	docfile = models.FileField(upload_to='documents/%Y/%m/%d', null = True)
	tema = models.CharField(max_length = 50, null = True)
	descripcion = models.CharField(max_length = 50, null= True)
	course = models.ForeignKey(Course)
	user = models.ForeignKey(User)
class Homework(models.Model):
	nombre = models.CharField(max_length = 50, null = True)
	descripcion = models.TextField(max_length = 2000, null = True)
	docfile = models.FileField(upload_to='documents/%Y/%m/%d', null = True, blank=True)
	user = models.ForeignKey('users.User', null= True,blank=True)
	curso= models.ForeignKey('Course',null = True)
	is_master = models.BooleanField(default= False)
	def __str__(self):
		return "tarea "+str(self.id)+" alumno: "+self.user.first_name + self.user.last_name
class Review(models.Model):
	descripcion = models.TextField(max_length = 300, null = True)
	calificacion = models.FloatField(default = 0)
	tarea = models.ForeignKey(Homework)
	user = models.ForeignKey('users.User')

	def __str__(self):
		return "revision "+self.tarea.nombre+" del alumno "+self.tarea.user.first_name
