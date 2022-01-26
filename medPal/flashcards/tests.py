from django.contrib.auth.models import User
from django.test import TestCase

from medPal.flashcards.models import Flashcard


class FlashcardModelTests(TestCase):

    def setUp(self):
        self.flashcard = Flashcard(
            name='flashcard',
            description='description',
            user_id=User()
        )

    def test_flashcard_model(self):
        f = self.flashcard
        self.assertTrue(isinstance(f, Flashcard))
        self.assertEqual(str(f), "None: flashcard")
