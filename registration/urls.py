from django.conf.urls import url
from . import views
app_name = 'registration'
urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^add_birth/$', views.birth_registration, name='birth_registration'),
    url(r'^(?P<person_id>[0-9]+)/add_death/$', views.death_registration, name='death_registration'),
    url(r'^cert_management/$', views.certificate_management, name='certificate_management'),
    url(r'^birth_search/$', views.birth_search, name='birth_search'),


]
