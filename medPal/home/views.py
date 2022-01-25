from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from medPal.diseases.models import Disease
from medPal.home.forms import ContactsForm, SearchForm


class HomeView(FormView):
    template_name = 'home/index.html'
    form_class = SearchForm

    def form_valid(self, form):
        disease_name = form.cleaned_data['disease_name']
        disease = Disease.objects.get(name=disease_name)
        context = {
            'disease': disease,
            'symptoms': ", ".join([str(d) for d in disease.symptoms.all()]),
        }
        return render(self.request, 'diseases/disease.html', context)


class AboutView(TemplateView):
    template_name = 'home/about.html'


class ContactsView(FormView):
    template_name = 'home/contacts.html'
    form_class = ContactsForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.send_support_email()
        return super().form_valid(form)
