from django.core.mail import send_mail
from django.shortcuts import render, redirect

from medPal.home.forms import ContactsForm, SearchForm


def home(request):
    if request.method == 'POSt':
        form = SearchForm(request.POST)
    else:
        form = SearchForm()

    context = {
        'form': form,
    }
    return render(request, 'home/index.html', context)


def about(request):
    return render(request, 'home/about.html')


def contacts(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            subject = f"FROM: {form.cleaned_data['full_name']}: " + form.cleaned_data['subject']
            send_mail(
                subject,
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                ['med.pall.app@gmail.com'],
                fail_silently=False,
            )
            send_mail(
                '[MedPall] Support',
                f"""
                Dear {form.cleaned_data['full_name']},
                
                Thank you for your email!
                We will get back to you as soon as possible!
                
                Best Regards,
                MedPall Support
                """,
                form.cleaned_data['email'],
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            return redirect('home')
    else:
        form = ContactsForm()
    context = {
        'form': form
    }
    return render(request, 'home/contacts.html', context)
