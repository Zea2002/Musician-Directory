from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    instrument_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
    album_name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.album_name
