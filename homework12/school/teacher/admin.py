from django.contrib import admin
from .models import Person, Teacher, Student, Homework, HomeworkResult

# Register your models here.

admin.site.register(Person)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Homework)
admin.site.register(HomeworkResult)
