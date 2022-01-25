from django.contrib.auth import get_user_model
from django.db import models


class Flashcard(models.Model):
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    user_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.id}: {self.name}"
