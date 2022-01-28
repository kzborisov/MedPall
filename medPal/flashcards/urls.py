from django.urls import path

from medPal.flashcards.views import CreateFlashcardView, FlashcardIndexView, PractiseFlashcardView

urlpatterns = [
    path('', FlashcardIndexView.as_view(), name='flashcards'),
    path('create-flashcard/', CreateFlashcardView.as_view(), name='create flashcard'),
    path('practise/', PractiseFlashcardView.as_view(), name='practise'),
]
