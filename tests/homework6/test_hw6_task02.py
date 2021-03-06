import datetime

import pytest
from freezegun import freeze_time

from homework6 import hw6_task02

opp_teacher = hw6_task02.Teacher("Shadrin", "Daniil")
advanced_python_teacher = hw6_task02.Teacher("Smetanin", "Aleksandr")
lazy_student = hw6_task02.Student("Petrov", "Roman")
good_student = hw6_task02.Student("Sokolov", "Lev")

oop_hw = opp_teacher.create_homework("Learn OOP", 1)
docs_hw = opp_teacher.create_homework("Read docs", 5)

result_1 = good_student.do_homework(oop_hw, "I have done this hw")
result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
result_3 = lazy_student.do_homework(docs_hw, "done")


def test_created():

    assert opp_teacher.last_name == "Shadrin"
    assert advanced_python_teacher.first_name == "Aleksandr"


def test_expired_homework_created_and_error_in_do_homework_method():

    with freeze_time("2020-01-14 12:00:01"):
        expired_homework = opp_teacher.create_homework("Learn functions", 10)
    assert expired_homework.text == "Learn functions"
    assert expired_homework.created == datetime.datetime(2020, 1, 14, 12, 0, 1)
    assert expired_homework.is_active() == False

    with pytest.raises(hw6_task02.DeadlineError, match="You are late"):
        lazy_student.do_homework(expired_homework, "I've done this")
    assert isinstance(expired_homework, hw6_task02.Homework)


def test_student_created():

    assert lazy_student.last_name == "Petrov"
    assert good_student.first_name == "Lev"


def test_active_homework_created():

    assert oop_hw.text == "Learn OOP"
    assert oop_hw.deadline == datetime.timedelta(days=1)
    assert oop_hw.is_active() == True


def test_homeworkresult_created():

    assert isinstance(result_3, hw6_task02.HomeworkResult)


def test_error_in_homework_result():
    with pytest.raises(ValueError, match="Parameter you gave is not a Homework object"):
        hw6_task02.HomeworkResult(lazy_student, "fff", "Solution")


def test_check_hw_and_reset_methods():
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = hw6_task02.Teacher.homework_done
    assert temp_1 == temp_2
    len_before_reset = len(hw6_task02.Teacher.homework_done)
    assert len_before_reset == 1
    hw6_task02.Teacher.reset_results()
    len_after_reset = len(hw6_task02.Teacher.homework_done)
    assert len_after_reset == 0
