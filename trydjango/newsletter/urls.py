from django.conf.urls import url
from . import views

app_name = 'newsletter'
urlpatterns = [
    url(r'^$', views.home, name = 'newsletter_home'),
    url(r'^contact/', views.contact, name = 'newsletter_contact'),
]
