from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
	
	url(r'^',include('apps.home.urls')),
	url(r'^panel/$',include('apps.users.urls')),
	url(r'^',include('apps.users.urls',namespace='users')),
	url(r'^',include('apps.courses.urls',namespace='courses')),
    url(r'^admin/', include(admin.site.urls)),
    #url de social_auth
    url('',include('social.apps.django_app.urls',namespace='social')),
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

