# coding=utf-8
from rest_framework import viewsets

from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing company instances.
    """
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
