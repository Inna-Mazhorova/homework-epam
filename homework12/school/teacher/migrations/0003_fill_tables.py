from __future__ import unicode_literals

from django.db import migrations, models
from teacher.models import *


def define_objects(apps, schema_editor):

    lazy_student = Student(first_name="Petrov", last_name="Roman")
    lazy_student.save()
    good_student = Student(first_name="Sokolov", last_name="Lev")
    good_student.save()

    opp_teacher = Teacher(first_name="Shadrin", last_name="Daniil")
    opp_teacher.save()
    advanced_python_teacher = Teacher(first_name="Smetanin", last_name="Aleksandr")
    advanced_python_teacher.save()

    oop_hw = opp_teacher.create_homework(text="Learn OOP", deadline=5)
    oop_hw.save()
    docs_hw = advanced_python_teacher.create_homework(text="Read docs", deadline=6)
    docs_hw.save()

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw")

    result_3 = lazy_student.do_homework(oop_hw, "bad")
    result_4 = lazy_student.do_homework(docs_hw, "bad")

    list(
        map(
            opp_teacher.check_homework,
            [
                result_1,
                result_2,
                result_3,
                result_4,
            ],
        )
    )

    result_1.save()
    result_2.save()
    result_3.save()
    result_4.save()


class Migration(migrations.Migration):
    dependencies = [
        ("teacher", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(define_objects),
    ]
