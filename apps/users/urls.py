from django.conf.urls import patterns, include, url
from .views import PanelView,RegistrateView,LogOut,LoginView
from apps.home.views import HomeView
urlpatterns = patterns('',
	url(r'^$',PanelView.as_view(),name='panel'),
	url(r'^login$',LoginView.as_view(),name='login'),
	url(r'^registrateGratis$',RegistrateView.as_view(),name='registrate'),
	url(r'^inicio$',LogOut,name='logout'),
	url(r'^home$',HomeView.as_view(),name='home'),
)