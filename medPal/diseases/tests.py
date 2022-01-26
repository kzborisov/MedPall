from django.test import TestCase

from medPal.diseases.models import Symptom, Category, Disease


class DiseaseModelsTests(TestCase):
    def setUp(self):
        self.symptom = Symptom.objects.create(
            name="symptom"
        )
        self.category = Category.objects.create(
            name="test system"
        )
        self.disease = Disease.objects.create(
            name="disease",
            description='description',
            category=self.category,
        )
        self.disease.symptoms.add(self.symptom)

    def test_symptom_model(self):
        s = self.symptom
        self.assertTrue(isinstance(s, Symptom))
        self.assertEqual(str(s), 'symptom')

    def test_category_model(self):
        c = self.category
        self.assertTrue(isinstance(c, Category))
        self.assertEqual(str(c), 'test system')

    def test_disease_model(self):
        d = self.disease
        self.assertTrue(isinstance(d, Disease))
        self.assertEqual(str(d), "1: disease")
