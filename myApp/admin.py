from django.contrib import admin
from .models import Student
from .forms import StudentForm


class StudentAdmin(admin.ModelAdmin):
	form = StudentForm

# Register your models here.
admin.site.register(Student, StudentAdmin)