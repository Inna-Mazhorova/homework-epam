from django.contrib import admin

from .models import Homework, HomeworkResult, Person, Student, Teacher

# Register your models here.

admin.site.register(Person)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Homework)
admin.site.register(HomeworkResult)
