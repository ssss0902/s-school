# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Data(models.Model):
	direction = models.CharField(max_length=10, default='00')
	forward = models.CharField(max_length=10, default = '+1')
	backward = models.CharField(max_length=10, default = '00')
	breaker = models.CharField(max_length=10, default = '00')
	speed = models.CharField(max_length=10, default = '0km/h')
	td = '+100000000'
	total_data = models.CharField(max_length=100, default=td)
	def __str__(self):
		return self.total_data
