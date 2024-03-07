from django.db import models

class UserInfor(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_number = models.CharField(max_length=20)
    details = models.TextField()

# Create your models here.
class FishTypes(models.Model):
    fish_type = models.CharField(max_length=100)
    description = models.TextField()
    feeding_schedule = models.TextField()
    maturity_period = models.TextField()
    fish_size = models.TextField()


class Pond(models.Model):
    action = models.CharField(max_length=100)
    youtubeUrl = models.URLField()

class Disease(models.Model):
    disease_type = models.TextField()
    disease_name = models.CharField(max_length=100)
    symptoms = models.TextField()
    causes = models.TextField()
    impact = models.TextField()
    imgUrl = models.URLField()
    treatment_method = models.TextField()  # Corrected field name
    medication_type = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    treatment_duration = models.CharField(max_length=100)
    prevention_strategies = models.TextField()
    types_of_fish_affected_mostly = models.TextField()

    def __str__(self):
        return self.disease_name