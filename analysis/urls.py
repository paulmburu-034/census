from django.conf.urls import url
from analysis import views
app_name = 'analysis'
urlpatterns = [
    url('live_population/', views.alive_population_information, name='live_population'),
    url('death_population/', views.dead_population_information, name='death_population'),
    url('death_analysis/', views.death_analysis_information, name='death_analysis'),
    url(r'^$', views.analysis_information, name='analysis'),
]
