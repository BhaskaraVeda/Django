from django.db import models

# Create your models here.
class Student_details(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    student_phone_number = models.IntegerField()
    student_email = models.EmailField()

    def __str__(self):
        return self.name
