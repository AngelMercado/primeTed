from django.conf.urls import patterns, include, url
from .views import CreateCourse,CourseDetailView,CourseListStudent,CreateHomework,Inscripcion,HomeworksCourse,HomeworksUser,HomeworksStudents,DeleteStudent,RevisarView,CourseActivityView
urlpatterns = patterns('',
	url(r'^CourseCreate/(?P<pk>\d+)/$',CreateCourse.as_view(),name='CourseCreate'),#el name es el indentificador de la vista
	url(r'^InfoCourse/(?P<pk>\d+)/$',CourseDetailView.as_view(),name='Info'),
	url(r'^ActivityCourse/(?P<pk>\d+)$',CourseActivityView.as_view(),name="Activities"),
	url(r'^listStudents/(?P<num>\d+)/$',CourseListStudent.as_view(),name='listStudents'),
	url(r'^CreateHomework/(?P<pk>\d+)/$',CreateHomework.as_view(),name='CreateHomework'),
	url(r'^Inscripcion/(?P<id_course>\d+)/$',Inscripcion.as_view(),name='Inscripcion'),
	url(r'^HomeworksCourse/(?P<pk>\d+)/$',HomeworksCourse.as_view(),name='HomeworksCourse'),
	url(r'^HomeworksUser/(?P<pk>\d+)/$',HomeworksUser.as_view(),name='HomeworksUser'),
	url(r'^HomeworksStudents/(?P<pk>\d+)/$',HomeworksStudents.as_view(),name='HomeworksStudents'),
	url(r'^DeleteStudent/(?P<pk_course>\d+)/(?P<pk_user>\d+)/$',DeleteStudent.as_view(),name='DeleteStudent'),
	url(r'^RevisarTareas/(?P<pk>\d+)/(?P<pk_tarea>\d+)/$',RevisarView.as_view(),name='revisar')
)