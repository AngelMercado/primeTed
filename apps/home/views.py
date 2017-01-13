from django.shortcuts import render
from django.views.generic import TemplateView,RedirectView
from apps.courses.models import Course
from braces.views import LoginRequiredMixin
class IndexView(LoginRequiredMixin,RedirectView):
	url = '/panel'
	login_url=login_url='/home'

	def get_context_data(self,**kwargs):
		context = super(IndexView,self).get_context_data(**kwargs)
		#if self.request.user.is_master:
		#	context['courses']= Course.objects.all()
		#else:
		context['courses']= Course.objects.filter(user=self.request.user)
		return context
class HomeView(TemplateView):
	template_name = 'home/index1.html'

class RegisterView(TemplateView):
	template_name = 'home/index2.html'
		