from django.shortcuts import render,redirect
from django.contrib.auth import logout, authenticate,login
from django.views.generic import TemplateView,CreateView,FormView,DetailView,ListView
from braces.views import LoginRequiredMixin
from apps.users.forms import RegisterStudentForm, LoginForm
from .models import User
from apps.courses.models import Course
from django.views.generic import TemplateView
from django.contrib.auth.models import Permission


def LogOut(request):
	logout(request)
   	return redirect('/')
   	
class IndexView(DetailView):
	template_name='home/login.html'
	#funcion por convencion para enviar mas informacion
	def get_context_data(self,**kwargs):
		context=super(IndexView,self).get_context_data(**kwargs)
		user = self.request.user 
		if user.is_master:
			courses=Course.objects.all()
		else:
			courses = Course.objects.filter(user = user)
		context['courses']= courses


class LoginView(FormView):
	form_class = LoginForm
	template_name='home/login.html'
	success_url='/panel/'

	def form_valid(self,form):
		user= authenticate(username = form.cleaned_data['username'],password=form.cleaned_data['password'])
		if user is not None:
			if user.is_active:
				login(self.request,user)

		return super(LoginView,self).form_valid(form)


class RegistrateView(FormView):
	template_name='home/registro.html'
	form_class=RegisterStudentForm
	success_url='/panel'

	
		

	def form_valid(self,form):
		user = User()
		user.email = form.cleaned_data['email']
		user.username = form.cleaned_data['username']
		user.first_name = form.cleaned_data['first_name']
		user.last_name = form.cleaned_data['last_name']
		user.email = form.cleaned_data['email']
		user.avatar = 'https://psiiss.net/images/User-icon.png'
		user.set_password(form.cleaned_data['password'])
		is_master = form.cleaned_data['is_master']

		if is_master=="True":
			user.is_master = True
			print("se creo un maetro")
			
		else:
			print("se creo un alumno")

		user.save()
		print(form.cleaned_data['is_master'])
		return super(RegistrateView,self).form_valid(form)
	def form_invalid(self,form):
		print "no es valido"
		return super(RegistrateView,self).form_invalid(form)
class PanelView(LoginRequiredMixin,ListView):
	template_name='users/perfil.html'
	login_url='/login'
	context_object_name='courses'
	
	def get_queryset(self):
		user = self.request.user
		#if user.is_master:
		#	models = Course.objects.all()
		#else:
		models = Course.objects.filter(users=user)
		u=User.objects.get(username=user.username)
		print(u.course_set.all())
		print(models)
		return models
