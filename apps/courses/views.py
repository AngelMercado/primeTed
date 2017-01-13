from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,CreateView,FormView,DetailView,ListView,DeleteView
from braces.views import LoginRequiredMixin
from .models import Course,User,Homework,Post,FilesCourse,Review
from .forms import LoginForm,CodigoForm,FileForm,HomeworkForm,CourseForm,ReviewForm
# Create your views here.
class CourseCreateView(LoginRequiredMixin,CreateView):
	template_name='courses/createCourse.html'
	model = Course
	success_url='/panel'
	login_url='/login'

	def form_valid(self,form):
		return super(CourseCreateView,self).form_valid(form)
	def form_invalid(self,form):
		return super(CourseCreateView,self).form_invalid(form)

class CourseDetailView(LoginRequiredMixin,FormView):
	id_course=0
	template_name='courses/course_detail.html'	
	login_url='/login'
	form_class = FileForm
	success_url='/InfoCourse/'
	def get_context_data(self,**kwargs):
		context = super(CourseDetailView,self).get_context_data(**kwargs)
		id_course=self.kwargs['pk'] 
		curso= Course.objects.get(id=id_course)
		files = FilesCourse.objects.filter(course=curso)
		context['course']= curso
		context['files'] = files
		return context
	def form_valid(self,form):
		id_course=self.kwargs['pk']
		self.success_url+= str(id_course) 		
		file = self.request.FILES['file']
		nombre= form.cleaned_data['nombre']
		course=Course.objects.get(id = id_course)
		nuevo_file=FilesCourse(name=nombre,docfile=file,course=course)
		nuevo_file.save()

		for x in range(0,10):
			print 'valido'

		return super(CourseDetailView,self).form_valid(form)
	def form_invalid(self,form):
		for x in range(0,10):
			print 'invalido'
		return super(CourseDetailView,self).form_invalid(form)
	#se usa esta funcion para enviar el id del curso

class CourseListStudent(LoginRequiredMixin,TemplateView):
	template_name='courses/alumnos_list.html'
	login_url='/login'
	
	def get_context_data(self,**kwargs):
		context=super(CourseListStudent,self).get_context_data(**kwargs)
		courses=Course.objects.all()
		numero= self.kwargs['num']  # se manda por parametro el id del curso seleccionado
		context['courses']= courses
		curso=Course.objects.filter(id=numero)
		alumnos=User.objects.filter(course=curso,is_master = False) 
		context['alumnos']=alumnos
		context['course'] = curso[0]
		return context


class CreateHomework(FormView):
	template_name='courses/create_homework.html'
	form_class = HomeworkForm
	success_url='/InfoCourse/'
	def get_context_data(self,**kwargs):
		context = super(CreateHomework,self).get_context_data(**kwargs)
		id_course=self.kwargs['pk'] 
		curso= Course.objects.get(id=id_course)
		files = FilesCourse.objects.filter(course=curso)
		context['course']= curso
		return context
	def form_valid(self,form):
		self.success_url += self.kwargs['pk'] 
		nombre = form.cleaned_data['nombre']
		descripcion = form.cleaned_data['descripcion']
		file = self.request.FILES['file']
		user = self.request.user
		id_course=self.kwargs['pk'] 
		curso= Course.objects.get(id=id_course)
		if user.is_master:
			nueva_tarea = Homework()
			nueva_tarea.nombre = nombre
			nueva_tarea.descripcion = descripcion
			nueva_tarea.docfile = file
			nueva_tarea.user = user 
			nueva_tarea.curso = curso
			nueva_tarea.is_master = True
			nueva_tarea.save()
		else:
			nueva_tarea = Homework()
			nueva_tarea.nombre = nombre
			nueva_tarea.descripcion = descripcion
			nueva_tarea.docfile = file
			nueva_tarea.user = user 
			nueva_tarea.curso = curso
			nueva_tarea.is_master = False
			nueva_tarea.save()

		return super(CreateHomework,self).form_valid(form)

	def form_invalid(self,form):
		return super(CreateHomework,self).form_invalid(form)

class Inscripcion(FormView):
	success_url='/panel'
	template_name= 'courses/cursosdisponibles.html'
	form_class = CodigoForm
	mensaje =""

	def get_context_data(self,**kwargs):
		context = super(Inscripcion,self).get_context_data(**kwargs)
		user = self.request.user
		if user.is_master:
			cursos= Course.objects.all()
		else:
			cursos= Course.objects.all()
			cursos_inscritos = Course.objects.filter(users=user)
		context['courses'] = cursos
		context['courses_enrrollment'] = cursos_inscritos
		return context
	def form_valid(self,form):
		codigo= form.cleaned_data['codigo']
		id_curso= self.kwargs['id_course']
		id_user = self.request.user.id
		curso = Course.objects.get(id=id_curso)
		user = User.objects.get(id=id_user)
		if curso.codigo == codigo:
			curso.users.add(user)
			print "revisa tu nuevo curso"
		else:
			print "error en el codigo"

		return super(Inscripcion,self).form_valid(form)


