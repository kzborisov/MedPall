from django.contrib import admin

from medPal.diseases.models import Disease, Symptom, Category


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    sortable_by = ('name',)


@admin.register(Symptom)
class Symptoms(admin.ModelAdmin):
    list_filter = ('name',)
    sortable_by = ('name',)


@admin.register(Category)
class Symptoms(admin.ModelAdmin):
    list_filter = ('name',)
    sortable_by = ('name',)
