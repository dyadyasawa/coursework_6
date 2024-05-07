from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


class StartPageView(TemplateView):

    template_name = 'mailings_app/index.html'