class HomeworksCourse(LoginRequiredMixin,TemplateView):
	template_name='courses/homeworks_course.html'
	login_url='/login'
	
	def get_context_data(self,**kwargs):
		context=super(HomeworksCourse,self).get_context_data(**kwargs)
		user = self.request.user
		id_course = self.kwargs['pk']
		course = Course.objects.get(id = id_course )
		homeworks_course = Homework.objects.filter(is_master = True, curso = course)
		courses = Course.objects.all()
		context['course'] = course
		context['courses']= courses
		context['homeworks_course'] = homeworks_course
		return context

class HomeworksUser(LoginRequiredMixin,TemplateView):
	template_name = "courses/homeworks_user.html"
	login = '/login'

	def get_context_data(self,**kwargs):
		context=super(HomeworksUser,self).get_context_data(**kwargs)
		user = self.request.user
		id_course = self.kwargs['pk']
		course = Course.objects.get(id = id_course )
		homeworks_course = Homework.objects.filter(curso = course, user=user)
		context['course'] = course
		context['homeworks_course'] = homeworks_course
		return context	


class HomeworksStudents(LoginRequiredMixin,TemplateView):
	template_name="courses/homeworks_students.html"
	login = '/login'

	def get_context_data(self,**kwargs):
		context = super(HomeworksStudents,self).get_context_data(**kwargs)
		id_course = self.kwargs['pk']
		course = Course.objects.get(id = id_course)
		homeworks_students = Homework.objects.filter(is_master = False, curso = course)
		context['course'] = course
		context['homeworks_students'] = homeworks_students
		return context


class DeleteStudent(LoginRequiredMixin,TemplateView):
	template_name='courses/alumnos_list.html'
	login = '/login'

	def get_context_data(self,**kwargs):
		context=super(DeleteStudent,self).get_context_data(**kwargs)
		id_course= self.kwargs['pk_course']  # se manda por parametro el id del curso seleccionado
		id_user = self.kwargs['pk_user']
		alumno_eliminado = User.objects.get(id = id_user)
		#User.objects.filter(id = id_user).delete()
		
		curso=Course.objects.get(id = id_course)
		
		alumnos=User.objects.filter(course=curso, is_master = False)
		alumno_eliminado.course_set.remove(curso)
		

		context['alumnos']=alumnos
		context['course'] = curso
		context['mensaje'] ="se ha eliminado con exito el alumno"+alumno_eliminado.first_name+" "+alumno_eliminado.last_name

		return context

class CreateCourse(FormView):
	template_name='courses/createCourse.html'
	form_class = CourseForm
	success_url='/InfoCourse/'
	def get_context_data(self,**kwargs):
		context = super(CreateCourse,self).get_context_data(**kwargs)
		return context
	def form_valid(self,form):
		course = Course()
		course.materia = form.cleaned_data['materia']
		course.salon = form.cleaned_data['salon']
		course.cupo_maximo = form.cleaned_data['cupo_maximo']
		course.descripcion = form.cleaned_data['descripcion']
		course.codigo = form.cleaned_data['codigo']
		course.save()
		user = self.request.user
		user.course_set.add(course)
		self.success_url+=str(course.id)
		return super(CreateCourse,self).form_valid(form)

	def form_invalid(self,form):
		print "no es valido"
		return super(CreateCourse,self).form_invalid(form)


class RevisarView(FormView):
	template_name = 'courses/review.html'
	form_class = ReviewForm
	success_url = '/HomeworksStudents/'
	id_course = 0
	id_homework = 0
	def get_context_data(self,**kwargs):
		context = super(RevisarView,self).get_context_data(**kwargs)
		self.id_course = self.kwargs['pk']
		self.id_homework = self.kwargs['pk_tarea']
		print(self.id_course)
		course = Course.objects.get(id = self.id_course)
		homeworks_students = Homework.objects.filter(is_master = False, curso = course)
		context['course'] = course
		context['homeworks_students'] = homeworks_students

		return context
	def form_valid(self,form,**kwargs):
		course_id = self.kwargs['pk']
		pk_tarea = self.kwargs['pk_tarea']
		course = Course.objects.get(id = course_id)
		homework = Homework.objects.get(id = pk_tarea)
		context = super(RevisarView,self).get_context_data(**kwargs)
		review = Review()
		review.descripcion = form.cleaned_data['descripcion']
		review.calificacion = form.cleaned_data['calificacion']
		review.tarea = homework
		review.user= homework.user
		review.save()
		self.success_url+=str(course_id)
		return super(RevisarView,self).form_valid(form)
	def form_invalid(self,form):
		return super(RevisarView,self).form_invalid(form)