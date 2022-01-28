from django.db import models


class Symptom(models.Model):
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.name


class Category(models.Model):

    CHOICES = (
        ('Integumentary System', 'Integumentary System'),
        ('Skeletal System', 'Skeletal System'),
        ('Muscular System', 'Muscular System'),
        ('Lymphatic System', 'Lymphatic System'),
        ('Respiratory System', 'Respiratory System'),
        ('Digestive System', 'Digestive System'),
        ('Nervous System', 'Nervous System'),
        ('Endocrine System', 'Endocrine System'),
        ('Cardiovascular System', 'Cardiovascular System'),
        ('Urinary System', 'Urinary System'),
        ('Reproductive System', 'Reproductive Systems'),
    )

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=max(len(c[0]) for c in CHOICES),
        choices=CHOICES,
        default='integumentary',
        unique=True,
    )

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    symptoms = models.ManyToManyField(Symptom)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.id}: {self.name}"
