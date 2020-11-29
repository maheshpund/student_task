from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ creating role based user to identify user """
    ROLE_CHOICES = (
        ('STUDENT', 'student'),
        ('TEACHER', 'teacher'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name


class Teacher(models.Model):
    student = models.ForeignKey(Student,related_name='teachers',on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=20)

    def __str__(self):
        return self.teacher_name


class Subjects(models.Model):
    teacher = models.ForeignKey(Teacher,related_name='subjects',on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=20)