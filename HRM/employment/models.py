from django.db import models


class Employment(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    national_id = models.CharField(max_length=255)
    year_of_birth = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    education_level = models.CharField(max_length=255)
    education_field = models.CharField(max_length=255)
    experience = models.CharField(max_length=1023)
    interests = models.CharField(max_length=1023)
    picture = models.CharField(max_length=1023)
    date_of_completion = models.DateField()
