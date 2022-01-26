from django.core.exceptions import ValidationError

from medPal.diseases.models import Disease


def validate_disease_exists(disease_name):
    disease = Disease.objects.filter(name=disease_name)
    if not disease.exists():
        raise ValidationError(f'Disease {disease_name} does not exists in the database!')
