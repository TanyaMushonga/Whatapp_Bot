from django.db import models


class UserResponse(models.Model):
    user_id = models.CharField(max_length=255)  # Assuming user_id is a string
    user_name = models.CharField(max_length=255)
    question = models.TextField()
    response = models.TextField()

    class Meta:
        # To ensure each user can only have one response per questionfrom django.db import models
        unique_together = ('user_id', 'question')

# Create your models here.
# Assuming the number is a string


class User(models.Model):
    # Assuming the number is a string
    number = models.CharField(max_length=255)
    question_index = models.IntegerField(default=0)

    def __str__(self):
        return self.number


class UserDetails(models.Model):
    full_name = models.CharField(max_length=200)
    age = models.IntegerField()
    location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    experience = models.TextField()
    expenditure = models.TextField()
    fishpond = models.BooleanField()


class PersonalDetails(models.Model):
    phone_number = models.CharField(max_length=20)
    sender_name = models.CharField(max_length=100)
    responses = models.TextField()

    def __str__(self):
        return self.sender_name
