from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'emp_id',
        'name',
        'email',
        'designation',
        'department',
        'salary',
        'date_joined',
        'is_active',
    )

    list_filter = (
        'designation',
        'department',
        'is_active',
        'date_joined',
    )

    search_fields = (
        'emp_id',
        'name',
        'email',
        'designation',
        'department',
    )

    ordering = ('emp_id',)
