import datetime
from typing import Any, Union

"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
"""


class Teacher:
    def __init__(self, last_name: str, first_name: str) -> None:
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text: str, deadline: int) -> "SomeClass":
        return Homework(text, deadline)


class Homework:
    def __init__(self, text: str, deadline: int) -> None:
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()
        if deadline < 1:
            raise Exception("Deadline must be >= 1 day")

    def is_active(self) -> Any:
        date_due = self.created + self.deadline
        return datetime.datetime.now() <= date_due


class Student:
    def __init__(self, last_name: str, first_name: str) -> None:
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework: str) -> Union[None, "Homework"]:
        if not homework.is_active():
            print("You are late")
            return None
        else:
            return homework
