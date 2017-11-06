# coding=utf-8
from django.db import models


class Company(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phone = models.TextField()
    address = models.TextField(blank=True)
