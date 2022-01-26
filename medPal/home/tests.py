from unittest.mock import patch

from django.core import mail
from django.core.exceptions import ValidationError
from django.test import TestCase

from medPal.home.forms import ContactsForm
from medPal.home.validators import validate_disease_exists


class ContactsFormTestCase(TestCase):

    def test_send_support_email(self):
        form_data = {
            'full_name': 'Test Testov',
            'email': 'test@email.com',
            'subject': "Test subject",
            'message': 'Test Message'
        }

        form = ContactsForm(form_data)
        subject = 'FROM: Test Testov: Test subject'
        if form.is_valid():
            form.send_support_email()

        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(mail.outbox[0].subject, subject)


class TestValidateDiseaseExists(TestCase):

    @patch('medPal.diseases.models.Disease.objects')
    def test_validate_disease__when_disease_exists(self, mock_disease):
        mock_disease.all.return_value = [
            'name',
            'description',
            'symptoms',
            'category'
        ]
        actual = validate_disease_exists('name')
        self.assertIsNone(actual)

    def test_validate_disease__when_disease_does_not_exist(self):
        with self.assertRaises(ValidationError) as context:
            validate_disease_exists('non existing name')

        self.assertIsNotNone(context.exception)
