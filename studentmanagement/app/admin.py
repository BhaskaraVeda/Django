from django.contrib import admin
from .models import Student_details

# Register your models here.

# admin.site.register(Student_details)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'student_phone_number', 'student_email']
    # list_display_links = ['name']
admin.site.register(Student_details,StudentAdmin)
