from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'app/index.html'


class Worlds(TemplateView):
    template_name = 'app/worlds.html'