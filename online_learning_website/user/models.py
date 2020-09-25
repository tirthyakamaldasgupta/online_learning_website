from django.db import models
from django.contrib.auth.models import User

class AdditionalStudentDetail(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

class AdditionalInstructorDetail(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)