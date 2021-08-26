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


class Teacher(Person):
    def create_homework(self, text: str, deadline: int) -> "SomeClass":
        return Homework(author=self, text=text, deadline=timedelta(days=deadline))

    def check_homework(self, homework_result: "SomeClass") -> bool:
        homework_result.done = len(homework_result.solution) > 5


class Homework(models.Model):
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    text = models.TextField()
    deadline = models.DurationField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text

    def is_active(self) -> bool:
        return timezone.now() - self.created < self.deadline


class Student(Person):
    def do_homework(
        self, homework: "SomeClass", solution: str
    ) -> Union[None, "SomeClass"]:
        if not homework.is_active(self):
            raise DeadlineError("You are late")

        return HomeworkResult(author=self, homework=homework, solution=solution)


class HomeworkResult(models.Model):

    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField()

    def __str__(self) -> str:
        return self.homework
