import datetime

from homework5 import hw5_task01


def test_classes():
    teacher = hw5_task01.Teacher("Shadrin", "Daniil")
    student = hw5_task01.Student("Petrov", "Roman")
    expired_homework = teacher.create_homework("Learn functions", -1)
    oop_homework = hw5_task01.Homework("create 2 simple classes", 5)
    assert teacher.last_name == "Shadrin"
    assert teacher.first_name == "Daniil"
    assert student.last_name == "Petrov"
    assert student.first_name == "Roman"
    assert expired_homework.text == "Learn functions"
    assert oop_homework.text == "create 2 simple classes"
    assert oop_homework.deadline == datetime.timedelta(days=5)
    assert oop_homework.is_active_method() == True
    assert expired_homework.is_active_method() == False
    assert student.do_homework_method(expired_homework) == None
    assert student.do_homework_method(oop_homework) == oop_homework
