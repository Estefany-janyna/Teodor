from django.urls import path
from formulario1.views import formulario
from . import views


urlpatterns = [
    path('', formulario, name='formulario'),
    path('', views.formulario, name='formulario'),
]
