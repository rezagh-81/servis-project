from django.shortcuts import render
from django.views import generic

# Create your views here.


class DetailView (generic.TemplateView) :
    template_name = "homeapp/detail.html"