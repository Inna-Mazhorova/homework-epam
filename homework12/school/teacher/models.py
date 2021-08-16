from django.db import models


# Create your models here.
class Person(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Teacher(Person, models.Model):
    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Student(Person, models.Model):
    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Homework(models.Model):
    text = models.TextField()
    deadline = models.DurationField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class HomeworkResult(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    solution = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.homework
