from django.db import models

# Create your models here.
class Student(models.Model):
    """docstring for Student."""
    gender_choices=(
        ('M','Male'),
        ('F','Female')
    )
    roll_no=models.IntegerField()
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/")
    full_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    gender = models.CharField(choices=gender_choices, max_length=100)

    def __str__(self):
        return self.full_name
