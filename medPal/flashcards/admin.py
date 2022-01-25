from django.contrib import admin

from medPal.flashcards.models import Flashcard


@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    sortable_by = ('name',)
