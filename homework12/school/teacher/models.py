import datetime
from datetime import timedelta
from typing import Union

from django.db import models
from django.utils import timezone


# Create your models here.
class DeadlineError(Exception):
    pass


class Person(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"


class Teacher(Person, models.Model):
    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"


class Student(Person, models.Model):
    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"


class Homework(models.Model):
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    text = models.TextField()
    deadline = models.DurationField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text


class HomeworkResult(models.Model):

    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField()

    def __str__(self) -> str:
        return self.homework


def is_active(homework: Homework) -> bool:
    return timezone.now() - homework.created < homework.deadline


def create_homework(teacher: Teacher, text: str, deadline: int):
    return Homework(author=teacher, text=text, deadline=timedelta(days=deadline))


def do_homework(
    student: Student, homework: Homework, solution: str
) -> Union[None, "SomeClass"]:
    if not is_active(homework):
        raise DeadlineError("You are late")

    return HomeworkResult(author=student, homework=homework, solution=solution)


def check_homework(homework_result: "SomeClass") -> bool:
    homework_result.done = len(homework_result.solution) > 5
