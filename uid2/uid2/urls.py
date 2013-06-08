from django.conf.urls import patterns, include, url
from webapp.views import *
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', home, {'template': 'index.html'},name='home'),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),
                       # url(r'^post$', post, {'template': 'post.html'},name='post'),
                       # url(r'^thanks$', TemplateView.as_view(template_name="thanks.html"), name='thanks'),
                       # url(r'^about$', home, {'template': 'about.html'},name='about'),
                       # url(r'^contact$', TemplateView.as_view(template_name="contact.html"),name='contact'),
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # url(r'^admin/', include(admin.site.urls)),                       
                       # url(r'^analytics/', 'viprmain.views.analytics'),
                       # url(r'^accounts/profile/', 'viprmain.views.analytics'),
                       # (r'^accounts?/', include('registration.urls')),
                       #url(r'^login/$',auth_views.login,{'template_name': 'login.html'},name='auth_login'),
)
