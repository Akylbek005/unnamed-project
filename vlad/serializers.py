from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from django.contrib.auth import authenticate

from .models import VladModels


class VladModelsSerializer(serializers.ModelSerializer):
    from_whom = serializers.CharField(max_length=64)

    class Meta:
        model = VladModels
        fields = '__all__'
