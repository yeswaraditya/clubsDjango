from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views.generic import TemplateView

class InnovationHomePageView(TemplateView):
    template_name = 'innovation.html'
