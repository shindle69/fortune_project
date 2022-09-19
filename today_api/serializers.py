from rest_framework import serializers
from .models import Today12

class Today12Serializer(serializers.Serializer):

    class Meta:
        model = Today12
        fields = '__all__'