from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import Client

# Create your views here.

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class ClientView(TemplateView):
    template_name = 'core/index.html'

    def clients_list(self):
        return Client.objects.all()

    def get(self, request, *args, **kwargs):

        clients = self.clients_list()
        context = {'clients': clients}

        return render(request, self.template_name, context)