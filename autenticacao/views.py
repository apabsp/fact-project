from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

class SignIn(View):
    def get(self,req): 
        if(req.user.is_authenticated): 
            return render(req, "../feedbackApp/templates/feedbackApp/app.html")
            pass #vamos redirecionar para o app feedbackApp

        return render(req, "/login.html/")
    #def post(self, req)
    def post(self,req):
        email = req.POST.get("email")
        password = req.POST.get("password")

        USER = auth.authenticate(email = email, password = password)
        if not USER:
            
            return render(req, 'autenticacao/signin.html')
        else:
            return render(req, "../feedbackApp/templates/feedbackApp/app.html")
