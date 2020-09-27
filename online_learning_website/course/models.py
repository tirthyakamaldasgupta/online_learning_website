from django.db import models
from user.models import AdditionalStudentDetail, AdditionalInstructorDetail

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, null=False, max_length=255)
    slug = models.SlugField(unique=True, null=False, max_length=255)


class SubCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, null=False, max_length=255)
    category_id = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=False, max_length=255)

class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=False, max_length=255)
    subcategory_id = models.ForeignKey(SubCategory, null=False, on_delete=models.CASCADE)
    instructor_id = models.ForeignKey(AdditionalInstructorDetail, null=False, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, max_length=255)