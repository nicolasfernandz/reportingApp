from django.conf.urls import url

from reporting import views as reporting_views

urlpatterns = [   
    
    
    url(r'^userRegistration/$', reporting_views.registration),
    
    
    url(r'^$', reporting_views.login, name='login'),
    url(r'^login/', reporting_views.login),
    
    
    url(r'^getReporting/', reporting_views.getReporting, name = 'Get Reporting'),
    url(r'^cierreToPDF/', reporting_views.campaignsToPDF),
    url(r'^logout', reporting_views.logout),
    
    
    url(r'^registration/', reporting_views.getRegistration),
    
    
    
    
]
