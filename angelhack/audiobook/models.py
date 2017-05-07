from __future__ import unicode_literals

from django.db import models

RELIGION_CHOICES = (
	('HINDUISM','Hinduism'),
	('CHRISTIANITY','Christianity'),
	('JUDAISM', 'Judaism'),
	('ISLAM','Islam'),
	('TAOISM','Taoism'),
	('BUDDHISM','Buddhism'),
	('SIKHISM','Sikhism'),
)

class Info(models.Model):
	email = models.EmailField(blank=True, null=True)
	Full_Name = models.CharField(max_length=120, blank=False, null=True)
	Phone_No = models.CharField(max_length=13, blank=False, null=True)
	City = models.CharField(max_length=100, blank=False, null=True)
	Religion = models.CharField(max_length=200, choices=RELIGION_CHOICES, blank=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.Full_Name