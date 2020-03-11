from django.conf.urls import url
from . import views
app_name = 'certmanagement'
urlpatterns = [
    #url(r'^$', views.birth_search(), name='home'),
    url(r'^birth_search/$', views.birth_search, name='birth_search'),
    url(r'^death_search/$', views.death_search, name='death_search'),
    url(r'^(?P<id>\d+)/birth_applicant/$', views.view_birth_applicant, name='birth_applicant_detail'),
    url(r'^(?P<id>\d+)/death_applicant/$', views.view_death_applicant, name='death_applicant_detail'),
    url(r'^(?P<id>\d+)/print_birth_certificate/$', views.print_birth_certificate, name='print_birth_certificate'),
    url(r'^(?P<id>\d+)/print_death_certificate/$', views.print_death_certificate, name='print_death_certificate'),

]
