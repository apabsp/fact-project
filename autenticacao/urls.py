from django.urls import path
from . import views

app_name = 'autenticacao'
urlpatterns = [

    path('', views.SignIn.as_view()) # não precisamos de signup por agora. Pretendemos fzr registro com superuser

]