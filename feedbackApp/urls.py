from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.dashboard, name = "root") #root é utilizado para retornar pra cá caso clique na logo
]