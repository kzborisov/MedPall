from django.contrib.auth.decorators import login_required
from django.urls import path

from medPal.flashcards.views import CreateFlashcardView, FlashcardIndex, PractiseFlashcardView

urlpatterns = [
    path('', login_required(FlashcardIndex.as_view()), name='flashcards'),
    path('create/', login_required(CreateFlashcardView.as_view()), name='create'),
    path('practise/', login_required(PractiseFlashcardView.as_view()), name='practise'),
]
