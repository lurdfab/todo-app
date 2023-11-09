from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDo
        fields = ("title", "description", "date", "completed", "owner")
        # read_only_fields = ["owner",]