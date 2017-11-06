# coding=utf-8
from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    """Serializer for company"""
    class Meta:
        model = Company
        fields = ('id', 'name', 'email', 'phone', 'address')
