from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import logout
from . import models
import pandas as pd

class FeedBackView(View):
    def get(self, req):
        if(not req.user.is_authenticated):
            return redirect("autenticacao:root")
        
        user = User.objects.get(username=req.user.username)
        groups = models.Grupo.objects.filter(professor=user)

        context = {
            "user": user,
            "groups": groups
        }
        
        return render(req, "feedbackApp/app.html", context=context)


    def post(self, req):
        if(not req.user.is_authenticated):
            return redirect("autenticacao:root")
        
        action = req.POST.get("action")

        user = User.objects.get(username=req.user.username)
        
        context = {
            "user": user
        }

        if(action == "addGroup"):
            return self.addGroup(req, context)

    
    def addGroup(self, req, context):
        groupName = req.POST.get("groupName")
        
        group = models.Grupo.objects.create(nomeDoGrupo=groupName, professor=context["user"])
        group.save()

        return render(req, "feedbackApp/app.html", context=context)


class GroupView(View):
    def get(self, req, id):
        if(not req.user.is_authenticated):
            return redirect("autenticacao:root")
        
        group = models.Grupo.objects.filter(pk=id)

        if(not group.exists()):
            return redirect("feedbackApp:root")
        
        context = {
            "group": group[0]
        }
        
        return render(req, "feedbackApp/group.html", context=context)
    

    def post(self, req, id):
        if(not req.user.is_authenticated):
            return redirect("autenticacao:root")
        
        group = models.Grupo.objects.filter(pk=id)

        if(not group.exists()):
            return redirect("feedbackApp:root")
        
        context = {
            "group": group[0]
        }

        #! TODO FAZER VERIFICACAO SE O ARQUIVO PERTENCE A ESSES TIPOS DE APPLICATION:
        #! "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        #! ou
        #! "application/vnd.ms-excel" 

        file = req.FILES["file"]
        df = pd.read_excel(file)

        print(df)

        return render(req, "feedbackApp/group.html", context=context)

def logoutFunction(req):
    logout(req)
    return redirect("autenticacao:root")
        