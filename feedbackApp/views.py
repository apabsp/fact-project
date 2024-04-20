from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
app_name = 'feedbackApp'

def dashboard(req):
    return render(req, "feedbackApp/stretch.html")


