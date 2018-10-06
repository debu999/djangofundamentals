"""Django rest framework api returns"""

from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Employee
        # fields = ("firstname ", "lastname", "sid")

        fields = "__all__"
