from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView, ListView

from medPal.flashcards.models import Flashcard


class FlashcardIndex(LoginRequiredMixin, TemplateView):
    template_name = 'flashcards/flashcards.html'


class CreateFlashcardView(LoginRequiredMixin, CreateView):
    template_name = 'flashcards/create-flashcard.html'
    model = Flashcard
    fields = ['name', 'description']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user_id = self.request.user
        obj.save()
        return redirect('flashcards')


class PractiseFlashcardView(LoginRequiredMixin, ListView):
    template_name = 'flashcards/practise-flashcards.html'
    model = Flashcard
    context_object_name = 'flashcard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_flashcard'] = Flashcard.objects.filter(
            user_id=self.request.user
        ).order_by('?').first()
        return context
