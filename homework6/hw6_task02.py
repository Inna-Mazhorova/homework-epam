import datetime
from collections import defaultdict
from typing import Union

"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
"""


class DeadlineError(Exception):
    pass


class Homework:
    def __init__(self, text: str, deadline: int) -> None:
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()
        if deadline < 1:
            raise Exception("Deadline must be more than 1 day")

    def is_active(self) -> bool:
        date_due = self.created + self.deadline
        return datetime.datetime.now() <= date_due


class HomeworkResult:
    def __init__(self, author: "SomeClass", homework: Homework, solution: str) -> None:
        if not isinstance(homework, Homework):
            raise ValueError("Parameter you gave is not a Homework object")
        self.homework = homework
        self.author = author
        self.solution = solution
        self.created = datetime.datetime.now()


class Person:
    def __init__(self, last_name: str, first_name: str) -> None:
        self.last_name = last_name
        self.first_name = first_name


class Teacher(Person):
    homework_done = defaultdict(set)

    def create_homework(self, text: str, deadline: int) -> Homework:
        return Homework(text, deadline)

    def check_homework(self, homework_result: HomeworkResult):
        if len(homework_result.solution) < 5:
            return False

        self.homework_done[homework_result.homework] = homework_result.solution
        return True

    @classmethod
    def reset_results(cls, homework_unit=None):

        if homework_unit:
            del cls.homework_done[homework_unit]
        else:
            cls.homework_done.clear()


class Student(Person):
    def do_homework(self, homework: str, solution: str) -> Union[None, "Homework"]:
        if not homework.is_active():
            raise DeadlineError("You are late")

        return HomeworkResult(self, homework, solution)
