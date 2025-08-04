from django.db import models

NATIONALITY_CHOICES = [
    ('USA', 'United States'),
    ('BRA', 'Brazil')
]


# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField(null=True, blank=True)
    nationality = models.CharField(choices=NATIONALITY_CHOICES, 
                                max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
