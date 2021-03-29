from django.shortcuts import render
from django.views.generic import TemplateView

class MainIndex(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        self.request.title = 'hiha'
        return super().get_context_data(**kwargs)
