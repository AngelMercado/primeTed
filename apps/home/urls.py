from django.conf.urls import patterns, include, url
from .views import IndexView,RegisterView
urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^registerPage/$',RegisterView.as_view())
)