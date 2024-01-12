from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from core.models import Client

from core.form import ClientForm


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


def post_client(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST or None)
        if form.is_valid():
            # save the form data to model
            form.save()
            return redirect('customer/')

        context = {'form' : form}
        return render(request, "core/editable_form.html", context)

    context = {'form': form}
    return render(request, "core/editable_form.html", context)


def update_client(request, id):
    client = get_object_or_404(Client, pk=id)
    form = ClientForm(request.POST, instance=client)
    if request.method == "POST":
        form = ClientForm(request.POST or None)
        if form.is_valid():
            # save the form data to model
            form.save()
            return redirect('customer/')

        context = {'form' : form}
        return render(request, "core/editable_form.html", context)

    context = {'form' : form}
    return render(request, "core/editable_form.html", context)