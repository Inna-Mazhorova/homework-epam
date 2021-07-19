import datetime

import pytest
from freezegun import freeze_time

from homework6.hw6_task02 import (DeadlineError, Homework, HomeworkResult,
                                  Student, Teacher)


def test_class_teacher():
    opp_teacher = Teacher("Shadrin", "Daniil")
    advanced_python_teacher = Teacher("Smetanin", "Aleksandr")
    lazy_student = Student("Petrov", "Roman")
    good_student = Student("Sokolov", "Lev")
    assert opp_teacher.last_name == "Shadrin"
    assert advanced_python_teacher.first_name == "Aleksandr"
    with freeze_time("2020-01-14 12:00:01"):
        expired_homework = opp_teacher.create_homework("Learn functions", 10)
    assert expired_homework.text == "Learn functions"
    assert expired_homework.created == datetime.datetime(2020, 1, 14, 12, 0, 1)
    assert expired_homework.is_active() == False
    with pytest.raises(DeadlineError, match="You are late"):
        lazy_student.do_homework(expired_homework, "I've done this")
    assert isinstance(expired_homework, Homework)


def test_class_student():
    lazy_student = Student("Petrov", "Roman")
    good_student = Student("Sokolov", "Lev")

    assert lazy_student.last_name == "Petrov"
    assert good_student.first_name == "Lev"


def test_class_homework():
    opp_teacher = Teacher("Shadrin", "Daniil")
    advanced_python_teacher = Teacher("Smetanin", "Aleksandr")
    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    assert oop_hw.text == "Learn OOP"
    assert oop_hw.deadline == datetime.timedelta(days=1)
    assert oop_hw.is_active() == True


def test_class_homeworkresult():
    lazy_student = Student("Petrov", "Roman")
    good_student = Student("Sokolov", "Lev")
    opp_teacher = Teacher("Shadrin", "Daniil")
    advanced_python_teacher = Teacher("Smetanin", "Aleksandr")
    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)
    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    assert isinstance(result_3, HomeworkResult)
    with pytest.raises(ValueError, match="Parameter you gave is not a Homework object"):
        HomeworkResult(lazy_student, "fff", "Solution")

    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2
    len_before_reset = len(Teacher.homework_done)
    assert len_before_reset == 1
    Teacher.reset_results()
    len_after_reset = len(Teacher.homework_done)
    assert len_after_reset == 0
