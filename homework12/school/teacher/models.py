import datetime
from collections import defaultdict
from typing import Union

from django.db import models


# Create your models here.
class Homework(models.Model):
    text = models.TextField()
    deadline = models.DurationField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text

    def is_active(self) -> bool:
        date_due = self.created + self.deadline

        return datetime.datetime.now() <= date_due


class Person(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"


class Teacher(Person, models.Model):
    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"

    homework_done = defaultdict(set)

    def create_homework(self, text: str, deadline: int):
        return Homework(text, deadline)

    def check_homework(self, homework_result) -> bool:
        if len(homework_result.solution) < 5:
            return False

        self.homework_done[homework_result.homework] = homework_result.solution
        return True

    @classmethod
    def reset_results(cls, homework_unit: Homework = None) -> None:

        if homework_unit:
            del cls.homework_done[homework_unit]
        else:
            cls.homework_done.clear()


class Student(Person, models.Model):
    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"

    def do_homework(self, homework: str, solution: str) -> Union[None, "Homework"]:
        return HomeworkResult(self, homework, solution)


class HomeworkResult(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    solution = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.homework
