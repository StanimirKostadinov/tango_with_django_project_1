from django.conf.urls import url
from DJANGO_app import views

urlpatterns = [
url(r'^$', views.index_django, name='index_django'),
]
