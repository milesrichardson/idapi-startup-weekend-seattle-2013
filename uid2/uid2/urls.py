from django.conf.urls import patterns, include, url
from webapp.views import *
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.views.generic.simple import direct_to_template
from webapp.views import companyprofile, profile
admin.autodiscover()
import api 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', home, {'template': 'index2.html'},name='home'),
                       url(r'^base2$', home, {'template': 'base2.html'},name='base2'),                       
                       url(r'^thanks$', TemplateView.as_view(template_name="thanks.html"), name='thanks'),
                       url(r'^about$', home, {'template': 'about.html'},name='about'),
                       url(r'^contact$', TemplateView.as_view(template_name="contact.html"),name='contact'),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^api/person/id=(\d{0,9})$','webapp.views.profile'),
                       url(r'^companyprofile=(\d{0,9})$','webapp.views.companyprofile'),
                       url(r'^redfin1',redfin,{'template': "Identity.html"}),
                       url(r'^redfin2',direct_to_template,{'template': "Confirmation.html"}),
                       url(r'^admin/', include(admin.site.urls)),   
                       # url(r'^accounts/profile/$', TemplateView.as_view(template_name="analytics.html"), name='analytics'),
                       # url(r'^accounts/profile/', 'viprmain.views.analytics'),
                       (r'^accounts?/', include('registration.urls')),
                       #url(r'^login/$',auth_views.login,{'template_name': 'login.html'},name='auth_login'),
                       url(r'^api/', include(api.urls)),
                       url(r'^verify', verify), # Redirects
)
print 'staticroot:'+settings.STATIC_ROOT
urlpatterns += patterns('',(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,'show_indexes': True }))
