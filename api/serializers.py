from rest_framework import serializers
from .models import Employee
import re

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def validate_email(self, value):
        if not value.endswith("@company.com"):
            raise serializers.ValidationError(
                "Email must belong to the company domain (@company.com)."
            )
        return value

    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError("Salary must be a positive value.")
        return value

    def validate_emp_id(self, value):
        pattern = r"^EMP\d+$"
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "emp_id must follow the format 'EMP' followed by digits (e.g., EMP001)."
            )
        return value
