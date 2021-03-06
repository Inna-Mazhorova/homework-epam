import datetime

from freezegun import freeze_time

from homework5 import hw5_task01


def test_class_teacher():

    teacher = hw5_task01.Teacher("Shadrin", "Daniil")
    student = hw5_task01.Student("Petrov", "Roman")
    assert teacher.last_name == "Shadrin"
    assert teacher.first_name == "Daniil"
    with freeze_time("2020-01-14 12:00:01"):
        expired_homework = teacher.create_homework("Learn functions", 10)
    assert expired_homework.text == "Learn functions"
    assert expired_homework.created == datetime.datetime(2020, 1, 14, 12, 0, 1)
    assert expired_homework.is_active() == False
    assert student.do_homework(expired_homework) == None
    assert isinstance(expired_homework, hw5_task01.Homework)


def test_class_student():
    student = hw5_task01.Student("Petrov", "Roman")
    assert student.last_name == "Petrov"
    assert student.first_name == "Roman"


def test_class_homework():
    oop_homework = hw5_task01.Homework("create 2 simple classes", 5)
    student = hw5_task01.Student("Petrov", "Roman")
    assert oop_homework.text == "create 2 simple classes"
    assert oop_homework.deadline == datetime.timedelta(days=5)
    assert oop_homework.is_active() == True
    assert student.do_homework(oop_homework) == oop_homework
