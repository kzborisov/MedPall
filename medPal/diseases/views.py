from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from medPal.diseases.models import Disease, Category


class CategoriesView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'diseases/categories.html'
    context_object_name = 'categories'


class DiseaseView(LoginRequiredMixin, ListView):
    model = Disease
    template_name = 'diseases/disease.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disease'] = Disease.objects.get(pk=self.kwargs['pk'])
        context['symptoms'] = ", ".join(
            [str(d) for d in context['disease'].symptoms.all()]
        )
        return context


class CategoryView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'diseases/diseases-by-category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['pk'])
        context['diseases'] = Disease.objects.all(). \
            filter(category=self.kwargs['pk'])
        return context
