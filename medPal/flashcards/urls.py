from django.urls import path

from medPal.flashcards.views import CreateFlashcardView, FlashcardIndex, PractiseFlashcardView

urlpatterns = [
    path('', FlashcardIndex.as_view(), name='flashcards'),
    path('create/', CreateFlashcardView.as_view(), name='create flashcard'),
    path('practise/', PractiseFlashcardView.as_view(), name='practise'),
]
