from django import forms

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
