from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Rezyser(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Reżyserzy'


class Film(models.Model):
    text = models.CharField(max_length = 200)
    rezyser = models.ForeignKey(Rezyser, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Filmy'

    def __str__(self):
        return self.text

class Ocena(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'oceny'

    def __str__(self):
        if (len(self.text) >50):
            return f"{self.text[:50]}..."
        else:
            return self.text