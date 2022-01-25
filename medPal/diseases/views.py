from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from medPal.diseases.models import Disease, Category
from medPal.home.forms import SearchForm


@login_required
def categories(request):
    context = {
        'categories': Category.objects.all(),
    }

    return render(request, 'diseases/categories.html', context)


@login_required
def disease(request, pk):
    disease = Disease.objects.get(pk=pk)
    symptoms = ", ".join([str(d) for d in disease.symptoms.all()])
    context = {
        'disease': disease,
        'symptoms': symptoms,
    }

    return render(request, 'diseases/disease.html', context)


@login_required
def category(request, pk):
    c = Category.objects.get(pk=pk)
    d = Disease.objects.all().filter(category=pk)
    context = {
        'category': c,
        'diseases': d,
    }

    return render(request, 'diseases/diseases-by-category.html', context)


@login_required
def search_disease(request):
    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            disease = Disease.objects.get(name=form.cleaned_data['disease_name'])
            symptoms = ", ".join([str(d) for d in disease.symptoms.all()])
            context = {
                'disease': disease,
                'symptoms': symptoms,
            }

            return render(request, 'diseases/disease.html', context)
        else:
            return redirect('home')
