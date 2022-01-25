from django import forms
from django.core.mail import send_mail

from medPal.diseases.models import Disease


def disease_exists(name):
    if Disease.objects.filter(name=name).exists():
        return True
    return False


class ContactsForm(forms.Form):
    full_name = forms.CharField(
        max_length=60,
    )
    email = forms.EmailField()
    subject = forms.CharField(
        max_length=60,
    )
    message = forms.CharField(
        widget=forms.Textarea,
    )

    def send_support_email(self):
        subject = f"FROM: {self.cleaned_data['full_name']}: " \
                  + self.cleaned_data['subject']
        send_mail(
            subject,
            self.cleaned_data['message'],
            self.cleaned_data['email'],
            ['med.pall.app@gmail.com'],
            fail_silently=False,
        )
        send_mail(
            '[MedPall] Support',
            f"""
Dear {self.cleaned_data['full_name']},

Thank you for your email!
We will get back to you as soon as possible!

Best Regards,
MedPall Support
            """,
            self.cleaned_data['email'],
            [self.cleaned_data['email']],
            fail_silently=False,
        )


class SearchForm(forms.Form):
    disease_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'class': 'search-input'}
        ),
    )

    def clean_disease_name(self):
        name = self.cleaned_data['disease_name']
        if disease_exists(name):
            return name
        raise forms.ValidationError(f'Disease {name} does not exists in the database!')
