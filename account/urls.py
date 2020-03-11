from django.conf.urls import url
from . import views
app_name = 'account'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^$', views.dashboard, name='dashboard'),

]