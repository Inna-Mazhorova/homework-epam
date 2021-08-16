# Generated by Django 3.2.6 on 2021-08-16 12:14

from __future__ import unicode_literals

from django.db import migrations, models


def define_objects(apps, schema_editor):

    Person = apps.get_model("teacher", "Person")
    for person in Person.objects.all():
        person.name = "%s %s" % (person.first_name, person.last_name)
        person.save()

    Teacher = apps.get_model("teacher", "Teacher")
    for teacher in Teacher.objects.all():
        teacher.name = "%s %s" % (teacher.first_name, teacher.last_name)
        teacher.save()
    Student = apps.get_model("teacher", "Student")
    for student in Student.objects.all():
        student.name = "%s %s" % (student.first_name, student.last_name)
        student.save()

    Homework = apps.get_model("teacher", "Homework")
    for homework in Homework.objects.all():
        homework.text = "%s %s" % (homework.text)
        homework.save()

    HomeworkResult = apps.get_model("teacher", "HomeworkResult")
    for hwresult in HomeworkResult.objects.all():
        hwresult.homework = "%s %s" % (hwresult.homework)
        hwresult.save()


class Migration(migrations.Migration):

    dependencies = [
        ("teacher", "0001_initial"),
    ]

    operations = [migrations.RunPython(define_objects)]