"""
Definition of urls for faithapp
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import webpage.forms
import webpage.views
import faithapi.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', webpage.views.home, name='home'),
    url(r'^contact$', webpage.views.contact, name='contact'),
    url(r'^about', webpage.views.about, name='about'),
    
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'webpage/login.html',
            'authentication_form': webpage.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]

faithapi.views.append_urls(urlpatterns);
